import numpy as np
import matplotlib.pylab as plt
import os
from savitzky_golay import * #savitzky_golay
from fix_sun import *
from scipy.optimize import leastsq

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
times= np.delete(times,54)
nice_values=files-dark_value/flat_correct
nice_values= np.delete(nice_values,54, axis=0)

#times -= times[0]

t_center=1716.7909999999999#times[6]+(times[82]-times[6])#1812.8965 #78.1875#np.median(times)
Delta_t=(times[82]-times[6])/2
I_o=  5200#5089.0822103348455
I=I_o*((2./5)+((3./5)*(np.sqrt(1-(((times-t_center)**2)/(Delta_t**2))))))

##### plotting wavelength of two ending points ########
file1=nice_values[6]#(files[6]-dark_value)/flat_correct
file2=nice_values[82]#(files[82]-dark_value)/flat_correct

wavelength=(pixel*(0.014))+524.61

smoothed=savitzky_golay(file1,window_size=601, order=1)
smoothed1=savitzky_golay(file2,window_size=601, order=1)

flat_curve1=file1/smoothed
flat_curve2=file2/smoothed1

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
plt.plot(times,nice_values,'o')
plt.plot(times,I,'r')
plt.title('Relative flux vs. Time -Sun 170ms')
plt.xlabel('Time(seconds)')
plt.ylabel('Relative Flux')
plt.legend(('Dark Subtracted Data','Limb Darkening'),loc='best')
'''

z=smooth(nice_values,10)

#### finding lag #######
'''
file1=file1*(np.hanning(3652))
file2=file2*(np.hanning(3652))
'''
mean=np.mean(z[6])
mean2=np.mean(z[81])
n=np.size(z[6])
covariance_list=[]
p_list=[]
for p in range(-10,10,1):
    tester=np.roll(z[81],p)
    p_list.append(p)
    numbers=[]
    for h in range(0,3652,1):
        #multiplications=((file1[h]*tester[h])-((n/(n-1))*((mean)**2)))
        multiplications=(z[6][h]-mean)*(tester[h]-mean2)
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

blah = np.array([0.,cent/2])
w=(5.22780795e+02+ (1.57108757e-02*blah) -(4.52128794e-07*blah**2))
v = c*(w[1]-w[0])/w[0] # 2 * radial velocity
v_rad=v/2 # in meters

##### solar plane angles in radians
eta=(335.0652*(np.pi))/180
wiggle=(-7.09*(np.pi))/180

##### converted radial velocity to real velocity
v_real=v_rad/((np.cos(eta))*(np.cos(wiggle)))

###### Period of rotation of the sun
Period=25.3*24*3600  #seconds

##### Radisu of Sun
R_sun=((v_real)*(Period))/(2*(np.pi))
True_R_sun=695500000 #meters

##### Angular size of the sun
theta=(360*(times[82]-times[6]))/(3600*24)
theta_rad=(theta*(np.pi))/180

####### AU calculation
AU=R_sun/(np.tan(theta_rad/2)) #meters
True_AU=1.496*1e11 #meters
ratio=AU/True_AU

'''
p_list=np.array(p_list)
sd=np.sqrt(sum((p_list+0.05)**2)/(np.size(p_list)-1))
gaussian_distribution=(1.0/(sd*(np.sqrt(2*np.pi))))*(np.exp(-0.5*(((p_list+0.5)/sd)**2)))
plt.plot(p_list,gaussian_distribution*55000000)
'''

index=covariance_list.index(max(covariance_list))  # finding the index of the minimum covariance values
print "lag is:", p_list[index]   #printing index of minimum covariance

##### angular size of the sun ########



######## Morten's flatting solution ########
#flat_sun=


##### blackbody fitting ######
'''
b=[]
k=1.38*1e-23
T=3695
H=6.62*1e-34
for o in wavelength:
    one=(2*H*(c**2))/((wavelength*(1e-9))**5)
    expo=np.exp(H*c/wavelength*k*T*(1e-9))
    two=1./(expo)
    B=one*two
    #v=c/(wavelength*(10**(-9)))
    #B=(2*h*(v))/((c**2)*0.36787944117144233)
b.append(B)
'''
'''
f=file1/blah
f2=file2/b


plt.plot(p_list,covariance_list)
plt.plot(p_list[index],(np.max(covariance_list)),'o')
plt.title("covariance vs. pixel values")
plt.xlabel("Pixel")
plt.ylabel("Covariance")
plt.grid()
'''



print "ratio is:", ratio
print "centroid is:", cent/2
print "v_rad is:", v_rad
print "AU value is:", AU



################ limb darkening fitting ########
x = times[6:82]
y = corrected[6:82]

#dy = 0.5
p0 = [5200.,1716.,64.]
#fit function
def peval(x, p):
    I_o,t_center,Delta_t = p
    return I_o*((2./5)+((3./5)*(np.sqrt(1-(((x-t_center)**2)/(Delta_t**2))))))

def residuals (p,y,x, peval):
    return (y) - peval(x,p)

p_final = leastsq(residuals,p0,args=(y,x, peval), full_output= True,maxfev=2000)

plt.figure()
plt.plot(x,peval(x,p_final[0]),'r')
plt.plot(x,y)

y_final = peval(x,p_final[0])
chi2 = np.sum((y - y_final)**2)#
resi = (residuals(p_final[0],y,x,peval))
dof = len(y)-len(p0)
chi_re2 = chi2/dof #
cov = p_final[1] * chi_re2


print "The inital parameter (p0) we used is:\n", p0
print "What we get as a parameter:", p_final[0]

if p_final[4] == 1: # change p_final[1] to success
    print "It converges."
else:
    print "It does not converge."

print "The Chi square is: \t\t\t",round(chi2,2)
print "The Chi-reduced square is: \t\t", round(chi_re2,2)
print

print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
print


################################################
'''

plt.subplot(211)
plt.plot(np.mean(z[5:81],axis=0))
#plt.plot(np.mean(z[5],axis=0))
plt.title("Smoother and Flattened using Gaussian")
plt.ylabel("Normalized Intensity")
plt.subplot(212)
plt.plot(pixel,flat_curve1)
plt.title("Smoothed and Flattened using Smoothing Function")
plt.xlabel("Pixel")
plt.ylabel("Normalized Intensity")
'''

plt.show()
