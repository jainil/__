import threading
from time import sleep
import os

# Layout of the table (P = philosopher, f = fork):
#          P0
#       f3    f0
#     P3        P1
#       f2    f1
#          P2

# Number of philosophers at the table. 
# There'll be the same number of forks.
numPhilosophers = 4

# Lists to hold the philosophers and the forks.
# Philosophers are threads while forks are locks.
philosophers = []
forks = []

class Philosopher(threading.Thread):
  def __init__(self, index):
    threading.Thread.__init__(self)
    self.index = index

  def run(self):
     