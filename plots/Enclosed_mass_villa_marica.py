import numpy as np
from scipy import integrate
import matplotlib as mpl
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
mpl.rcParams['text.usetex'] = True

c        = 4.46                                   # concentration parameter (Paper Dutton and Maccio) this was checked many times 
delta_c  = ( (200./3)*c**3 )/( np.log( 1.0 + c) - c/( 1.0 + c ) )
rho_c    = 197.8                                  # Critical density in M_sun/kpc^3 (197.8)
r_s      = 100                                    # Characteristic radius (kpc) 
I_e      = 5.1e7                          # Effective brightness I(Re) 2.6e6
b        = 7.67                                   # Lokas and Mamon paper
R_e      = 73.7                                   # Half of the total light in kpc

#MASS ENCLOSED BY LIGHT (DE VAUCOULEURS PROFILE)

def surf_bright(r):
	return 8.0*np.pi*I_e*np.exp( -b*( ( r/R_e )**0.25 - 1.0 ) )

#NOW FOR THE MASS OF THE NFW PROFILE

def NFW(x):
	if (x < 1.0):
		surf_mass = 2.0*np.pi*x*( ( 2.0*r_s*delta_c*rho_c )/( x**2 - 1.0 ) )*( 1.0 - 2.0/( np.sqrt( 1.0 - x**2 ) )*np.arctanh( np.sqrt( ( 1.0-x )/( 1.0 + x ) ) ) )
	elif (x == 1.0):
		surf_mass = 2.0*r_s*delta_c*rho_c/3.0
	else:
		surf_mass = 2.0*np.pi*x*( ( 2.0*r_s*delta_c*rho_c )/( x**2 - 1.0 ) )*( 1.0 - 2.0/( np.sqrt( x**2 - 1.0 ) )*np.arctan( np.sqrt( ( x - 1.0 )/( 1 + x ) ) ) )
	return surf_mass
  
R = np.arange(0.1, 10000, 10)

def F(val):
  h = lambda x: surf_bright(x)
  return integrate.quad(h, 0.1, val)[0]

def N(val):
  g = lambda y: NFW(y)
  return integrate.quad(g, 0.1, val)[0]
      
for i in range(len(R)):
  plt.plot(np.log10(R[i]), np.log10(F(R[i])), '.', c = 'r')
  plt.plot(np.log10(R[i]), np.log10(N(R[i])), '.', c = 'b')
plt.show()      
	
#plt.yscale('log')
#plt.xscale('log')
#plt.xlabel('$R(kpc)$')
#plt.ylabel('$M_{\odot }$')
#plt.title('Enclosed Mass')
#plt.grid(True)
#plt.legend()
#plt.savefig("Enclosed Mass.png")
#plt.show()

