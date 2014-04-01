import numpy as np
import matplotlib.pylab as plt
import os


filenames=os.listdir("sun2")
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
for i in range(0,92,1):
    file='/Users/anita/Documents/University_Third_Year/AST326/Lab6/solar_data/sun2/'+filenames[i]
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


####### flats #########
flat_means=[]
flat_median_list=[]
flat_array=np.zeros(3652)

for m in range(0,48,1):
    flat='/Users/anita/Documents/University_Third_Year/AST326/Lab6/solar_data/march-18-flats/'+flatnames[m]
    loaded_flats=np.loadtxt(flat)
    flats.append(loaded_flats)
    flat_median=np.median(flats[m])
    flatss=flats[m]/flat_median
    flat_array+=flatss
flat_array=flat_array/48
flat_correct=np.mean(flat_array)



###### dark flats ######
darkflat_list=[]
darkflats=[]
for l in range(0,48,1):
    darkflat='/Users/anita/Documents/University_Third_Year/AST326/Lab6/solar_data/march-18-darkflat/'+darkflatnames[l]
    loaded_darkflats=np.loadtxt(darkflat)
    darkflats.append(loaded_darkflats)
    mean_darkflats=np.mean(darkflats[l])
    darkflat_list.append(mean_darkflats)

darkflat_value=np.mean(darkflat_list)



corrected=(means-dark_value)/flat_correct#/(flat_correct-darkflat_value)
####### times ######
times=[]
np.savetxt("sun2-filenames.txt",filenames,fmt='%s')
for k in range(0,92,1):
    names=np.loadtxt('sun2-filenames.txt',dtype='str')
    minutes=names[k][15:17]    # taking minute parts of the file name
    minutes=float(minutes)*60    # converting str to int and converting to seconds
    seconds=names[k][17:19]    # taking second parts of the file name
    seconds=float(seconds)       #converting str to int
    miliseconds=names[k][19:22] # taking mili second parts of the file name
    miliseconds=float(miliseconds)/1000 #converting str to int and converting to seconds
    time=minutes+seconds+miliseconds
    times.append(time)

times = np.array(times)
#times -= times[0]

t_center=1716.7909999999999#times[6]+(times[82]-times[6])#1812.8965 #78.1875#np.median(times)
Delta_t=(times[82]-times[6])/2
I_o=  5200#5089.0822103348455
I=I_o*((2./5)+((3./5)*(np.sqrt(1-(((times-t_center)**2)/(Delta_t**2))))))

##### plotting wavelength of two ending points ########
file1=(files[6]-dark_value)/flat_correct
file2=(files[82]-dark_value)/flat_correct

wavelength=(pixel*(0.014))+524.61
'''
plt.plot(wavelength,file1,'b')
plt.plot(wavelength,file2,'r')
plt.title("Intensity vs. Wavelength for sun 125ms")
plt.xlabel("Wavelength(nm)")
plt.ylabel("Intensity")
plt.legend(('First Spectrum','Second Spectrum'),loc='best')
'''
'''
#### plotting limb darkening#######
plt.plot(times,corrected,'o')
plt.plot(times,I,'r')
plt.title('Relative flux vs. Time -Sun 170ms')
plt.xlabel('Time(seconds)')
plt.ylabel('Relative Flux')
plt.legend(('Dark Subtracted Data','Limb Darkening'),loc='best')
'''



#### finding lag #######
file1=file1*(np.hanning(3652))
file2=file2*(np.hanning(3652))
mean=np.mean(file1)
mean2=np.mean(file2)
n=np.size(file1)
covariance_list=[]
p_list=[]
for p in range(-10,10,1):
    tester=np.roll(file2,p)
    p_list.append(p)
    numbers=[]
    for h in range(0,3652,1):
        #multiplications=((file1[h]*tester[h])-((n/(n-1))*((mean)**2)))
        multiplications=(file1[h]-mean)*(tester[h]-mean2)
        numbers.append(multiplications)
    sums=np.sum(numbers)
    sums=np.array(sums)
    #covariance=((1/n)-1)*sums
    covariance=1./(n-1)*sums
    covariance_list.append(covariance)

#covariance_list=np.array(covariance_list)
#covariance_list=covariance_list/3572926.5362021714


#### finding centroid of cross-correlation #####
cents=[]

for g in range(6,82,1):
    nums=[]
    denoms=[]
    for n in p_list:
        num=(n*covariance_list[n])
        denom=(covariance_list[n])
        nums.append(num)
        denoms.append(denom)
    numerator=np.sum(nums)
    denominator=np.sum(denoms)
    cent=numerator/denominator
    cents.append(cent)

c=3*1e8  # speed of light

blah = np.array([0.,cent])
w=(5.22780795e+02+ (1.57108757e-02*blah) -(4.52128794e-07*blah**2))
v = c*(w[1]-w[0])/w[0] # 2 * radial velocity
v_rad=v/2 # in meters


'''
p_list=np.array(p_list)
sd=np.sqrt(sum((p_list+0.05)**2)/(np.size(p_list)-1))
gaussian_distribution=(1.0/(sd*(np.sqrt(2*np.pi))))*(np.exp(-0.5*(((p_list+0.5)/sd)**2)))
plt.plot(p_list,gaussian_distribution*55000000)
'''

index=covariance_list.index(max(covariance_list))  # finding the index of the minimum covariance values
print "lag is:", p_list[index]   #printing index of minimum covariance

##### angular size of the sun ########
theta=(360*(times[82]-times[6]))/(3600*24)
'''
##### blackbody fitting ######    
b=[]
for o in wavelength:
    v=c/(wavelength*(10**(-10)))
    B=(2*h*(v))/((c**2)*0.36787944117144233)
b.append(B)

f=file1/blah
f2=file2/b
'''

plt.plot(p_list,covariance_list)
plt.plot(p_list[index],(np.max(covariance_list)),'o')
plt.title("covariance vs. pixel values")
plt.xlabel("Pixel")
plt.ylabel("Covariance")
plt.grid()
plt.show()
