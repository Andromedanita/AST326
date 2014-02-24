import numpy as np
import matplotlib.pyplot as plt
import pyfits as pf
import matplotlib.cm as cm

stars='/Users/anita/Documents/University_Third_Year/AST326/Lab5/Lab5_ACAM_DATA/r1599580.fit'
star=pf.getdata(stars)


w=[72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89]  # suffixes for  flat files
t=[43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63] # suffixes for bias files



############### maximas ##########
max_x=np.array([])
max_y=np.array([])
for i in range(1,2070):
    for j in range(1,2147):
        if star[i][j]>=star[i+1][j] and star[i][j]>=star[i][j+1]:
            if star[i][j]>=star[i-1][j] and star[i][j]>=star[i][j-1]:
                if star[i][j]>5000:
                    max_x=np.append(max_x,j)
                    max_y=np.append(max_y,i)
                    print star[i][j]
                    #plt.plot(j,i,'g.')
output=np.column_stack((max_x,max_y))
np.savetxt('output.txt',output,fmt='%.1i')


########### centroids #################
theta=np.arange(0,(2.1*(np.pi)),0.1)

centroid_x_list=[]
centroid_y_list=[]

m=0
while m < len(max_x):
    x=max_x[m]
    y=max_y[m]
    box_x=np.arange(-10,10,1)  #box in x direction
    box_y=np.arange(-10,10,1)  #box in y direction
    multi_x=[]   #list of all the x*intensity values
    multi_y=[]   #list of all the y*intensity values
    denominator=[]  #list of  all the sum of intensity values
    for i in box_x:
        for j in box_y:
            if star[y+j][x+i]>10000:
                multix=(x+i)*star[y+j][x+i]
                multiy=(y+j)*star[y+j][x+i]
                multi_x.append(multix)
                multi_y.append(multiy)
                denominator.append(star[y+j][x+i])
    centroids_x=np.sum(multi_x)/np.sum(denominator)
    centroids_y=np.sum(multi_y)/np.sum(denominator)
    centroid_x_list.append(centroids_x)
    centroid_y_list.append(centroids_y)
    circle_x1=centroids_x+(6*(np.cos(theta)))
    circle_y1=centroids_y+(6*(np.sin(theta)))
    plt.plot(circle_x1,circle_y1,'r')
    circle_x2=centroids_x+(11*(np.cos(theta)))
    circle_y2=centroids_y+(11*(np.sin(theta)))
    plt.plot(circle_x2,circle_y2,'g')
    circle_x3=centroids_x+(15*(np.cos(theta)))
    circle_y3=centroids_y+(15*(np.sin(theta)))
    plt.plot(circle_x3,circle_y3,'k')
    m+=1



############## bias ##################
'''
bias_array=np.zeros((2501,2148))
means=[]

t=[43,44]
#computing bias median
for e in t:
    biaslist='/Users/anita/Documents/University_Third_Year/AST326/Lab5/Lab5_ACAM_DATA/r15976'+str(e)+'.fit'
    bias=pf.getdata(biaslist)
    #mean_bias=np.mean(bias)
    temp_bias=[]
    for i in range(2501):
        for j in range(2148):
            if bias[i][j]>bias[1800][1500]:
                temp_bias.append(bias[i][j])
                #mean_bias=np.mean(temp_bias)
                #means.append(mean_bias)
    print "bias number is:", e
bias_array=temp_bias/len(t)

############### flats ###################

flat_array=np.zeros((2071,2148))

# computing  flat median
for q in w:
    flatlist='/Users/anita/Documents/University_Third_Year/AST326/Lab5/Lab5_ACAM_DATA/r15980'+str(q)+'.fit'
    flats=pf.getdata(flatlist)
    #mean_flat=np.mean(flats)
    print flats[1856][1592]
    temp_flat=[]
    for k in range(2071):
        for l in range(2148):
            if flats[k][l]>(flats[1856][1592]):
                temp_flat.append(flats[k][l])
    single_flat= flats/np.median(temp_flat)
    flat_array+=single_flat
flat_array=flat_array/len(w)
'''
#corrected=(star-(702.0))/((master_flat)-(702.0)) # bias subtracted and flat divided star
plt.imshow(star,origin= 'lower',interpolation='nearest')
plt.plot(centroid_x_list,centroid_y_list,'y*')
plt.xlim(0,2150)
plt.ylim(0,2090)
plt.title("Centroid of the star and the sky annulus")
plt.colorbar() #showing the color bar


plt.show()
