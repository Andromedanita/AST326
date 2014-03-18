#Plotting the fit files-dark subtracted and with flat
import numpy as np
import matplotlib.pyplot as plt
import pyfits as pf
import matplotlib.cm as cm
from USNO import *
import math

maxima=[]

fits1='NGC7331-S001-R001-C001-r.fts'
dark='Dark-S001-R003-C003-B2.fts'
flat='combflatr.fits'

x=pf.getdata(fits1)  #NGC7331 data, flipped up/down
y=pf.getdata(dark)   #dark data for NGC7331
z=pf.getdata(flat)   #flat data for NGC7331
g=z/np.median(z)     #flat  so that flat median is equal to zero

dark_subtracted=x-y  #dark subtracted data
corrected_value=dark_subtracted/g [::-1] #the corrected data flipped

max_x=np.loadtxt('output.txt',usecols=(0,))
max_y=np.loadtxt('output.txt',usecols=(1,))


#finding centroids of the stars
centroid_x_list=[]
centroid_y_list=[]

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
            if corrected_value[y+j][x+i]>20000:
                multix=(x+i)*corrected_value[y+j][x+i]
                multiy=(y+j)*corrected_value[y+j][x+i]               
                multi_x.append(multix)
                multi_y.append(multiy)
                denominator.append(corrected_value[y+j][x+i])
    centroids_x=np.sum(multi_x)/np.sum(denominator)
    centroids_y=np.sum(multi_y)/np.sum(denominator)
    centroid_x_list.append(centroids_x)
    centroid_y_list.append(centroids_y)
   
    m+=1

'''
#plt.plot(centroid_x_list, centroid_y_list,'or')

delta=ded[w]*np.pi/180
alpha=rad[w]*np.pi/180
delta_0=dedeg*np.pi/180
alpha_0=radeg*np.pi/180

########################### calculating the X and Y values ###################
# X values
position_x_numerator=-(np.cos(delta))*(np.sin(alpha-alpha_0))
position_x_denominator=(np.cos(delta_0)*np.cos(delta)*np.cos(alpha-alpha_0))+(np.sin(delta)*np.sin(delta_0))
position_x=(-(np.cos(delta))*(np.sin(alpha-alpha_0)))/((np.cos(delta_0)*np.cos(delta)*np.cos(alpha-alpha_0))+(np.sin(delta)*np.sin(delta_0)))


# Y values
position_y_numerator=-((np.sin(delta_0)*np.cos(delta)*np.cos(alpha-alpha_0))-((np.cos(delta_0))*(np.sin(delta))))
position_y_denominator=(np.cos(delta_0)*np.cos(delta)*np.cos(alpha-alpha_0))+(np.sin(delta)*np.sin(delta_0))
position_y=(-((np.sin(delta_0)*np.cos(delta)*np.cos(alpha-alpha_0))-((np.cos(delta_0))*(np.sin(delta)))))/((np.cos(delta_0)*np.cos(delta)*np.cos(alpha-alpha_0))+(np.sin(delta)*np.sin(delta_0)))


f=3454     # focal length(milimeters)
p=0.018    # pixel size(binned) (milimeters)
x_0=1024   # x center
y_0=1024   # y center


################## Pixel positions ################
pos_x=f*position_x/p+x_0   # x values
pos_y=f*position_y/p+y_0   # y values



########## matching the stars ###########
def finding_match (x_catalog,y_catalog,centrox, centroy):
    
    detectedx = np.array([])
    detectedy = np.array([])
    catalogx = np.array([])
    catalogy = np.array([])
    differncex = np.array([])
    differncey = np.array([])
    x = x_catalog
    y = y_catalog
    for a in centroid_x_list : 
        for b in centroid_y_list:
            if math.isnan(centroid_x_list) == 'True':
                centroid_x_list.pop(a)
                for q in range(len(centrox)):
                    x_max = centrox[q]
                    y_max = centroy[q]
                    for i in range(len(x)):
                        dx = (x[i]- x_max)
                        dy = (y[i] - y_max)
                        R = np.sqrt(abs(dx**2)+abs(dy**2))
                    
                        if R < 18:
                            differncex = np.append(differncex,dx)
                            differncey = np.append(differncey,dy)
                            detectedx = np.append(detectedx,x_max)
                            detectedy = np.append(detectedy,y_max)
                            catalogx = np.append(catalogx,x[i])
                            catalogy = np.append(catalogy,y[i])
    return detectedx,detectedy, catalogx, catalogy, differncex, differncey


'''
plt.figure()
#plt.plot(pos_x,pos_y,'r+')
plt.plot(centroid_x_list, centroid_y_list,'g.')
#plt.xlim(0,2020)
#plt.ylim(0,2020)
plt.title('small x and small y and centroids')    



plt.imshow(corrected_value,cmap=cm.gray,vmin=0,vmax=24000,origin= 'lower',interpolation='nearest')

#plt.plot(max_x,max_y,'g.')
#plt.xlim(0,2020)
#plt.ylim(0,2020)
plt.colorbar() #showing the color bar
plt.show()
