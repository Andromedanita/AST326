#Plotting wavelength vs. pixel number for neon and fluor data sets
import numpy as np
import matplotlib.pylab as plt
from scipy.optimize import leastsq


#mean_list=[]
#variance=[]
names=["Vega01","Vega02","Vega03","albero_01","albero_02","Erif01","Erif02"]
#names=[Vega01,Vega02,Vega03,albero_01,albero_02,Erif01,Erif02]

for i in names:
    file="/Users/anita/Desktop/University_Third_Year/AST326/Lab2/AST325_2013/Night1/"+str(i)+".txt"
    #print "/Users/anita/Desktop/University_Third_Year/AST326/Lab2/AST325_2013/Night1/{0}.csv".format(i)
    #wavelength=np.loadtxt("/Users/anita/Desktop/University_Third_Year/AST326/Lab2/AST325_2013/Night1/{0}.csv".format(i), delimiter=",",usecols=(0,))
    #intensity=np.loadtxt("/Users/anita/Desktop/University_Third_Year/AST326/Lab2/AST325_2013/Night1/{0}.csv", usecols=(1,))
    wavelength=np.loadtxt(file, usecols=(0,))
    intensity=np.loadtxt(file, usecols=(1,))
    plt.figure()
    plt.plot(wavelength,intensity)
    

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
