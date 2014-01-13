import numpy as np
import matplotlib.pylab as plt

a=2.766 #semimajor axis(Au)
tau=2454868 #epoch of perihelion(Julian Date)
#t=2456667 #current epoch(Julian Date)
#v= #True anomaly(rad)
w_deg=73.12 #Arguement of perihelion(deg)
w=(w_deg*np.pi)/180 #w in rad
v=np.arange(0,(2*np.pi),0.0037377663933251554)
theta=v+w #Polar angle from the x-axis(rad)
omega_deg=80.72 #Longitude of ascending node(deg)
omega=(omega_deg*np.pi)/180
i_deg=10.61 #inclination(deg)
i=(i_deg*np.pi)/180 #i in rad
e=0.079 #eccentricity
M_sun=2*(10**30) #mass of the Sun (kg)
G=6.67*(10**(-11)) #gravitational constant (SI units)

#k=np.sqrt(G*M_sun)
k=0.017202098950
n=k*(a**(-3./2))
p=(2*(np.pi))/n
t=np.arange(2454702,(2454702+p))

mu=n*(t-tau)

E=np.zeros(len(mu)) #Eccentric anomaly(rad)
E[0]=mu[0]
M=np.zeros(len(mu))
M[0]=E[0]
r=np.zeros(len(mu))



for q in range(1,len(t)):
    M[q-1]=E[q-1]-e*(np.sin(E[q-1]))
    E[q]=E[q-1]+((mu[q-1]-M[q-1])/(1-e*np.cos(E[q-1])))
    

r=a*(1-(e*np.cos(E)))

plt.plot(t,M,'-b',t,E,'r')
plt.legend(('Mean Anomaly','Eccentric Anomaly'),loc='best')
plt.figure()
plt.plot(t,r)
plt.title('position of the asteroid')
plt.xlabel('time(Julian Day)')
plt.ylabel('r(Au)')
plt.show()
