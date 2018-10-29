''' Module to test random strings of different lengths given a fixed length prime'''
import paderson_commitment
import os
from datetime import datetime
import subprocess
from threading import Thread
import random 
import constants


class nodeA(Thread):
    def __init__(self):
        Thread.__init__(self)
    
    def run(self):
        os.system('sleep 0.1; python3 node-A.py')



class nodeB(Thread):
    def __init__(self):
        Thread.__init__(self)
    
    def run(self):
        os.system('python3 node-B.py')


A = [i for i in range(10, 100, 5)]
P = [100, 140, 160, 180, 320, 384, 512]

c = open('100.csv', 'a')
p,g,q = paderson_commitment.generate_p_g_q()

f = open('constants.py', 'w')

i = constants.LENGTH_OF_PRIME

for j in A:
        
    port = random.randint(13000, 20000)
    f = open('constants.py', 'w')
    m = 'PORT = ' + str(port) + '\nSERVER_IP_ADDR = "127.0.0.1"\nSHARED_PRIME = ' + str(p) + '\nSHARED_BASE = 2\nRANDOM_STRING_LENGTH = ' + str(j) + '\nRAND_NUMBER_LOWER_BOUND = 100\nRAND_NUMBER_UPPER_BOUND = 1000\nLENGTH_OF_PRIME = ' + str(i) 
    f.write(m)
    f.close()
    os.system('sleep 1')

    b = nodeB()
    a = nodeA()

    start = datetime.now()

    b.start()
    a.start()
    a.join()
    b.join()

    end = datetime.now()
    print("Prime = {}, String Length = {}".format(i, j))

    t = (end - start).microseconds 

    s = str(i) + ',' + str(j) + ',' + str(t) + '\n'
    c.write(s)
    c.flush()


c.close()
        

        

