import numpy as np
import matplotlib.pylab as plt

mean_list=[]
sd_list=[]
runs=[2,4,8,16,32,64,128,256,512,1024,2048]
counts=[1,2,3,4,5,6,7,8,9,10]
for j in counts:
    for i in runs:
        file='/Users/anita/Desktop/University_Third_Year/AST326/Data/TASK9pmtrunno_'+str(j)+'sample'+str(i)+'.dat'
        mean=np.sum(x)/np.size(x)                    #the mean
        sd=np.sqrt(sum((x-mean)**2)/(np.size(x)-1))  #standard deviation 
        mean_list.append(mean)
        sd_list.append(sd)
        MOM=sum(mean_list)/np.size(mean_list) #mean of mean
        SDOM= #standard deviation of mean 
plt.plot(x,MOM,'-o')
plt.plot(x,SDOM,'*')
plt.legend(('Mean of Mean','Standard Deviation of Mean'),loc='best')
plt.xlabel('number of samples')
plt.title('Mean of Mean and Standard Deviation of Mean as a function of number of samples')
plt.show()
