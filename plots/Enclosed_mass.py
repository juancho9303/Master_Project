import numpy as np
from scipy import integrate
from scipy.integrate import quad
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.rcParams['text.usetex'] = True

c        = 4.46                                      # Concentration parameter (Paper Dutton and Maccio) 
delta_c  = ((200./3)*c**3)/(np.log(1.0+c)-c/(1.0+c)) # Characteristic overdensity of the halo
rho_c    = 212                                     # Critical density in M_sun/kpc^3 (212)
r_s      = 307.1                                       # Characteristic radius (kpc) 
I_e      = 10**7                                     # Effective brightness I(Re)
b        = 7.67                                      # Lokas and Mamon paper
R_e      = 73.7                                      # Half of the total light in kpc
n_array  = [] 
f_array  = []
R        = np.arange(0.0001, 1000, 10.)

# MASS ENCLOSED BY LIGHT (DE VAUCOULEURS PROFILE)

def surf_bright(r):
	return 8.0*np.pi*I_e*np.exp( -b*( ( r/R_e )**0.25 - 1.0 ) )
I1, I1err = quad(surf_bright, 0.01, 1000)
print 'Luminosity: %e' %(I1)
# NOW FOR THE MASS OF THE NFW PROFILE

def NFW(r):
	if (r < r_s):
		surf_mass = 2.0*np.pi*r*( ( 2.0*r_s*delta_c*rho_c )/( (r/r_s)**2 - 1.0 ) )*( 1.0 - 2.0/( np.sqrt( 1.0 - (r/r_s)**2 ) )*np.arctanh( np.sqrt( ( 1.0-r/r_s )/( 1.0 + r/r_s ) ) ) )
	elif (r == r_s):
		surf_mass = 2.0*np.pi*r*2.0*r_s*delta_c*rho_c/3.0
	else:
		surf_mass = 2.0*np.pi*r*( ( 2.0*r_s*delta_c*rho_c )/( (r/r_s)**2 - 1.0 ) )*( 1.0 - 2.0/( np.sqrt( (r/r_s)**2 - 1.0 ) )*np.arctan( np.sqrt( ( r/r_s - 1.0 )/( 1 + r/r_s ) ) ) )
	return surf_mass
I2, I2err = quad(NFW, 0.001, 1000)
print 'Dark Matter: %e' %(I2)
	
def F(val):
  h = lambda x: surf_bright(x)
  return integrate.quad(h, 0.001, val)[0]

def N(val):
  g = lambda y: NFW(y)
  return integrate.quad(g, 0.001, val)[0]
      
for i in range(len(R)):
   f_array.append(np.log10(F(R[i])))
   n_array.append(np.log10(N(R[i])))
    
plt.plot(np.log10(R), f_array, '-', c = 'r', label = r'$\mathrm{Stellar\:Mass}$', lw = 2)
plt.plot(np.log10(R), n_array, '-', c = 'b', label = r'$\mathrm{NFW\:Profile\:Mass}$', lw = 2)
plt.xlabel(r'$\log R(kpc)$',fontsize=18)
plt.ylabel(r'$\log M_{\odot }$',fontsize=18)
plt.title(r'$\mathrm{Enclosed\:Mass}$',fontsize=20)
#plt.grid(True)
plt.legend(frameon=False,bbox_to_anchor=(0.95, 0.2), loc=1, borderaxespad=0.)
plt.savefig("Enclosed Mass.png")
plt.show()
plt.show()      
