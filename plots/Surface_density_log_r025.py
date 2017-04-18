import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
import pylab as plt
import matplotlib.patches as mpatches
from scipy.integrate import quad
from scipy import integrate
from matplotlib.transforms import BlendedGenericTransform
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
#plt.title(r'$\mathrm{Surface\:Mass\:Density}$',fontsize=20)
plt.subplot(121)
r = np.arange(0.001,99.9,0.01)
plt.plot(np.log10(r),np.log10(( 2.0*r_s*delta_c*rho_c )/( (r/r_s)**2 - 1.0 ) *( 1.0 - 2.0/( np.sqrt( 1.0 - (r/r_s)**2 ) )*np.arctanh( np.sqrt( ( 1.0-r/r_s )/( 1.0 + r/r_s ) ) ) )), c = 'blue', lw = 2)
r = 100
plt.plot(np.log10(r),np.log10(2.0*r_s*delta_c*rho_c/3.0))
r = np.arange(100.01,10000,0.01)
plt.plot(np.log10(r),np.log10(( 2.0*r_s*delta_c*rho_c )/( (r/r_s)**2 - 1.0 ) *( 1.0 - 2.0/( np.sqrt( (r/r_s)**2 - 1.0 ) )*np.arctan( np.sqrt( ( r/r_s - 1.0 )/( 1 + r/r_s ) ) ) )),label=r'$\mathrm{NFW\:profile}$', c = 'blue', lw = 2)

# Mass density profile from M/L ratio and de Vaucouleurs profile:

R = np.arange(0.001,10000,0.001)
plt.plot(np.log10(R),np.log10(4.*I_e*np.exp( -b*( ( R/R_e )**0.25 - 1. ) )),label=r'$\mathrm{Stellar\:Contribution}$', lw = 2)  #4*I(R) where I(R) is de Vaucouleurs
plt.ylabel(r'$\log \Sigma_{NFW}(M_{\odot }/ kpc^{2})$',fontsize=18)
plt.xlabel(r'$\log R(kpc)$',fontsize=18)
plt.legend(frameon=False,bbox_to_anchor=(0.9, 0.25), loc=1, borderaxespad=0.)

plt.subplot(122)
r = np.arange(0.001,99.9,0.01)
plt.plot(r**0.25,np.log10(( 2.0*r_s*delta_c*rho_c )/( (r/r_s)**2 - 1.0 ) *( 1.0 - 2.0/( np.sqrt( 1.0 - (r/r_s)**2 ) )*np.arctanh( np.sqrt( ( 1.0-r/r_s )/( 1.0 + r/r_s ) ) ) )), c = 'blue', lw = 2)
r = 100
plt.plot(r**0.25,np.log10(2.0*r_s*delta_c*rho_c/3.0))
r = np.arange(100.01,10000,0.01)
plt.plot(r**0.25,np.log10(( 2.0*r_s*delta_c*rho_c )/( (r/r_s)**2 - 1.0 ) *( 1.0 - 2.0/( np.sqrt( (r/r_s)**2 - 1.0 ) )*np.arctan( np.sqrt( ( r/r_s - 1.0 )/( 1 + r/r_s ) ) ) )),label=r'$\mathrm{NFW\:profile}$', c = 'blue', lw = 2)

# Mass density profile from M/L ratio and de Vaucouleurs profile:

R = np.arange(0.001,10000,0.001)
plt.plot(R**0.25,np.log10(4.*I_e*np.exp( -b*( ( R/R_e )**0.25 - 1. ) )),label=r'$\mathrm{Stellar\:Contribution}$', lw = 2)  #4*I(R) where I(R) is de Vaucouleurs

plt.xlabel(r'$\mathrm{R^{1/4}(kpc)}$',fontsize=18)
#plt.title(r'$\mathrm{Surface\:Mass\:Density}$',fontsize=20)
#plt.legend(frameon=False,bbox_to_anchor=(0.003, 0.25), loc=1, borderaxespad=0.)
plt.savefig("Surface_mass_density_log.png")
plt.show() 

