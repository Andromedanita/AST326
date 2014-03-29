import numpy as np
import os
import matplotlib.pylab as plt
from savitzky_golay import * #savitzky_golay



filenames=os.listdir("sun-170ms")
darknames=os.listdir("dark-170ms")
flatnames=os.listdir("flats")
files=[]
darks=[]
flats=[]
sum_file=np.zeros(3652)
sum_dark=np.zeros(3652)
pixel=np.arange(0,3652,1)


######## files #######
means=[]
for i in range(0,66,1):
    file='/Users/anita/Documents/University_Third_Year/AST326/Lab6/solar_data/sun-170ms/'+filenames[i]
    loaded_files=np.loadtxt(file)
    files.append(loaded_files)
    mean_file=np.mean(files[i])
    means.append(mean_file)

dark_means=[]
####### darks #########
for j in range(0,58,1):
    dark='/Users/anita/Documents/University_Third_Year/AST326/Lab6/solar_data/dark-170ms/'+darknames[j]
    loaded_darks=np.loadtxt(dark)
    darks.append(loaded_darks)
    mean_dark=np.mean(darks[j])
    dark_means.append(mean_dark)

dark_value=np.mean(dark_means)

flat_means=[]
flat_median_list=[]
####### flats #########
for m in range(0,39,1):
    flat='/Users/anita/Documents/University_Third_Year/AST326/Lab6/solar_data/flats/'+flatnames[m]
    loaded_flats=np.loadtxt(flat)
    flats.append(loaded_flats)
    flat_median=np.median(flats)
    flat_median_list.append(flat_median)
    #flat1=flats/flat_median
    #flat_median_list.append(flat1)
    #mean_flats=np.mean(flat_median_list)
    #flat_means.append(mean_flats)

#t=np.arange(0,39,1)
#plt.plot(t,flat_median_list)



corrected=means-dark_value
####### times ######
times=[]
#np.savetxt("sun170ms-filenames.txt",filenames,fmt='%s')
for k in range(0,66,1):
    names=np.loadtxt('sun170ms-filenames.txt',dtype='str')
    minutes=names[k][17:19]    # taking minute parts of the file name
    minutes=float(minutes)*60    # converting str to int and converting to seconds
    seconds=names[k][19:21]    # taking second parts of the file name
    seconds=float(seconds)       #converting str to int
    miliseconds=names[k][21:24] # taking mili second parts of the file name
    miliseconds=float(miliseconds)/1000 #converting str to int and converting to seconds
    time=minutes+seconds+miliseconds
    times.append(time)

times = np.array(times)
#times -= times[0]

t_center=1812.8965 #78.1875#np.median(times)
Delta_t=(times[59]-times[5])/2
I_o=7550#np.median(corrected)
I=I_o*((2./5)+((3./5)*(np.sqrt(1-(((times-t_center)**2)/(Delta_t**2))))))
#I_o = 7550
#t_center = 78.77
#Delta_t = -64.67
#I = I_o*((2./5)+(3./5)*np.sqrt(1-((times-t_center)/Delta_t)**2))

#Smoothing
correct=(files[7]-dark_value)
wavelength=(pixel*(0.014))+524.61
smoothed=savitzky_golay(correct,window_size=31, order=4)


#plt.plot(times,corrected,'o')
plt.plot(wavelength,correct)
plt.plot(wavelength,smoothed,'r')
#plt.plot(times,I,'r')
plt.title('Relative flux vs. Time -Sun 170ms')
#plt.xlabel('Time(seconds)')
plt.ylabel('Relative Flux')
plt.xlabel('Wavelength(nm)')
#plt.legend(('Dark Subtracted Data','Limb Darkening'),loc='best')
plt.legend(('Corrected Data','Smoothed'),loc='best')
plt.show()

