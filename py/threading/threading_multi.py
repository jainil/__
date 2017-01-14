##import threading
##
##theVar=1
##
##class MyThread(threading.Thread):
##    def run(self):
##        global theVar
##        print 'This is thread' + str(theVar) +'speaking'
##        print ':P xD'
##        theVar = theVar + 1
##
##for x in xrange(20):
##    MyThread().start()

import threading

#global theVar

theVar = 0

class MyThread ( threading.Thread ):
    def run ( self ):
        global theVar
        theVar = theVar + 1
        print 'This is thread ' + str ( theVar ) + ' speaking.'
        print 'Hello and good bye from thread' + str(theVar)
        

for x in xrange ( 20 ):
    MyThread().start()

