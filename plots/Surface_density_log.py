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

r = np.arange(0.001,99.9,0.01)
plt.loglog(r,( 2.0*r_s*delta_c*rho_c )/( (r/r_s)**2 - 1.0 ) *( 1.0 - 2.0/( np.sqrt( 1.0 - (r/r_s)**2 ) )*np.arctanh( np.sqrt( ( 1.0-r/r_s )/( 1.0 + r/r_s ) ) ) ))
r1 = 100
plt.loglog(r1,2.0*r_s*delta_c*rho_c/3.0)
r2 = np.arange(100.01,10000,0.01)
plt.loglog(r2,( 2.0*r_s*delta_c*rho_c )/( (r2/r_s)**2 - 1.0 ) *( 1.0 - 2.0/( np.sqrt( (r2/r_s)**2 - 1.0 ) )*np.arctan( np.sqrt( ( r2/r_s - 1.0 )/( 1 + r2/r_s ) ) ) ),label=r'$\mathrm{NFW\:profile}$')
"""
def NFW(r):
	if (r < r_s):
		surf_mass = 2.0*np.pi*r/r_s*( ( 2.0*r_s*delta_c*rho_c )/( (r/r_s)**2 - 1.0 ) )*( 1.0 - 2.0/( np.sqrt( 1.0 - (r/r_s)**2 ) )*np.arctanh( np.sqrt( ( 1.0-r/r_s )/( 1.0 + r/r_s ) ) ) )
	elif (r == r_s):
		surf_mass = 2.0*r_s*delta_c*rho_c/3.0
	else:
		surf_mass = 2.0*np.pi*r/r_s*( ( 2.0*r_s*delta_c*rho_c )/( (r/r_s)**2 - 1.0 ) )*( 1.0 - 2.0/( np.sqrt( (r/r_s)**2 - 1.0 ) )*np.arctan( np.sqrt( ( r/r_s - 1.0 )/( 1 + r/r_s ) ) ) )
	return surf_mass
"""
# Mass density profile from M/L ratio and de Vaucouleurs profile:

R = np.arange(0.001,10000,0.001)
plt.loglog(R,4.*I_e*np.exp( -b*( ( R/R_e )**0.25 - 1. ) ),label=r'$\mathrm{Stellar\:Surface\:Mass}$')  #4*I(R) where I(R) is de Vaucouleurs

plt.xlabel(r'$\log R(kpc)$',fontsize=18)
plt.ylabel(r'$\log \Sigma_{NFW}(M_{\odot }/ kpc^{2})$',fontsize=18)
plt.title(r'$\mathrm{Surface\:Mass\:Density}$',fontsize=20)
plt.grid(True)
plt.legend()
plt.savefig("Surface_mass_density_log.png")
plt.show() 
