import numpy as np
import matplotlib.pylab as plt
import os


filenames=os.listdir("sun1")
darknames=os.listdir("march18-dark")
flatnames=os.listdir("march-18-flats")
darkflatnames=os.listdir("march-18-darkflat")
files=[]
darks=[]
flats=[]
sum_file=np.zeros(3652)
sum_dark=np.zeros(3652)
pixel=np.arange(0,3652,1)


######## files #######
means=[]
for i in range(0,75,1):
    file='/Users/anita/Documents/University_Third_Year/AST326/Lab6/solar_data/sun1/'+filenames[i]
    loaded_files=np.loadtxt(file)
    files.append(loaded_files)
    mean_file=np.mean(files[i])
    means.append(mean_file)

dark_means=[]
####### darks #########
for j in range(0,112,1):
    dark='/Users/anita/Documents/University_Third_Year/AST326/Lab6/solar_data/march18-dark/'+darknames[j]
    loaded_darks=np.loadtxt(dark)
    darks.append(loaded_darks)
    mean_dark=np.mean(darks[j])
    dark_means.append(mean_dark)

dark_value=np.mean(dark_means)

flat_means=[]
flat_median_list=[]
####### flats #########
for m in range(0,48,1):
    flat='/Users/anita/Documents/University_Third_Year/AST326/Lab6/solar_data/march-18-flats/'+flatnames[m]
    loaded_flats=np.loadtxt(flat)
    flats.append(loaded_flats)
    flat_median=np.median(flats)
    flat_median_list.append(flat_median)
#flat1=flats/flat_median
#flat_median_list.append(flat1)
#mean_flats=np.mean(flat_median_list)
#flat_means.append(mean_flats)


for l in range(0,48,1):
    darkflat='/Users/anita/Documents/University_Third_Year/AST326/Lab6/solar_data/march18-darkflat/'+darkflatnames[l]
    loaded_darkflats=np.loadtxt(darkflat)
    darkflats.append(loaded_darkflats)


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


plt.plot(times,corrected,'o')
plt.plot(times,I,'r')
plt.title('Relative flux vs. Time -Sun 170ms')
plt.xlabel('Time(seconds)')
plt.ylabel('Relative Flux')
plt.legend(('Dark Subtracted Data','Limb Darkening'),loc='center')
plt.show()
