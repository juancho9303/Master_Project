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

r = np.arange(0.001,1,0.001)
plt.plot((r*r_s)**0.25,np.log10(((2*r_s*delta_c*rho_c)/((r*r)-1))*(1-(2)/(np.sqrt(1-(r*r)))*np.arctanh(np.sqrt((1-r)/(1+r))))), lw = 2, c = 'blue')
r = 1
plt.plot((r*r_s)**0.25,np.log10((2*r_s*delta_c*rho_c)/3))
r = np.arange(1.0001,100,0.001)
plt.plot((r*r_s)**0.25,np.log10(((2*r_s*delta_c*rho_c)/((r*r)-1))*(1-(2)/(np.sqrt((r*r)-1))*np.arctan(np.sqrt((r-1)/(1+r))))),label=r'$\mathrm{NFW\:profile}$', lw=2, c='blue')

# Mass density profile from M/L ratio and de Vaucouleurs profile:

R = np.arange(0.01,10000,0.001)
plt.plot(R**0.25,np.log10(4.*I_e*np.exp( -b*( ( R/R_e )**0.25 - 1. ) )),label=r'$\mathrm{Stellar\:Surface\:Mass}$', lw=2)  #4*I(R) where I(R) is de Vaucouleurs

plt.xlabel(r'$R^{1/4}(kpc)$',fontsize=18)
plt.ylabel(r'$\log \Sigma_{NFW}(M_{\odot }/ kpc^{2})$',fontsize=18)
plt.title(r'$\mathrm{Surface\:Mass\:Density}$',fontsize=20)
plt.legend(frameon=False,bbox_to_anchor=(0.45, 0.25), loc=1, borderaxespad=0.)
plt.savefig("Surface_mass_density_r025.png")
plt.show()
