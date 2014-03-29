import numpy as np
import os
import matplotlib.pylab as plt



filenames=os.listdir("sun-200ms")
darknames=os.listdir("dark-200ms")
flatnames=os.listdir("flats")
files=[]
darks=[]
flats=[]
sum_file=np.zeros(3652)
sum_dark=np.zeros(3652)
pixel=np.arange(0,3652,1)


######## files #######
means=[]
for i in range(0,55,1):
    file='/Users/anita/Documents/University_Third_Year/AST326/Lab6/solar_data/sun-200ms/'+filenames[i]
    loaded_files=np.loadtxt(file)
    files.append(loaded_files)
    mean_file=np.mean(files[i])
    means.append(mean_file)

dark_means=[]
####### darks #########
for j in range(0,39,1):
    dark='/Users/anita/Documents/University_Third_Year/AST326/Lab6/solar_data/dark-200ms/'+darknames[j]
    loaded_darks=np.loadtxt(dark)
    darks.append(loaded_darks)
    mean_dark=np.mean(darks[j])
    dark_means.append(mean_dark)

dark_value=np.mean(dark_means)

flat_means=[]
####### flats #########
for m in range(0,39,1):
    flat='/Users/anita/Documents/University_Third_Year/AST326/Lab6/solar_data/flats/'+flatnames[m]
    loaded_flats=np.loadtxt(flat)
    flats.append(loaded_flats)
    mean_flats=np.mean(flats[m])
    flat_means.append(mean_flats)




corrected=means-dark_value
####### times ######
times=[]
np.savetxt("sun200ms-filenames.txt",filenames,fmt='%s')
for k in range(0,55,1):
    names=np.loadtxt('sun200ms-filenames.txt',dtype='str')
    minutes=names[k][18:20]    # taking minute parts of the file name
    minutes=float(minutes)*60    # converting str to int and converting to seconds
    seconds=names[k][20:22]    # taking second parts of the file name
    seconds=float(seconds)       #converting str to int
    miliseconds=names[k][22:25] # taking mili second parts of the file name
    miliseconds=float(miliseconds)/1000 #converting str to int and converting to seconds
    time=minutes+seconds+miliseconds
    times.append(time)

times = np.array(times)
#times -= times[0]

t_center=3918.7240000000002#1805.3589999999999#1812.8965 #78.1875#np.median(times)
Delta_t=(times[51]-times[10])/2
I_o=8421#np.median(corrected)
I=I_o*((2./5)+((3./5)*(np.sqrt(1-(((times-t_center)**2)/(Delta_t**2))))))
#I_o = 7550
#t_center = 78.77
#Delta_t = -64.67

#I = I_o*((2./5)+(3./5)*np.sqrt(1-((times-t_center)/Delta_t)**2))


plt.plot(times,corrected,'o')
plt.plot(times,I,'r')
plt.title('Relative flux vs. Time - Sun 200ms')
plt.xlabel('Time(seconds)')
plt.ylabel('Relative Flux')
plt.legend(('Dark Subtracted Data','Limb Darkening'),loc='center')
plt.show()

