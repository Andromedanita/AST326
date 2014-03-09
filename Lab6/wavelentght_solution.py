import numpy as np
import os
import matplotlib.pyplot as plt
#from scipy import leastsq

filenames=os.listdir("neon_200ms")
darknames=os.listdir("neon_200ms_dark")
files=[]
darks=[]
sum_file=np.zeros(3652)
sum_dark=np.zeros(3652)
pixel=np.arange(0,3652,1)

for i in range(0,310,1):
    #pathname=os.path.join("neon_200ms", filenames[i])
    file='/Users/anita/Documents/University_Third_Year/AST326/Lab6/Group_B/neon_200ms/'+filenames[i]
    dark='/Users/anita/Documents/University_Third_Year/AST326/Lab6/Group_B/neon_200ms_dark/'+darknames[i]
    loaded_files=np.loadtxt(file)
    loaded_darks=np.loadtxt(dark)
    files.append(loaded_files)
    darks.append(loaded_darks)
    sum_file+=files[i]
    mean_file=sum_file/(np.size(files))
    sum_dark+=darks[i]
    mean_dark=sum_dark/(np.size(darks))
corrected=mean_file-mean_dark
plt.plot(pixel,corrected)




