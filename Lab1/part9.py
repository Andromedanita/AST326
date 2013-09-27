import numpy as np
import matplotlib.pylab as plt
import scipy as sc


main_mean=[]
main_sd=[]


runs=[2,4,8,16,32,64,128,256,512,1024,2048]  #number of samples
counts=[1,2,3,4,5,6,7,8,9,10]          #number of runs
for i in runs:
    mean_list=[]      #list of means
    sd_list=[]        #list of standard deviations
    for j in counts:
        file='/Users/anita/Desktop/University_Third_Year/AST326/Data/TASK9pmtrunno_'+str(j)+'sample'+str(i)+'.dat' #file name
        x=np.loadtxt(file)          #loading the file
        mean=np.sum(x)/np.size(x)   #the mean
        sd=np.sqrt(sum((x-mean)**2)/(np.size(x)-1))  #standard deviation 
        mean_list.append(mean)      #appending mean of each data set for one of the numbers to the meanlist
        sd_list.append(sd)
    MOM= sum(mean_list)/np.size(mean_list)    #mean of mean
    SDOM= np.sqrt(sum((mean_list-MOM)**2)/(np.size(mean_list)-1))    #standard deviation of mean
    main_mean.append(MOM)
    main_sd.append(SDOM)
plt.plot(runs,main_mean,'b')
plt.plot(runs,main_sd,'g')
plt.legend(('Mean of Mean','Standard Deviation of Mean'),loc='best')
plt.xlabel('number of samples')
plt.title('Mean of Mean and Standard Deviation of Mean as a function of number of samples')
plt.show()
