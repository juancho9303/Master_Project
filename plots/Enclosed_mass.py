import numpy as np
from scipy import integrate
from scipy.integrate import quad
import seaborn
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.rcParams['text.usetex'] = True

c        = 4.46                                      # Concentration parameter (Paper Dutton and Maccio) 
delta_c  = ((200./3)*c**3)/(np.log(1.0+c)-c/(1.0+c)) # Characteristic overdensity of the halo
rho_c    = 212                                       # Critical density in M_sun/kpc^3 (212)
r_s      = 307.1                                     # Characteristic radius (kpc) 
I_e      = 10**7                                     # Effective brightness I(Re)
b        = 7.67                                      # Lokas and Mamon paper
R_e      = 73.7                                      # Half of the total light in kpc
n_array     = []; n_array_plus  = []; n_array_minus   = []; f_array1    = []
fractionDM1 = []; f_array2      = []; fractionDM2     = []; f_array3    = []; fractionDM3 = []
R           = np.arange(0.0001, 100, 0.1)

# MASS ENCLOSED BY LIGHT (SALPETER)
def surf_bright1(r):
	return 8.0*np.pi*r*I_e*np.exp( -b*( ( r/R_e )**0.25 - 1.0 ) )
I1, I1err = quad(surf_bright1, 0.001, 1000)
print 'Luminosity: %e' %(I1)

# MASS ENCLOSED BY LIGHT (KROUPA)
def surf_bright2(r):
	return 5.2*np.pi*r*I_e*np.exp( -b*( ( r/R_e )**0.25 - 1.0 ) )
I3, I3err = quad(surf_bright2, 0.001, 1000)
print 'Luminosity: %e' %(I3)

# MASS ENCLOSED BY LIGHT (CHABRIER)
def surf_bright3(r):
	return 5.04*np.pi*r*I_e*np.exp( -b*( ( r/R_e )**0.25 - 1.0 ) )
I4, I4err = quad(surf_bright3, 0.001, 1000)
print 'Luminosity: %e' %(I4)

def F1(val):
  h = lambda x: surf_bright1(x)
  return integrate.quad(h, 0.01, val)[0]
  
def F2(val):
  h = lambda x: surf_bright2(x)
  return integrate.quad(h, 0.01, val)[0]
  
def F3(val):
  h = lambda x: surf_bright3(x)
  return integrate.quad(h, 0.01, val)[0]
   
for i in range(len(R)):
   f_array1.append((F1(R[i])))
   f_array2.append((F2(R[i])))
   f_array3.append((F3(R[i])))

plt.xlim( 0.1, 100.0 )
plt.loglog((R), (f_array1), '-.', c='darkorange', label = r'$\mathrm{Salpeter}$', lw = 2)
plt.loglog((R), (f_array2), '--', c='darkred', label = r'$\mathrm{Kroupa}$', lw = 2)
plt.loglog((R), (f_array3), '-.', c='darkgreen', label = r'$\mathrm{Chabrier}$', lw = 2)
plt.xlabel(r'$\mathrm{r(kpc)}$',fontsize=18)
plt.ylabel(r'$\mathrm{M(r)}/\mathrm{M}_{\odot }$',fontsize=18)
#plt.title(r'$\mathrm{Enclosed\:Mass\:for\:different\:IMFs}$',fontsize=20)
plt.legend(frameon=False,bbox_to_anchor=(0.95, 0.3), loc=1, borderaxespad=0.)
plt.savefig("Enclosed_Mass_IMFs.png")
plt.show()
plt.show()      
