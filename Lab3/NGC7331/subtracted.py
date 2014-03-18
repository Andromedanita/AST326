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

x=pf.getdata(fits1)[::-1]  #NGC7331 data, flipped up/down
y=pf.getdata(dark)   #dark data for NGC7331
z=pf.getdata(flat)   #flat data for NGC7331
g=z/np.median(z)     #flat  so that flat median is equal to zero

x1=np.arange(0,2048)
y1=np.arange(0,2048)


dark_subtracted=x-y  #dark subtracted data

corrected_value=dark_subtracted/g #the corrected data
#x.astype('int') #changing the type of data

#finding local maxima points
for i in range(1,2047):
    for j in range(1,2047):
        if x[i][j]>=x[i+1][j] and x[i][j]>=x[i][j+1]:
            if x[i][j]>=x[i-1][j] and x[i][j]>=x[i][j-1]:
                if x[i][j]>20000:
                    plt.plot(j,i,'g.')


                


plt.imshow(corrected_value,cmap=cm.gray_r,vmin=0,origin= 'lower',interpolation='nearest') #plotting 2-D , vmin=0 sets the lowest value of color bar to zero
#plt.imshow(maxima,cmap='gray',vmin=0,origin= 'lower',interpolation='nearest')
#plt.imshow(centroids, cmap=cm.gray_r, vmin= 0 , vmax = 20000, origin='lower' , interpolation='nearest')
plt.colorbar() #showing the color bar
plt.show()
