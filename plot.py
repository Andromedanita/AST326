import numpy as np
import matplotlib.pylab as plt

y=np.loadtxt('my-first-data.txt')
z=np.loadtxt('my-second-data.txt')
w=np.loadtxt('my-third-data.txt')
t=np.loadtxt('my-fourth-data.txt')

#first data set plot
a=plt.plot(y,'r',lw=3)
plt.legend(('1'),loc='upper center')
plt.figure()
#second data set plot
b=plt.plot(z,'b',lw=3)
plt.legend(('2'),loc='upper center')
plt.figure()
#third data set plot
c=plt.plot(w,'g',lw=3)
plt.legend(('3'),loc='upper center')
plt.figure()
#fourth data set plot
d=plt.plot(t,'y',lw=3)
plt.legend(('4'),loc='upper center')

plt.title('Photon counts per sample vs. Time(ms)')
plt.xlabel('Time(ms)')
plt.ylabel('Counts per sample')
plt.figure()

hmin=0
hmax=20
hr=np.arange(hmin,hmax+1,1)

hist=np.zeros(hmax-hmin+1,dtype=np.int)
for i in hr:
    hist[i]=np.where(y==i)[0].size
plt.plot(hr,hist,drawstyle='steps-mid',lw=2,color='red')
plt.figure()
for i in hr:
    hist[i]=np.where(z==i)[0].size
plt.plot(hr,hist,drawstyle='steps-mid',lw=2,color='blue')
plt.figure()
for i in hr:
    hist[i]=np.where(w==i)[0].size
plt.plot(hr,hist,drawstyle='steps-mid',lw=2,color='green')
plt.figure()
for i in hr:
    hist[i]=np.where(t==i)[0].size
plt.plot(hr,hist,drawstyle='steps-mid',lw=2,color='yellow')
    

#hist=np.array([np.where(y==i)[0].size for i in hr])
#plt.plot(hr,hist,drawstyle='step')

#plotting histograms
#n, bins, patches = plt.hist(y, facecolor='green', histtype='step',lw=2)
#plt.figure()
#n, bins, patches = plt.hist(z, facecolor='magenta', histtype='step',lw=2)
#plt.figure()
#n, bins, patches = plt.hist(w, facecolor='red', histtype='step',lw=2)
#plt.figure()
#n, bins, patches = plt.hist(t, facecolor='blue', histtype='step',lw=2)

#plt.title('Histogram Plots')
#plt.xlabel('Count')
#plt.ylabel('Frequency')

#plt.legend(('first data set: (0.001,10)','second data set: (0.001,100)','third data set: (0.01,100)','fourth data set: (0.1,100)'),bbox_to_anchor=(0.77, 0.5))
plt.show()
