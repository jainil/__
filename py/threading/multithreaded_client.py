import pickle
import socket
import threading

class ConnectionThread(threading.Thread):
    def run(self):
        #Connect to server
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(('localhost',2727))

        #Retrieve and unpickle the list object
        print pickle.loads(client.recv(1024))  #1024 is the buf size

        #Send dome messages
        for x in xrange(10):
            client.send('Hey' + str(x) + '\n')

        #Close connection
        client.close()

#Spawn a few threads
for x in xrange(5):
    ConnectionThread().start()
    
