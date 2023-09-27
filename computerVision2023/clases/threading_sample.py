""" 
Universidad Francisco Marroquin
Computer Vision
Author: Christian Medina Armas
"""

from threading import Thread
import time
import os

print(f'PID IS: {os.getpid()}')

i = 0
running = True


def thread1():
    """Print i, modified by thread 2
    """
    global i, running
    while running:
        print('Executing code. i = {0} \r'.format(i), end='')
    return None


def thread2():
    """Modify i
    """
    global i, running
    while running:
        i += 1
        time.sleep(1)
    return None


# create threads and assign functions
t1 = Thread(target=thread1, args=())
t2 = Thread(target=thread2, args=())

# start execution of threads
t1.start()
t2.start()

# do additional work and signal threads to stop
time.sleep(12)
running = False

# add to ensure that threads terminate properly
t1.join()
t2.join()


