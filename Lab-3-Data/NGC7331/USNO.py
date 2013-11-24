def usno(radeg,decdeg,fovam):
    import urllib as url
    import numpy as np
    import string as str
    
    str1='http://webviz.u-strasbg.fr/viz-bin/asu-tsv/?-source=USNO-B1'
    str2='&-c.ra={0}&-c.dec={1}&-c.bm={2}/{3}&-out.max=unlimited'.format(radeg,decdeg,fovam,fovam)
    str=str1+str2
    f= url.urlopen(str)
    s=f.read()
    f.close()
    
    s1=s.splitlines()
    s1=s1[45:-1] #get rid of header... start fat 45 instead of 37 to remove header completely
    name = np.array([])
    rad= np.array([])
    ded= np.array([])
    rmag=np.array([])
    
    for k in s1:
        kw=k.split('\t')
        name=np.append(name,kw[0])
        rad=np.append(rad,float(kw[1]))
        ded=np.append(ded,float(kw[2]))
        if kw[12] != '     ':
            rmag=np.append(rmag,float(kw[12]))
        else:
            rmag=np.append(rmag,np.nan)
    return  name,rad,ded,rmag

#############
import numpy as np
import matplotlib.pyplot as plt
import pyfits as pf
import urllib as url

fits1='NGC7331-S001-R001-C001-r.fts'
s1=pf.open(fits1)

#read position from the FITS file and convert RA/DEC to degrees
ras=s1[0].header['ra']
des=s1[0].header['dec']
radeg=15*(float(ras[0:2])+float(ras[3:5])/60. + float(ras[6:])/3600.)
dsgn=np.sign(float(des[0:3]))
dedeg=float(des[0:3])+ dsgn*float(des[4:6])/60. +dsgn*float(des[7:])/3600.

fovam=17.0 #size of square search field in arc min
name,rad,ded,rmag = usno(radeg,dedeg,fovam)
w = np.where(rmag<15.)[0] #select only bright stars r<15 mag.

plt.plot(rad[w],ded[w],'g.')
plt.locator_params(axis='x',nbins=4)
plt.locator_params(axis='y',nbins=4)
plt.tick_params('x',pad=10)
plt.xlabel('RA[DEG]')
plt.ylabel('DEC[DEG]')
plt.ticklabel_format(useOffset=False)
plt.axis('scaled')
plt.xlim([339.5,339.1]) #reverse the x-axis direction
plt.show()
