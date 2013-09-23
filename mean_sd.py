import numpy as np
import matplotlib.pylab as plt

m=[]    #empty list for mean
s=[]    #empty list for variance
x=np.arange(0,50)        #range for plotting x
lst=[0.01,0.0125,0.025,0.0375,0.05]   #the list of the end of the names of the files (the counts)
for j in lst:
    for i in range(1,7,1):
        file="/Users/anita/Desktop/University_Third_Year/AST326/Data/LONGCOUNTtask7pmtrunno_"+str(i)+"count"+str(j)+".dat"
        x=np.loadtxt(file)                            #loading the data files
        mean=np.sum(x)/np.size(x)                     #the mean
        sd=np.sqrt(sum((x-mean)**2)/(np.size(x)-1))   #standard deviation
        m.append(mean)                                #list of mean values
        s.append(sd**2)                               #list of variance values
        print "The mean value is:", mean,". The standard deviation is:", sd,"\n"
    plt.plot(m,s, '-o')
    plt.title('Variance vs. number of counts')
    #plotting on a log-log scale
    plt.yscale('log')
    plt.xscale('log')
    #y=x line plotting
    plt.plot(x,x)
    plt.xlabel('Mean Values')
    plt.ylabel('Variance')
    #legend of the plots
    plt.legend(('Mean vs. Variance','x=y'), loc='best')
    plt.show()

