import tensorflow as tf
from util import store_args, nn
import numpy as np


class MultiActorCritic:
    @store_args
    def __init__(self, inputs_tf, number_actors, number_critics, dimo, dimg, dimu, max_u, o_stats, g_stats, hidden, layers,
                 **kwargs):
        """The actor-critic network and related training code.
        Args:
            inputs_tf (dict of tensors): all necessary inputs for the network: the
                observation (o), the goal (g), and the action (u)
            number_actors (int): number of actors to be used
            number_critics (int): number of critics to be used
            dimo (int): the dimension of the observations
            dimg (int): the dimension of the goals
            dimu (int): the dimension of the actions
            max_u (float): the maximum magnitude of actions; action outputs will be scaled
                accordingly
            o_stats (baselines.her.Normalizer): normalizer for observations
            g_stats (baselines.her.Normalizer): normalizer for goals
            hidden (int): number of hidden units that should be used in hidden layers
            layers (int): number of hidden layers
        """
        self.o_tf = inputs_tf['o']
        self.g_tf = inputs_tf['g']
        self.u_tf = inputs_tf['u']

        # Prepare inputs for actor and critic.
        o = self.o_stats.normalize(self.o_tf)
        g = self.g_stats.normalize(self.g_tf)
        input_pi = tf.concat(axis=1, values=[o, g])  # for actor

        # Networks.
        # actors
        with tf.variable_scope('pi'):
            # self.pi_tf = self.max_u * tf.tanh(nn(
            #     input_pi, [self.hidden] * self.layers + [self.dimu]))
            self.pi_tf_array = [] # creating array of networks for actors
            for i in range(0, number_actors):
                self.pi_tf_array.append(self.max_u * tf.tanh(nn(input_pi, [self.hidden] * self.layers + [self.dimu], reuse=None, flatten=False, name=str('actor_'+str(i)))))

            # taking averages
            pi_tf_avg = self.pi_tf_array[0]
            for i in range(1, len(self.pi_tf_array)):
                pi_tf_avg = pi_tf_avg + self.pi_tf_array[i]
            self.pi_tf_avg = pi_tf_avg / len(self.pi_tf_array)

        # critics
        with tf.variable_scope('Q'):
            # for policy training
            self.pi_tf_avg = self.pi_tf_array[0]
            for i in range(1, len(self.pi_tf_array)):
                self.pi_tf_avg = self.pi_tf_avg + self.pi_tf_array[i]
            self.pi_tf_avg = self.pi_tf_avg / len(self.pi_tf_array)
            # input_Q = tf.concat(axis=1, values=[o, g, self.pi_tf / self.max_u])
            input_Q = tf.concat(axis=1, values=[o, g, self.pi_tf_avg / self.max_u])
            # self.Q_pi_tf = nn(input_Q, [self.hidden] * self.layers + [1])
            self.Q_pi_tf_array = [] # creating array of networks for policy
            for i in range(0, number_critics):
                self.Q_pi_tf_array.append(nn(input_Q, [self.hidden] * self.layers + [1], None, False, str('critic_'+str(i)))) # 256 * 3
            self.Q_pi_tf_array = np.array(self.Q_pi_tf_array)

            # for critic training
            input_Q = tf.concat(axis=1, values=[o, g, self.u_tf / self.max_u])
            self._input_Q = input_Q  # exposed for tests
            # self.Q_tf = nn(input_Q, [self.hidden] * self.layers + [1], reuse=True)
            self.Q_tf_array = []  # creating array of networks for critics
            for i in range(0, number_critics):
                self.Q_tf_array.append(nn(input_Q, [self.hidden] * self.layers + [1], reuse=True, flatten=False, name=str('critic_'+str(i))))
            self.Q_tf_array = np.array(self.Q_tf_array)


            # taking averages
            Q_pi_tf_array = self.Q_pi_tf_array
            Q_pi_tf_avg = Q_pi_tf_array[0]
            for i in range(1, len(Q_pi_tf_array)):
                Q_pi_tf_avg = Q_pi_tf_avg + Q_pi_tf_array[i]
            self.Q_pi_tf_avg = Q_pi_tf_avg / len(Q_pi_tf_array)

            Q_tf_avg = self.Q_tf_array[0]
            for i in range(1, len(self.Q_tf_array)):
                Q_tf_avg = Q_tf_avg + self.Q_tf_array[i]
            self.Q_tf_avg = Q_tf_avg / len(self.Q_tf_array)
