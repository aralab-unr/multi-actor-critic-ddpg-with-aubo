import tensorflow as tf
import os
os.environ['CUDA_VISIBLE_DEVICES'] ="0"
config = tf.ConfigProto()
sess = tf.Session(config=config)