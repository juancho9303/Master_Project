import numpy as np
from scipy import integrate
from scipy.integrate import quad
import matplotlib as mpl
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
mpl.rcParams['text.usetex'] = True

c        = 4.46           # concentration parameter (Paper Dutton and Maccio) 
#delta_c  = 6716.38        # Dimensionless overdensity using 4.46
delta_c = (200/3)*(c*c*c)/(np.log(1+c)-c/(1+c))
rho_c    = 197.8            # Critical density in M_sun/kpc^3 (197.8)
r_s      = 100            # Characteristic radius (kpc) 
sigma_c  = 10**8

x1 = np.arange(0.001,0.99,0.0001)
plt.plot(x1*r_s,((r_s*delta_c*rho_c+x1-x1)/(sigma_c))*( ((8*np.arctanh(np.sqrt((1-x1)/(1+x1))))/(x1*x1*np.sqrt(1-x1*x1))) + ((4*(np.log(x1/2)))/(x1*x1)) - ((2)/(x1*x1-1)) + ((4*np.arctanh(np.sqrt((1-x1)/(1+x1))))/((x1*x1-1)*(1-x1*x1)**0.5))))
x2 = 1
plt.plot(x2*r_s,((r_s*delta_c*rho_c+x2-x2)/(sigma_c))*(10/3+4*np.log(0.5)))
x3 = np.arange(1.0001,10,0.0001)
plt.plot(x3*r_s,((r_s*delta_c*rho_c+x3-x3)/(sigma_c))*( ((8*np.arctan(np.sqrt((x3-1)/(1+x3))))/(x3*x3*np.sqrt(x3*x3-1))) + ((4*(np.log(x3/2)))/(x3*x3)) - ((2)/(x3*x3-1)) + ((4*np.arctan(np.sqrt((x3-1)/(1+x3))))/((x3*x3-1)**1.5))))

#plt.yscale('log')
#plt.xscale('log')
plt.xlabel('$R(kpc)$')
plt.ylabel('$\gamma_{NFW}$')
plt.title('Shear dependence on radius')
plt.grid(True)
#plt.legend()
plt.savefig("Shear dependence on radius.png")
plt.show()
