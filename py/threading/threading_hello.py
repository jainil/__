import threading

class MyThread(threading.Thread):
    def run(self):
        print'Yello!'

MyThread().start()
