import numpy as np
from scipy import integrate
from scipy.integrate import quad
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import gridspec
mpl.rcParams['text.usetex'] = True

c          = 4.46                                      # Concentration parameter (Paper Dutton and Maccio) 
delta_c    = ((200./3)*c**3)/(np.log(1.0+c)-c/(1.0+c)) # Characteristic overdensity of the halo
rho_c      = 220                                       # Critical density in M_sun/kpc^3 (220)
r_s        = 307.1                                     # Characteristic radius (kpc) calculated using M200 of 9.8e15 
n_array    = [] 
R          = np.arange(0.0001, 10000, 1.)

def NFW(r):
	if (r < r_s):
		surf_mass = 2.0*np.pi*r*( ( 2.0*r_s*delta_c*rho_c )/( (r/r_s)**2 - 1.0 ) )*( 1.0 - 2.0/( np.sqrt( 1.0 - (r/r_s)**2 ) )*np.arctanh( np.sqrt( ( 1.0-r/r_s )/( 1.0 + r/r_s ) ) ) )
	elif (r == r_s):
		surf_mass = 2.0*np.pi*r*2.0*r_s*delta_c*rho_c/3.0
	else:
		surf_mass = 2.0*np.pi*r*( ( 2.0*r_s*delta_c*rho_c )/( (r/r_s)**2 - 1.0 ) )*( 1.0 - 2.0/( np.sqrt( (r/r_s)**2 - 1.0 ) )*np.arctan( np.sqrt( ( r/r_s - 1.0 )/( 1 + r/r_s ) ) ) )
	return surf_mass
I2, I2err = quad(NFW, 0.001, 10000)
print 'Dark Matter: %e' %(I2)

def N(val):
  g = lambda y: NFW(y)
  return integrate.quad(g, 0.01, val)[0]
      
for i in range(len(R)):
   n_array.append(np.log10(N(R[i])))

plt.plot(np.log10(R), n_array, '-', c = 'b', label = r'$\mathrm{NFW\:Profile\:Mass}$', lw = 2)
plt.ylabel(r'$\mathrm{\log M_{\odot}}$',fontsize=18)
plt.legend(frameon=False,bbox_to_anchor=(0.95, 0.3), loc=1, borderaxespad=0.)
#plt.savefig("DM_fraction.png")
plt.show()
