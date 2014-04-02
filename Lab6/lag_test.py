import numpy as np
import matplotlib.pylab as plt


k=(2*(np.pi))/80
l=[]
l1=[]


for a in range(0,500):   # two sine functions
    y=np.sin(k*a)
    y1=np.sin(k*(a+5))
    l.append(y)
    l1.append(y1)

l=np.array(l)
l1=np.array(l1)
a=np.arange(0,500)
l=np.array(l)
l1=np.array(l1)



mean=np.mean(l)
n=np.size(l)
covariance_list=[]
i_list=[]

for i in range(-10,10,1):
    l3=np.roll(l1,i)
    i_list.append(i)
    numbers=[]
    for j in range(0,500,1):
        multiplications=((l[j]*l3[j])-((n/(n-1))*((mean)**2)))
        numbers.append(multiplications)
    sums=np.sum(numbers)
    sums=np.array(sums)
    covariance=((1/n)-1)*sums
    covariance_list.append(covariance)

index=covariance_list.index(min(covariance_list))  # finding the index of the minimum covariance values
print "lag is:", i_list[index]   #printing index of minimum covariance

z=np.fft.ifft((np.fft.fft(l1))*(np.ma.conjugate(l)))
#plt.plot(a,z)
plt.plot(i_list,covariance_list)
plt.plot(i_list[index],(np.min(covariance_list)),'o')
plt.grid()
#plt.plot(a,l)
#plt.plot(a,l1)
plt.show()
