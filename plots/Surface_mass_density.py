import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
import matplotlib.patches as mpatches
from scipy.integrate import quad
from scipy import integrate
mpl.rcParams['text.usetex'] = True

# This plot is made for the cluster ABELL 1068

c        = 4.46           # concentration parameter (Paper Dutton and Maccio) this was checked many times 
delta_c  = 6716.38        # Dimensionless overdensity using 4.46
rho_c    = 200            # Critical density in M_sun/kpc^3 (197.8)
r_s      = 100            # Characteristic radius (kpc) 
I_e      = 2.6*10**9      # Effective brightness I(Re) 2.6e6
b        = 7.67           # Lokas and Mamon paper
R_e      = 20             # Half of the total light in kpc

# Mass density profile from NFW density profile:

x1 = np.arange(0.001,1,0.0001)
plt.plot(x1*r_s,((2*r_s*delta_c*rho_c)/((x1*x1)-1))*(1-(2)/(np.sqrt(1-(x1*x1)))*np.arctanh(np.sqrt((1-x1)/(1+x1)))))
x2 = 1
plt.plot(x2*r_s,(2*r_s*delta_c*rho_c)/3)
x3 = np.arange(1.0001,100,0.0001)
plt.plot(x3*r_s,((2*r_s*delta_c*rho_c)/((x3*x3)-1))*(1-(2)/(np.sqrt((x3*x3)-1))*np.arctan(np.sqrt((x3-1)/(1+x3)))),label='NFW profile')

# Mass density profile from M/L ratio and de Vaucouleurs profile:

R = np.arange(0.1,10000,0.001)
plt.plot(R,4*I_e*np.exp(-b*(((R)/(R_e))**(0.25)-1)),label='Stellar Surface Mass')  #4*I(R) where I(R) is de Vaucouleurs

# INTEGRATIONS:

# For the total luminosity:

def surf_bright(r, I_e, b, R_e):
	return 4*I_e*np.exp(-b*(((r)/(R_e))**(0.25)-1))
I1, I1err = quad(surf_bright, 0.1, 10000, args=(I_e,b,R_e))
#r = np.arange(0.1,10,0.001)

print 'Luminosity: %e' %(I1)

# Projected masses found by integrating the projected surface mass density

def NFW1(x1, delta_c, r_s, rho_c):
	return 2*np.pi*x1*((2*r_s*delta_c*rho_c)/((x1*x1)-1))*(1-(2)/(np.sqrt(1-(x1*x1)))*np.arctanh(np.sqrt((1-x1)/(1+x1))))
I2, I2err = quad(NFW1, 0.001, 1, args=(delta_c, r_s, rho_c))

def NFW2(x3, delta_c, r_s, rho_c):
	return 2*np.pi*x3*((2*r_s*delta_c*rho_c)/((x3*x3)-1))*(1-(2)/(np.sqrt((x3*x3)-1))*np.arctan(np.sqrt((x3-1)/(1+x3))))
I3, I3err = quad(NFW2, 1.001, 100, args=(delta_c, r_s, rho_c))
IT = I2+I3
print 'Dark Matter: %e' %(IT)

plt.yscale('log')
plt.xscale('log')
plt.xlabel('$R(kpc)$')
plt.ylabel('$\Sigma_{NFW}(M_{\odot }/ kpc^{2})$')
plt.title('Surface Mass Density')
plt.grid(True)
plt.legend()
plt.savefig("Surface_mass_density_full.png")
plt.show()
