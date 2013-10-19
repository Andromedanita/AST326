#Plotting wavelength vs. pixel number for neon and fluor data sets
import numpy as np
import matplotlib.pylab as plt
from scipy.optimize import leastsq


trial=[1,2,3,4,5,6]
mean_list=[]
variance=[]

for i in trial:
    file="/Users/anita/Desktop/University_Third_Year/AST326/Lab2/100msSUN"+str(i)+".txt"
    pixel=np.loadtxt(file, usecols=(0,))
    intensity=np.loadtxt(file, usecols=(1,))
    plt.plot(pixel,intensity)
    #mean=np.sum(intensity/np.size(intensity))
    #sd=np.sqrt(sum((intensity-mean)**2)/(np.size(intensity)-1))
    #mean_list.append(mean)
    #variance.append(sd)
plt.xlabel('pixel number')
plt.ylabel('wavelength(nm)')
plt.title('wavelength vs. pixel number of LAMP')
plt.legend(('trial 1','trial 2','trial 3','trial 4','trial 5','trial 6'),loc='best')
plt.plot(mean_list,variance,'o')

'''
p0=(0.0, 10)

def peval(pixel,intensity):
    return p[0]+p[1]*pixel

def residuals (p,pixel,intensity, peval1):
    return pixel - peval(intensity,p)

plsq1 = leastsq(residuals,p0,args=(pixel,intensity,peval),maxfev=2000)


ma =np.array([[np.sum(pixel**2),np.sum(pixel)],[np.sum(pixel),len(pixel)]])
mc =np.array([[np.sum(pixel*intensity)],[np.sum(intensity)]])

mai = np.linalg.inv(ma)
md = np.dot(mai,mc)

mfit = md[0,0]
cfit = md[1,0]

plt.plot(pixel,mfit*pixel+cfit)
'''
plt.show()
