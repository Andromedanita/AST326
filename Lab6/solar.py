import numpy as np
import os
import matplotlib.pylab as plt


filenames=os.listdir("sun-170ms")
darknames=os.listdir("dark-170ms")
files=[]
darks=[]
sum_file=np.zeros(3652)
sum_dark=np.zeros(3652)
pixel=np.arange(0,3652,1)

for i in range(0,66,1):
    file='/Users/anita/Documents/University_Third_Year/AST326/Lab6/solar_data/sun-170ms/'+filenames[i]
    loaded_files=np.loadtxt(file)
    files.append(loaded_files)
    sum_file+=files[i]
mean_file=sum_file/66#(np.size(files))


for j in range(0,58,1):
    dark='/Users/anita/Documents/University_Third_Year/AST326/Lab6/solar_data/dark-170ms/'+darknames[j]
    loaded_darks=np.loadtxt(dark)
    darks.append(loaded_darks)
    sum_dark+=darks[j]
mean_dark=sum_dark/58#(np.size(darks))

corrected=mean_file-mean_dark

plt.plot(pixel,mean_file)
plt.plot(pixel,corrected)
plt.legend(('Raw Data','Dark Subtracted'),loc='best')
plt.title("Solar Spectrum")
plt.xlabel("Pixel")
plt.ylabel("Intensity")
plt.show()