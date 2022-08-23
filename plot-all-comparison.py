import os
import matplotlib.pyplot as plt
import numpy as np
import json
import seaborn as sns; sns.set()
import glob2
import argparse


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

for dir in  list_of_dirs:
    results = load_results(os.path.join(args.dir, dir, 'progress.csv'))
    if not results:
        print('skipping {}'.format(os.path.join(args.dir, dir)))
        continue

    success_rate = np.array(results['test/success_rate'])
    reward = np.array(results['test/reward'])
    mean_Q = np.array(results['test/mean_Q'])
    epoch = np.array(results['epoch']) + 1
    config = dir

    # success_rate
    assert success_rate.shape == epoch.shape
    x = epoch
    y = success_rate
    if args.smooth:
        x, y = smooth_reward_curve(epoch, success_rate)
    assert x.shape == y.shape

    if config not in success_rate_array:
        success_rate_array[config] = []
    success_rate_array[config].append((x, y))

    # reward
    assert reward.shape == epoch.shape
    x = epoch
    y = reward
    if args.smooth:
        x, y = smooth_reward_curve(epoch, reward)
    assert x.shape == y.shape

    if config not in reward_array:
        reward_array[config] = []
    reward_array[config].append((x, y))

    # mean_Q
    assert mean_Q.shape == epoch.shape
    x = epoch
    y = mean_Q
    if args.smooth:
        x, y = smooth_reward_curve(epoch, mean_Q)
    assert x.shape == y.shape

    if config not in mean_Q_array:
        mean_Q_array[config] = []
    mean_Q_array[config].append((x, y))

# plot rewards
plt.clf()
for config in sorted(reward_array.keys()):
    xs, ys = zip(*reward_array[config])
    xs, ys = pad(xs), pad(ys)
    assert xs.shape == ys.shape

    plt.plot(xs[0], np.nanmedian(ys, axis=0), label=config)

plt.fill_between(xs[0], np.nanpercentile(ys, 25, axis=0), np.nanpercentile(ys, 75, axis=0), alpha=0.25)
plt.title('Reward vs epochs')
plt.xlabel('epochs')
plt.ylabel('Reward')
plt.legend()
plt.savefig(os.path.join(args.dir, 'fig_{}.png'.format('rewardsVSepochs')))
plt.show()

# plot success rate
plt.clf()
for config in sorted(success_rate_array.keys()):
    xs, ys = zip(*success_rate_array[config])
    xs, ys = pad(xs), pad(ys)
    assert xs.shape == ys.shape

    plt.plot(xs[0], np.nanmedian(ys, axis=0), label=config)

plt.fill_between(xs[0], np.nanpercentile(ys, 25, axis=0), np.nanpercentile(ys, 75, axis=0), alpha=0.25)
plt.title('Success rate vs epochs')
plt.xlabel('epochs')
plt.ylabel('Success rate')
plt.legend()
plt.savefig(os.path.join(args.dir, 'fig_{}.png'.format('successRateVSepochs')))
plt.show()

# plot Q value rate
plt.clf()
for config in sorted(mean_Q_array.keys()):
    xs, ys = zip(*mean_Q_array[config])
    xs, ys = pad(xs), pad(ys)
    assert xs.shape == ys.shape

    plt.plot(xs[0], np.nanmedian(ys, axis=0), label=config)

plt.fill_between(xs[0], np.nanpercentile(ys, 25, axis=0), np.nanpercentile(ys, 75, axis=0), alpha=0.25)
plt.title('Average Q values vs epochs')
plt.xlabel('epochs')
plt.ylabel('Average Q value')
plt.legend()
plt.savefig(os.path.join(args.dir, 'fig_{}.png'.format('averageQVSepochs')))
plt.show()

