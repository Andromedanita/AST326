import numpy as np
import matplotlib.pylab as plt
import math

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


#a for loop in order to open the file and calculate the mean and standard deviation
for i in runs:
    file='/Users/anita/Desktop/University_Third_Year/AST326/Data/SMALLRATEtask8pmtrunno_'+str(i)+'count0.001.dat'
    x=np.loadtxt(file)
    mean=np.sum(x)/np.size(x)                    #the mean
    sd=np.sqrt(sum((x-mean)**2)/(np.size(x)-1))  #standard deviation
    poisson_distribution=((mean**x)*(np.exp((-1)*mean)))/(factorial(x.all()))   #poisson distribution
    gaussian_distribution=(1.0/(sd*(np.sqrt(2*np.pi))))*(np.exp(-0.5*(((x-mean)/sd)**2)))   #gaussian distribution
    poisson.append(poisson_distribution)         #appending the poisson distribution points to the poisson list
    gaussian.append(gaussian_distribution)       #appending the gaussian distribution points to the gaussian list
    poisson1=np.array(poisson)
    gaussian1=np.array(gaussian)
    #plotting poisson and gaussian distribution points vs. x(counts)
    plt.plot(x,poisson1,'*')
    plt.plot(x,gaussian1,'-o')
    plt.legend(('poisson distribution','gaussian distribution'),loc='best')
    plt.title('poisson and gaussian distribution')
    plt.show()    
