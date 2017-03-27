import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
import matplotlib.patches as mpatches
from scipy.integrate import quad
from scipy import integrate
mpl.rcParams['text.usetex'] = True

# This plot is made for the cluster ABELL 1068

c        = 4.46           # concentration parameter (Paper Dutton and Maccio) this was checked many times 
delta_c = (200./3)*(c**3)/(np.log(1+c)-c/(1+c))
rho_c    = 197.8            # Critical density in M_sun/kpc^3 (197.8)
r_s      = 100            # Characteristic radius (pc) 
I_e      = 5.1*10**8     # Effective brightness I(Re) in L_sun per kpc^2
b        = 7.67           # Lokas and Mamon paper
R_e      = 73.7             # Half of the total light in kpc

# Mass density profile from NFW density profile:

x1 = np.arange(0.001,1,0.0001)
plt.plot((x1*r_s)**0.25,np.log10(((2*r_s*delta_c*rho_c)/((x1*x1)-1))*(1-(2)/(np.sqrt(1-(x1*x1)))*np.arctanh(np.sqrt((1-x1)/(1+x1))))))
x2 = 1
plt.plot((x2*r_s)**0.25,np.log10((2*r_s*delta_c*rho_c)/3))
x3 = np.arange(1.0001,100,0.0001)
plt.plot((x3*r_s)**0.25,np.log10(((2*r_s*delta_c*rho_c)/((x3*x3)-1))*(1-(2)/(np.sqrt((x3*x3)-1))*np.arctan(np.sqrt((x3-1)/(1+x3))))),label='NFW profile')

# Mass density profile from M/L ratio and de Vaucouleurs profile:

R = np.arange(0.1,10000,0.001)
plt.plot(R**0.25,np.log10(4.*I_e*np.exp( -b*( ( R/R_e )**0.25 - 1. ) )),label='Stellar Surface Mass')  #4*I(R) where I(R) is de Vaucouleurs

# INTEGRATIONS:

# For the total luminosity:

def surf_bright(r):
	return 2*np.pi*r*I_e*np.exp(-b*(((r)/(R_e))**(0.25)-1))
I1, I1err = quad(surf_bright, 0.1, 10000)

print 'Luminosity: %e' %(I1)

# Projected masses found by integrating the projected surface mass density

def NFW1(x):
	return 2*np.pi*x*((2*r_s*delta_c*rho_c)/((x*x)-1))*(1-(2)/(np.sqrt(1-(x*x)))*np.arctanh(np.sqrt((1-x)/(1+x))))
I2, I2err = quad(NFW1, 0.001, 1)

def NFW2(x):
	return 2*np.pi*x*((2*r_s*delta_c*rho_c)/((x*x)-1))*(1-(2)/(np.sqrt((x*x)-1))*np.arctan(np.sqrt((x-1)/(1+x))))
I3, I3err = quad(NFW2, 1.001, 100)
IT = I2+I3
print 'Dark Matter: %e' %(IT)

#plt.yscale('log')
#plt.xscale('log')
plt.xlabel('$\log R^{1/4}(kpc)$')
plt.ylabel('$\log \Sigma_{NFW}(M_{\odot }/ kpc^{2})$')
plt.title('Surface Mass Density')
plt.grid(True)
plt.legend()
plt.savefig("Surface_mass_density_r025.png")
plt.show()
