import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
import matplotlib.patches as mpatches
from scipy.integrate import quad
from scipy import integrate
mpl.rcParams['text.usetex'] = True

# This plot is made for the cluster ABELL 1068

c        = 4.46                                      # Concentration parameter (Paper Dutton and Maccio) 
delta_c  = ((200./3)*c**3)/(np.log(1.0+c)-c/(1.0+c)) # Characteristic overdensity of the halo
rho_c    = 197.8                                     # Critical density in M_sun/kpc^3 (197.8)
r_s      = 100                                       # Characteristic radius (kpc) 
I_e      = 10**7                                     # Effective brightness I(Re)
b        = 7.67                                      # Lokas and Mamon paper
R_e      = 73.7                                      # Half of the total light in kpc

# Mass density profile from NFW density profile:

x1 = np.arange(0.001,1,0.001)
plt.plot((x1*r_s)**0.25,np.log10(((2*r_s*delta_c*rho_c)/((x1*x1)-1))*(1-(2)/(np.sqrt(1-(x1*x1)))*np.arctanh(np.sqrt((1-x1)/(1+x1))))))
x2 = 1
plt.plot((x2*r_s)**0.25,np.log10((2*r_s*delta_c*rho_c)/3))
x3 = np.arange(1.0001,100,0.001)
plt.plot((x3*r_s)**0.25,np.log10(((2*r_s*delta_c*rho_c)/((x3*x3)-1))*(1-(2)/(np.sqrt((x3*x3)-1))*np.arctan(np.sqrt((x3-1)/(1+x3))))),label=r'$\mathrm{NFW\:profile}$')

# Mass density profile from M/L ratio and de Vaucouleurs profile:

R = np.arange(0.01,10000,0.001)
plt.plot(R**0.25,np.log10(4.*I_e*np.exp( -b*( ( R/R_e )**0.25 - 1. ) )),label=r'$\mathrm{Stellar\:Surface\:Mass}$')  #4*I(R) where I(R) is de Vaucouleurs

plt.xlabel(r'$R^{1/4}(kpc)$',fontsize=18)
plt.ylabel(r'$\log \Sigma_{NFW}(M_{\odot }/ kpc^{2})$',fontsize=18)
plt.title(r'$\mathrm{Surface\:Mass\:Density}$',fontsize=20)
plt.grid(True)
plt.legend()
plt.savefig("Surface_mass_density_r025.png")
plt.show()
