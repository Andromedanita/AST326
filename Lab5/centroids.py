import numpy as np
import matplotlib.pyplot as plt
import pyfits as pf
import matplotlib.cm as cm

stars='/Users/anita/Documents/University_Third_Year/AST326/Lab5/Lab5_ACAM_DATA/r1599580.fit'
star=pf.getdata(stars)


w=[72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89]  # suffixes for  flat files
#t=[43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63] # suffixes for bias files
#t=[1599995,1599996,1599997,1599998,1599999,1600000,1600001,1600002,1600003,1600004,1600005,1600006,1600007,1600008,1600009,1600010,1600011,1600012,1600013,1600014,1600015,1600016,1600017,1600018,1600019,1600020]
w=[72,73]
t=[1599995,1599996]

############## bias ##################
'''
bias_array=np.zeros((2071,2148))

#computing bias median
for e in t:
    biaslist='/Users/anita/Documents/University_Third_Year/AST326/Lab5/Lab5_ACAM_DATA/r'+str(e)+'.fit'
    bias=pf.getdata(biaslist)
    temp_bias=[]
    print bias[1800][1500]
    for i in range(2071):
        for j in range(2148):
            if bias[i][j]>bias[1800][1500]:
                temp_bias.append(bias[i][j])
    bias_array=np.array(temp_bias)
    bias_array+=bias_array
    bias_array_final=bias_array/(np.size(t))
    print "bias number is:", e
'''

bias_array=np.zeros((2071,2148))

for e in t:
    biaslist='/Users/anita/Documents/University_Third_Year/AST326/Lab5/Lab5_ACAM_DATA/r'+str(e)+'.fit'
    bias=pf.getdata(biaslist)
    bias_array+=bias
bias_array_final=bias_array/(np.size(t))


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


corrected=-(star-bias_array_final)/((flat_array)-(bias_array_final))




############### maximas ##########
max_x=np.array([])
max_y=np.array([])
for i in range(1,2070):
    for j in range(1,2147):
        if corrected[i][j]>=corrected[i+1][j] and corrected[i][j]>=corrected[i][j+1]:
            if corrected[i][j]>=corrected[i-1][j] and corrected[i][j]>=corrected[i][j-1]:
                if corrected[i][j]>5000:
                    max_x=np.append(max_x,j)
                    max_y=np.append(max_y,i)
                    print corrected[i][j]
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
            if corrected[y+j][x+i]>10000:
                multix=(x+i)*corrected[y+j][x+i]
                multiy=(y+j)*corrected[y+j][x+i]
                multi_x.append(multix)
                multi_y.append(multiy)
                denominator.append(corrected[y+j][x+i])
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

########### plots ################hb u

plt.imshow(corrected,origin= 'lower',interpolation='nearest')
plt.plot(centroid_x_list,centroid_y_list,'y*')
#plt.xlim(0,2150)
#plt.ylim(0,2090)
#plt.title("Centroid of the star and the sky annulus")

plt.colorbar() #showing the color bar
plt.show()
