import threading
import time

def hello(x):
    print 'hello! ',x



for x in xrange(10):
    t = threading.Timer(10.0, hello(x))
    t.start()
    
