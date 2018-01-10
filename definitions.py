class Subject: #This class will be the main one, everything else will be dependent upon it
    def __init__(self, directory):
        self.pid=directory
        self.petDir=self.pid+'/PET/'
        self.mriDir=self.pid+'/MRI/'


class ListMode(Subject): #This is the main class that holds, reads and processes listmode stuff
    def __init__(self, directory): #Constructor, argument points to the LM file name
        import glob
        Subject.__init__(self, directory)
        self.lmFile    = glob.glob(self.petDir + '*.l')[0]
        self.lmFileHDR = glob.glob(self.petDir + '*.l.hdr')[0]
        self.scanTime  = self.read_lm_header()
        self.read_lm_main()


    def read_lm_header(self): #checked this, working, returns the time listed in STUDY TIME
        with open(self.lmFileHDR,'r') as hdr:
            for line in hdr:
                if line.startswith('%study time'):
                    time=line.split(':=')[1]
                    h, m, s = time.split(':')
                    h=int(h)
                    m=int(m)
                    s=int(s)
                    h = h - 5 #deals with communist GMT time
                    time = 3600 * h + 60 * m + s #convert hh:mm:ss to seconds
                    return time

    def read_lm_main(self):
        import struct
        with open(self.lmFile,'rb') as lm:
            for line in lm:
                buff = lm.lineread()




#class Times(): # This is going to be a class for dealing with lining up PET/MRI times


#def point_to_pet_and_mri(directoryPath):
