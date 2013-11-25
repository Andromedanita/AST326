#Plotting the fit files-dark subtracted and with flat

import numpy as np
import matplotlib.pyplot as plt
import pyfits as pf
import matplotlib.cm as cm

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

corrected_value=dark_subtracted/g [::-1] #the corrected data flipped
#x.astype('int') #changing the type of data
'''
#finding local maxima points
max_x=np.array([])
max_y=np.array([])
for i in range(1,2047):
    for j in range(1,2047):
        if x[i][j]>=x[i+1][j] and x[i][j]>=x[i][j+1]:
            if x[i][j]>=x[i-1][j] and x[i][j]>=x[i][j-1]:
                if x[i][j]>10000:
                    # plt.plot(j,i,'g.')
                    max_x=np.append(max_x,j)
                    max_y=np.append(max_y,i)
output=np.column_stack((max_x,max_y))
np.savetxt('output.txt',output,fmt='%.1i') 
 
                 

'''
max_x=np.loadtxt('output.txt',usecols=(0,))
max_y=np.loadtxt('output.txt',usecols=(1,))
                
#finding centroids of the stars
centroid_x_list=[]
centroid_y_list=[]
#avgx_list=[]
#avgy_list=[]
m=0
while m < len(max_x):
    x=max_x[m]
    y=max_y[m]
    box_x=np.arange(-5,5,1)  #box in x direction
    box_y=np.arange(-5,5,1)  #box in y direction
    multi_x=[]   #list of all the x*intensity values
    multi_y=[]   #list of all the y*intensity values
    denominator=[]  #list of  all the sum of intensity values
    for i in box_x:
        for j in box_y:
            if corrected_value[y+j][x+i]>10000:
                multix=(x+i)*corrected_value[y+j][x+i]
                multiy=(y+j)*corrected_value[y+j][x+i]               
                multi_x.append(multix)
                multi_y.append(multiy)
                denominator.append(corrected_value[y+j][x+i])
    centroids_x=np.sum(multi_x)/np.sum(denominator)
    centroids_y=np.sum(multi_y)/np.sum(denominator)
            #avg_x=np.average(max_x)
            #avg_y=np.average(max_y)
            #avgx_list.append(avg_x)
            #avgy_list.append(avg_y)
            #print centroids_x
    centroid_x_list.append(centroids_x)
    centroid_y_list.append(centroids_y)
    #print centroid_x_list, centroid_y_list
    m+=1
plt.plot(centroid_x_list, centroid_y_list,'or')
#plt.plot(avgx_list,avgy_list,'*r')

delta=ded
alpha=rad
delta_0=0.28264999999999674
alpha_0=0.34201400000000604

position_x_numerator=
position_x_denominator=
position_x=position_x_numerator/position_x_denominator
position_y_numerator=((-np.sin(delta_0))*(np.cos(delta))*(np.cos(alpha-alpha_0)))-((np.cos(delta_0))*(np.sin(delta)))
position_y_denominator=((np.cos(delta_0))*(np.cos(delta))*(np.cos(alpha-alpha_0)))+((np.sin(delta))*(np.sin(delta_0)))
position_y=position_y_numerator/position_y_denominator


plt.imshow(corrected_value,cmap=cm.gray_r,vmin=0,vmax=24000,origin= 'lower',interpolation='nearest') #plotting 2-D , vmin=0 sets the lowest value of color bar to zero
plt.plot(max_x,max_y,'g.')
plt.xlim(0,2065)
plt.ylim(0,2065)
plt.colorbar() #showing the color bar
plt.show()
