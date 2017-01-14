"""Thread pools

@author not:jainil
"""
import pickle
import Queue
import socket
import threading

#Pickle
someList = [1, 2, 4, 67, 2]
pickledList = pickle.dumps(someList)

#Revised thread class
class ClientThread(threading.Thread):

    #No need to change __init__
    #Queue module takes care of it

    def run(self):

        #Have it run 'forever'
        while True:

            #Get a client out of the queue
            client = clientPool.get()

            #Check if we actually have a client
            if client != None:
                print 'Received Connection:', client[1][0]
                client[0].send(pickledList)
                for x in xrange(10):
                    print client[0].recv(1024)
                client[0].close()
                print 'Closed Connection:', client[1][0]

#Create our q
clientPool = Queue.Queue(0)

#Start two threads
for x in xrange(2):
    ClientThread().start()

#Set up the server
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('',2727))
server.listen(5)

#Have the server serve "forever"
while True:
    clientPool.put(server.accept())


             
