import tensorflow as tf
import os
os.environ['CUDA_VISIBLE_DEVICES'] ="0"
config = tf.ConfigProto(log_device_placement=True)
sess = tf.Session(config=config)