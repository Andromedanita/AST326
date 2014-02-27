import numpy as np
import matplotlib.pyplot as plt
import pyfits as pf
import matplotlib.cm as cm

stars='/Users/anita/Documents/University_Third_Year/AST326/Lab5/Lab5_ACAM_DATA/r1599580.fit'
star=pf.getdata(stars)


w=[72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89]  # suffixes for  flat files
t=[1599995,1599996,1599997,1599998,1599999,1600000,1600001,1600002,1600003,1600004,1600005,1600006,1600007,1600008,1600009,1600010,1600011,1600012,1600013,1600014,1600015,1600016,1600017,1600018,1600019,1600020]
'''
############## bias ##################
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
'''
bias_array=np.zeros((2071,2148))

for e in t:
    biaslist='/Users/anita/Documents/University_Third_Year/AST326/Lab5/Lab5_ACAM_DATA/r'+str(e)+'.fit'
    bias=pf.getdata(biaslist)
    bias_array+=bias
bias_array_final=bias_array/(np.size(t))
pf.writeto('bias.fit',bias_array_final)

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

pf.writeto('flat.fit',flat_array)
'''
bias1='/Users/anita/Documents/University_Third_Year/AST326/Lab5/bias.fit'
bias_array_final=pf.getdata(bias1)

flat1='/Users/anita/Documents/University_Third_Year/AST326/Lab5/flat.fit'
flat_array=pf.getdata(flat1)

corrected=(star-bias_array_final)/((flat_array))

'''
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

flux_list=[]
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
    #final_centroids=np.column_stack((centroid_x_list,centroid_y_list))
    #np.savetxt('centroids.txt',final_centroids)
    m+=1
'''

########## calculation of flux of each star #########
p_list=[]
l_list=[]

distances=[]
temp_flux=np.zeros(35)
temp_background=[]
temp_flux=[]
centroid_x_list=np.loadtxt('/Users/anita/Documents/University_Third_Year/AST326/Lab5/cent.txt',usecols=(0,))
centroid_y_list=np.loadtxt('/Users/anita/Documents/University_Third_Year/AST326/Lab5/cent.txt',usecols=(1,))
#predicted_radius=np.arange(0,15,1.756224351806862e-05)
#predicted_radius=0
i =0
while i < 35:
    r =centroid_x_list[i]
    u =centroid_y_list[i]
    box_x=np.arange(-26,26,1)  #box in x direction
    box_y=np.arange(-26,26,1)  #box in y direction
    #temp_flux=[]
    #temp_flux=np.zeros(35)
    total_flux=[]
    flux_list=[]
    background_list=[]
    for l in (box_x+r):
        for p in (box_y+u):
            distance=np.sqrt(((l-r)**2)+((p-u)**2)) #distance between centroid and the points in the box
            distances.append(distance)
            print "distance is:", distance
            if distance <15:
                flux_list.append(corrected[l][p]) #appends the flux of the point if inside radius 15
            elif distance<25 and distance>22:
                background_list.append(corrected[l][p])  #appends the background if inside annulus(22<r<25)
    flux_sum=np.sum(flux_list)
    temp_flux.append(flux_sum)
    #temp_flux[i] = total_flux
    background_avg=np.mean(background_list)
    temp_background.append(background_avg)
    i+=1



#circle_x1=centroids_x+(10*(np.cos(theta)))
#   circle_y1=centroids_y+(10*(np.sin(theta)))
#   plt.plot(circle_x1,circle_y1,'r')
#   circle_x2=centroids_x+(15*(np.cos(theta)))
#   circle_y2=centroids_y+(15*(np.sin(theta)))
#   plt.plot(circle_x2,circle_y2,'g')
#   circle_x3=centroids_x+(20*(np.cos(theta)))
#   circle_y3=centroids_y+(20*(np.sin(theta)))
#   plt.plot(circle_x3,circle_y3,'k')
# m+=1

'''
##### growth curve ######

flux_list=[]
distances=[]
for l in range(0,2071):     #to only consider a box around the stars
    for p in range(0,2148):
        distance=np.sqrt(((l-410.54895642)**2)+((p-127.45104358)**2)) #distance between centroid and the points in the box
        distances.append(distance)
        print "distance is:", distance
        for predicted_radius in range(0,15):
            if distance <predicted_radius:
                flux_list.append(corrected[l][p]) #appends the flux of the point if inside radius 15
            plt.plot(predicted_radius,flux_list)

'''

#############  noise  ###########
q=np.array(temp_background)
r1=15
r2=22
r3=25
readout_noise=6.0/1.9
N1=(np.pi)*(r1**2)
N23=(np.pi)*((r3**2)-(r2**2))
B=q/(np.size(temp_background))
poisson_noise=np.std(temp_flux)
total_noise=(poisson_noise)+(N1*(B+(readout_noise**2)))+((N1*(B+(readout_noise**2)))/N23)
signal_to_noise=poisson_noise/(np.sqrt(total_noise))


########### plots ################
'''
plt.imshow(corrected,origin= 'lower',interpolation='nearest')
plt.plot(centroid_x_list,centroid_y_list,'y*')
plt.xlim(0,2150)
plt.ylim(0,2090)
plt.title("Centroid of the star and the sky annulus")
plt.colorbar() #showing the color bar
'''
plt.show()
