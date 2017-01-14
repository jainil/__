import pickle
import socket
import threading

#Pickle
someList = [1,2,9,7,0]
pickledList = pickle.dumps(someList)

#Thread class
class ClientThread(threading.Thread):
    #Override Thread's __init__ method to accept parameters needed
    def __init__(self, channel, details):
        self.channel = channel
        self.details = details
        threading.Thread.__init__(self)

    def run(self):
        print 'Received Connection:', self.details[0]
        self.channel.send(pickledList)
        for x in xrange(10):
            print self.channel.recv(1024)
        self.channel.close()
        print 'Closed Connection:', self.details[0]

#Set up the Server
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('',2727))
server.listen(5) #backlog - queue size of connections

#Have the server serve "forever"
while True:
    channel, details = server.accept()
    ClientThread(channel, details).start()
    
