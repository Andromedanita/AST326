import numpy as np
import matplotlib.pyplot as plt
import pyfits as pf
import matplotlib.cm as cm

stars='/Users/anita/Documents/University_Third_Year/AST326/Lab5/Lab5_ACAM_DATA/r1599580.fit'
star=pf.getdata(stars)

w=[8072,8073,8074,8075,8076,8077,8078,8079,8080,8081,8082,8083,8084,8085,8086,8087,8088,8089,9966,9967,9968,9969,9970,9971,9972,9973,9974,9975,9976,9977,9978,9979,9980,9981,9982,9983,9984,9985,9986,9987,9988,9989,9990,9991,9992,9993,9994]  # suffixes for  flat files
t=[43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63] # suffixes for bias files

#myarray=np.asarray(t)

bias_array=np.zeros((2501,2148))
means=[]
'''
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
                bias_array.append(bias[i][j])
    print "bias number:", e
temp_bias_array+=temp_bias_array

#temp_bias_array=np.asarray(temp_bias)
#print "bias number is:", e
bias_array=temp_bias_array/len(t)

'''
flat_array=np.zeros((2071,2148))

# computing  flat median
for q in w:
    flatlist='/Users/anita/Documents/University_Third_Year/AST326/Lab5/Lab5_ACAM_DATA/r159'+str(q)+'.fit'
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

#corrected=(star-(702.0))/((master_flat)-(702.0)) # bias subtracted and flat divided star
plt.imshow(bias_array,origin= 'lower',interpolation='nearest')
plt.colorbar() #showing the color bar


plt.show()
