import numpy as np
import matplotlib.pylab as plt
from scipy.optimize import leastsq



for i in range(6):
    file="/Users/anita/Desktop/new_data_1/500ms_SUN_0000"+str(i)+".txt"
    pixel=np.loadtxt(file,usecols=(0,))
    intensity=np.loadtxt(file,usecols=(1,))
    for j in range(6):
        mean=np.sum(pixel)/np.len(pixel)
print mean
