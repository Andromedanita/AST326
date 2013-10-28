#Plotting wavelength vs. pixel number for neon and fluor data sets
import numpy as np
import matplotlib.pylab as plt
from scipy.optimize import leastsq


#mean_list=[]
#variance=[]
gaussian=[]
names=["Vega01","Vega02","Vega03"]#,"albero_01","albero_02","Erif01","Erif02"]
maximum_list=[]

#names=[Vega01,Vega02,Vega03,albero_01,albero_02,Erif01,Erif02]
#dark1=np.loadtxt('/Users/anita/Desktop/University_Third_Year/AST326/Lab2/AST325_2013/Night1/vega01_dark.txt')
#dark2=np.loadtxt('/Users/anita/Desktop/University_Third_Year/AST326/Lab2/AST325_2013/Night1/Vega02_dark.csv')
#dark3=np.loadtxt('/Users/anita/Desktop/University_Third_Year/AST326/Lab2/AST325_2013/Night1/vega03_dark.csv')

for i in names:
    file="/Users/anita/Desktop/University_Third_Year/AST326/Lab2/AST325_2013/Night1/"+str(i)+".txt"
    #file1="/Users/anita/Desktop/University_Third_Year/AST326/Lab2/AST325_2013/Night1/"+str(i)+"_dark.csv"
    #print "/Users/anita/Desktop/University_Third_Year/AST326/Lab2/AST325_2013/Night1/{0}.csv".format(i)
    #wavelength=np.loadtxt("/Users/anita/Desktop/University_Third_Year/AST326/Lab2/AST325_2013/Night1/{0}.csv".format(i), delimiter=",",usecols=(0,))
    #intensity=np.loadtxt("/Users/anita/Desktop/University_Third_Year/AST326/Lab2/AST325_2013/Night1/{0}.csv", usecols=(1,))
    wavelength=np.loadtxt(file, usecols=(0,))
    #dark=np.loadtxt(file1)
    intensity=np.loadtxt(file, usecols=(1,))
    mean=np.sum(wavelength)/np.size(wavelength)
    sd=np.sqrt(sum((wavelength-mean)**2)/(np.size(wavelength)-1)) 
    gaussian_distribution=(1.0/(sd*(np.sqrt(2*np.pi))))*(np.exp(-0.5*(((wavelength-mean)/sd)**2)))
    #gaussian.append(gaussian_distribution) 
    maximum=np.max(intensity)
    maximum_list.append(maximum)
    plt.figure()
    plt.plot(wavelength,intensity,'r')#,wavelength,gaussian_distribution*(10**7.4),'b')
    #plt.plot(wavelength,gaussian_distribution*(10**256))
    for j in range(len(wavelength)):
        if intensity[j]==maximum:
            print wavelength[j]
    

    #mean=np.sum(intensity/np.size(intensity))
    #sd=np.sqrt(sum((intensity-mean)**2)/(np.size(intensity)-1))
    #mean_list.append(mean)
    #variance.append(sd)
plt.xlabel('pixel number')
plt.ylabel('intensity')
plt.title('intensity vs. wavelength of Vega')
plt.legend(('Vega-1','Vega-2','Vega-3','albero-1','albero-2','Erif-1','Erif-2'),loc='best')
#plt.plot(mean_list,variance,'o')
plt.show()
