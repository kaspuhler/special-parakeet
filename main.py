import numpy as np
import matplotlib.pyplot as plt
from definitions import *
import os
import glob
import dicom

dataDir = os.getcwd() + '/Studies/'
tracer  = 'FDG'
pidList = glob.glob(dataDir + '*'+tracer+'*')

pulseSeqs = ['gre_vte', 'DTI/DSI', 'pCASL']

pidCounter=0
for pid in pidList:
    Subject=Subject(pidList[pidCounter])
    LM=ListMode(Subject.pid)
    pidCounter+=1

PathDicom='/Users/kspuhler/Research/CUBIT_MoCo/Studies/SHFDG155/MRI'
lstFilesDCM = []  # create an empty list
for dirName, subdirList, fileList in os.walk(PathDicom):
    for filename in fileList:
        if ".dcm" in filename.lower():  # check whether the file's DICOM
             lstFilesDCM.append(os.path.join(dirName, filename))

for i in lstFilesDCM:
    print(dicom.read_file(i).SeriesDescription)