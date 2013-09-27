import numpy as np
import matplotlib.pylab as plt
import math
import scipy.misc as sc

#Two empty lists 
poisson=[]
gaussian=[]

#for 6 different runs
runs=[1,2,3,4,5,6]

#function for calculating the factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

hmin=0
hmax=40
hr=np.arange(hmin,hmax+1,1)
#Histogram plots in subplots
#hist=np.zeros(hmax-hmin+1,dtype=np.int)

plt.figure(1)

#a for loop in order to open the file and calculate the mean and standard deviation
for i in runs:
    file='/Users/anita/Desktop/University_Third_Year/AST326/Data/SMALLRATEtask8pmtrunno_'+str(i)+'count0.001.dat'
    x=np.loadtxt(file)
    x_max=max(x)
    x_min=min(x)
    y=np.arange(x_min,x_max,0.1)
    g=np.arange(x_min,x_max)
    mean=np.sum(x)/np.size(x)                    #the mean
    sd=np.sqrt(sum((x-mean)**2)/(np.size(x)-1))  #standard deviation
    poisson_distribution=((mean**g)*(np.exp((-1)*mean)))/(sc.factorial(g))   #poisson distribution
    gaussian_distribution=(1.0/(sd*(np.sqrt(2*np.pi))))*(np.exp(-0.5*(((y-mean)/sd)**2)))   #gaussian distribution
    poisson.append(poisson_distribution)         #appending the poisson distribution points to the poisson list
    gaussian.append(gaussian_distribution)       #appending the gaussian distribution points to the gaussian list
    #plotting poisson and gaussian distribution points vs. x(counts)
   # plt.subplot(3,2,i)
    for j in hr:
        hist=np.array([np.where(x==j)[0].size for j in hr])
    plt.subplot(3,2,i)
    plt.plot(hr,hist,drawstyle='steps-mid',lw=2,color='green')
    plt.plot(g,poisson_distribution*1000,'-m')
    plt.plot(y,gaussian_distribution*1000,'-b')
    plt.legend(('histogram','poisson distribution','gaussian distribution'),loc='best',prop={'size':10})
    plt.xlim(0,15)
    plt.title('poisson and gaussian distribution')
plt.show()    
