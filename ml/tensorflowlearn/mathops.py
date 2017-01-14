# Solution is available in the other "solution.py" tab
import tensorflow as tf

# TODO: Convert the following to TensorFlow:
x = tf.placeholder(tf.int32)
y = tf.placeholder(tf.int32)
z = tf.sub(tf.div(x, y), 1)

# TODO: Print z from a session
with tf.session() as sess:
    output = sess.run(z, feed_dict={x:10, y:2})
    print(output)