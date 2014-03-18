#Plotting the fit files-dark subtracted and with flat

import numpy as np
import matplotlib.pyplot as plt
import pyfits as pf
import matplotlib.cm as cm

centroids_x=[]
centroids_y=[]
multi_x_list=[]
multi_y_list=[]
maxima=[]

fits1='NGC7331-S001-R001-C001-r.fts'
dark='Dark-S001-R003-C003-B2.fts'
flat='combflatr.fits'

x=pf.getdata(fits1)  #NGC7331 data, flipped up/down
y=pf.getdata(dark)   #dark data for NGC7331
z=pf.getdata(flat)   #flat data for NGC7331
g=z/np.median(z)     #flat  so that flat median is equal to zero

x1=np.arange(0,2048)
y1=np.arange(0,2048)


dark_subtracted=x-y  #dark subtracted data

corrected_value=dark_subtracted/g[::-1] #the corrected data
#x.astype('int') #changing the type of data
'''
#finding local maxima points
max_x=np.array([])
max_y=np.array([])
for i in range(1,2047):
    for j in range(1,2047):
        if x[i][j]>=x[i+1][j] and x[i][j]>=x[i][j+1]:
            if x[i][j]>=x[i-1][j] and x[i][j]>=x[i][j-1]:
                if x[i][j]>20000:
                    # plt.plot(j,i,'g.')
                    max_x=np.append(max_x,j)
                    max_y=np.append(max_y,i)
output=np.column_stack((max_x,max_y))
np.savetxt('output.txt',output,fmt='%.1i')                   
'''
max_x=np.loadtxt('output.txt',usecols=(0,))
max_y=np.loadtxt('output.txt',usecols=(1,))
                
#finding centroids of the stars
'''
for i in max_x:
    for j in :
        multi_x=i*corrected_value[i][j]
        multi_x_list.append(multi_x)
        multi_y=j*corrected_value[i][j]
        centroid_x=np.sum(multi_x_list)/np.sum(corrected_value)
        centroid_y=np.sum(multi_y_list)/np.sum(corrected_value)
        centroids_x.append(centroid_x)
        centroids_y.append(centroid_y)
'''
centroid_x_list=[]
centroid_y_list=[]
m=0
while m < len(max_x):
    x=max_x[m]
    y=max_y[m]
    box_x=np.array(-5,+5,1)  #box in x direction
    box_y=np.array(-5,+5,1)  #box in y direction
    for max_x in box_x and max_y in box_y: #to check only the values in the box that are in the 10*10 box
        multi_x=(x*corrected_value) #values of numerator of x centroids
        multi_y=(y*corrected_value) #values of numerator of y centroids
        centroid_x_list.append(multi_x) #appending x centroids
        centroid_y_list.append(multi_y) #appending y centroids
        centroids_x=np.sum(centroid_x_list)/np.sum(corrected_value)   #list of x centroids
        centroids_y=np.sum(centroid_y_list)/np.sum(corrected_value)   #list of y centroids
        
    


#an array of zeros 
#centroids = np.zeros([48,48])
'''
q = 0
while q < np.sqrt(len(centroids_x)):
    if centroids_x !=0 and centroids_y !=0:
        e = centroids_x[q]
        r = centroids_y[q]
        centroids[e][r] = 10000
    q+=1
'''
plt.imshow(corrected_value,cmap=cm.gray_r,vmin=0,vmax=24000,origin= 'lower',interpolation='nearest') #plotting 2-D , vmin=0 sets the lowest value of color bar to zero
plt.plot(max_x,max_y,'g.')
plt.xlim(0,2065)
plt.ylim(0,2065)
plt.colorbar() #showing the color bar
plt.show()
