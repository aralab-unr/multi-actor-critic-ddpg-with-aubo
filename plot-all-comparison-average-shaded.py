import os
import matplotlib.pyplot as plt
import numpy as np
import json
import seaborn as sns; sns.set()
import glob2
import argparse
import pandas as pd
import seaborn as sns
import seaborn.timeseries

def smooth_reward_curve(x, y):
    halfwidth = int(np.ceil(len(x) / 60))  # Halfwidth of our smoothing convolution
    k = halfwidth
    xsmoo = x
    ysmoo = np.convolve(y, np.ones(2 * k + 1), mode='same') / np.convolve(np.ones_like(y), np.ones(2 * k + 1),
        mode='same')
    return xsmoo, ysmoo


def load_results(file):
    if not os.path.exists(file):
        return None
    with open(file, 'r') as f:
        lines = [line for line in f]
    if len(lines) < 2:
        return None
    keys = [name.strip() for name in lines[0].split(',')]
    data = np.genfromtxt(file, delimiter=',', skip_header=1, filling_values=0.)
    if data.ndim == 1:
        data = data.reshape(1, -1)
    assert data.ndim == 2
    assert data.shape[-1] == len(keys)
    result = {}
    for idx, key in enumerate(keys):
        result[key] = data[:, idx]
    return result


def pad(xs, value=np.nan):
    maxlen = np.max([len(x) for x in xs])

    padded_xs = []
    for x in xs:
        if x.shape[0] >= maxlen:
            padded_xs.append(x)

        padding = np.ones((maxlen - x.shape[0],) + x.shape[1:]) * value
        x_padded = np.concatenate([x, padding], axis=0)
        assert x_padded.shape[1:] == x.shape[1:]
        assert x_padded.shape[0] == maxlen
        padded_xs.append(x_padded)
    return np.array(padded_xs)

parser = argparse.ArgumentParser()
parser.add_argument('dir', type=str)
parser.add_argument('--smooth', type=int, default=1)
args = parser.parse_args()

reward_array={}
mean_Q_array={}
success_rate_array={}
list_of_dirs = os.listdir(args.dir)
epochs = 11
csv_name = 'temp_csv'
if os.path.exists(csv_name + '.csv'):
  os.remove(csv_name + '.csv')

# assign header columns
headerList = ['Config', 'Epoch', 'Success_rate', 'reward', 'q_value']
headerString = ''
for header in headerList:
    headerString += header + ' '
with open(csv_name + '.csv', 'a') as csv:
        csv.write(headerString + "\n")

for dir in  list_of_dirs:
    results = load_results(os.path.join(args.dir, dir, 'progress.csv'))
    if not results:
        print('skipping {}'.format(os.path.join(args.dir, dir)))
        continue

    success_rate = np.array(results['test/success_rate'])
    reward = np.array(results['test/reward'])
    mean_Q = np.array(results['test/mean_Q'])
    epoch = np.array(results['epoch']) + 1
    print(dir)
    config = dir.split("-")[0]
    run = dir.split("-")[1]

    # success_rate
    assert success_rate.shape == epoch.shape
    x = epoch
    y = success_rate
    if args.smooth:
        x, y = smooth_reward_curve(epoch, success_rate)
    assert x.shape == y.shape

    if config not in success_rate_array:
        success_rate_array[config] = {}
    if run not in success_rate_array[config]:
        success_rate_array[config][run] = []
    success_rate_array[config][run].append((x, y))

    success_rate_converted = success_rate

    # reward
    assert reward.shape == epoch.shape
    x = epoch
    y = reward
    if args.smooth:
        x, y = smooth_reward_curve(epoch, reward)
    assert x.shape == y.shape

    if config not in reward_array:
        reward_array[config] = {}
    if run not in reward_array[config]:
        reward_array[config][run] = []
    reward_array[config][run].append((x, y))

    reward_converted = reward

    # mean_Q
    assert mean_Q.shape == epoch.shape
    x = epoch
    y = mean_Q
    if args.smooth:
        x, y = smooth_reward_curve(epoch, mean_Q)
    assert x.shape == y.shape

    if config not in mean_Q_array:
        mean_Q_array[config] = {}
    if run not in mean_Q_array[config]:
        mean_Q_array[config][run] = []
    mean_Q_array[config][run].append((x, y))

    q_converted = mean_Q
    # create csv
    for i, j, k, l in zip(x, success_rate_converted, reward_converted, q_converted):
        if i > epochs:
            break
        record = str(config) + " " + str(int(i)) + " " + \
                 str(j) + " " + str(k) + " " + str(l) + "\n"
        # print(record)
        # print(abc)
        with open(csv_name + '.csv', 'a') as csv:
            csv.write(str(record))

def _plot_range_band(*args, central_data=None, ci=None, data=None, **kwargs):
    upper = data.max(axis=0)
    lower = data.min(axis=0)
    #import pdb; pdb.set_trace()
    ci = np.asarray((lower, upper))
    kwargs.update({"central_data": central_data, "ci": ci, "data": data})
    seaborn.timeseries._plot_ci_band(*args, **kwargs)

seaborn.timeseries._plot_range_band = _plot_range_band

# success rate
plt.clf()
cluster_overload = pd.read_csv(csv_name + '.csv', delim_whitespace=True)
cluster_overload['Unit'] = cluster_overload.groupby(['Config','Epoch']).cumcount()

ax = sns.tsplot(time='Epoch',value="Success_rate", condition="Config", unit="Unit", data=cluster_overload,
               err_style="range_band", n_boot=0)

plt.title('Success rate vs Epochs')
plt.xlabel('Epochs')
plt.ylabel('Success rate')
plt.legend()
plt.savefig(os.path.join(args.dir, 'fig_{}.png'.format('fig_successRateVSepochs_3_shaded')))
plt.show()

#reward
plt.clf()
cluster_overload = pd.read_csv(csv_name + '.csv', delim_whitespace=True)
cluster_overload['Unit'] = cluster_overload.groupby(['Config','Epoch']).cumcount()

ax = sns.tsplot(time='Epoch',value="reward", condition="Config", unit="Unit", data=cluster_overload,
               err_style="range_band", n_boot=0)

plt.title('Reward vs Epochs')
plt.xlabel('Epochs')
plt.ylabel('Reward')
plt.legend()
plt.savefig(os.path.join(args.dir, 'fig_{}.png'.format('fig_rewardsVSepochs_3_shaded')))
plt.show()

#q_value
plt.clf()
cluster_overload = pd.read_csv(csv_name + '.csv', delim_whitespace=True)
cluster_overload['Unit'] = cluster_overload.groupby(['Config','Epoch']).cumcount()

ax = sns.tsplot(time='Epoch',value="q_value", condition="Config", unit="Unit", data=cluster_overload,
               err_style="range_band", n_boot=0)

plt.title('Average Q values vs Epochs')
plt.xlabel('Epochs')
plt.ylabel('Average Q value')
plt.legend()
plt.savefig(os.path.join(args.dir, 'fig_{}.png'.format('fig_averageQVSepochs_3_shaded')))
plt.show()




