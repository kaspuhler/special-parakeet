import numpy as np
import matplotlib.pyplot as plt
from definitions import *
import os
import glob

dataDir = os.getcwd() + '/Studies/'
tracer  = 'FDG'
pidList = glob.glob(dataDir + '*'+tracer+'*')

pidCounter=0
for pid in pidList:
    Subject=Subject(pidList[pidCounter])
    LM=ListMode(Subject.pid)
    pidCounter+=1