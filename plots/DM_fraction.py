import numpy as np
from scipy import integrate
from scipy.integrate import quad
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import gridspec
mpl.rcParams['text.usetex'] = True

c        = 4.46                                      # Concentration parameter (Paper Dutton and Maccio) 
delta_c  = ((200./3)*c**3)/(np.log(1.0+c)-c/(1.0+c)) # Characteristic overdensity of the halo
rho_c    = 197.8                                     # Critical density in M_sun/kpc^3 (197.8)
r_s      = 100                                       # Characteristic radius (kpc) 
I_e      = 10**7                                     # Effective brightness I(Re)
b        = 7.67                                      # Lokas and Mamon paper
R_e      = 73.7                                      # Half of the total light in kpc
n_array  = [] 
f_array  = []
fractionDM = []
R        = np.arange(0.01, 10000, 10.)

# MASS ENCLOSED BY LIGHT (DE VAUCOULEURS PROFILE)

def surf_bright(r):
	return 8.0*np.pi*I_e*np.exp( -b*( ( r/R_e )**0.25 - 1.0 ) )
I1, I1err = quad(surf_bright, 0.1, 10000)
print 'Luminosity: %e' %(I1)
# NOW FOR THE MASS OF THE NFW PROFILE

def NFW(r):
	if (r < r_s):
		surf_mass = 2.0*np.pi*r/r_s*( ( 2.0*r_s*delta_c*rho_c )/( (r/r_s)**2 - 1.0 ) )*( 1.0 - 2.0/( np.sqrt( 1.0 - (r/r_s)**2 ) )*np.arctanh( np.sqrt( ( 1.0-r/r_s )/( 1.0 + r/r_s ) ) ) )
	elif (r == r_s):
		surf_mass = 2.0*r_s*delta_c*rho_c/3.0
	else:
		surf_mass = 2.0*np.pi*r/r_s*( ( 2.0*r_s*delta_c*rho_c )/( (r/r_s)**2 - 1.0 ) )*( 1.0 - 2.0/( np.sqrt( (r/r_s)**2 - 1.0 ) )*np.arctan( np.sqrt( ( r/r_s - 1.0 )/( 1 + r/r_s ) ) ) )
	return surf_mass
I2, I2err = quad(NFW, 0.01, 10000)
print 'Dark Matter: %e' %(I2)
	
def F(val):
  h = lambda x: surf_bright(x)
  return integrate.quad(h, 0.1, val)[0]

def N(val):
  g = lambda y: NFW(y)
  return integrate.quad(g, 0.1, val)[0]
      
for i in range(len(R)):
   f_array.append(np.log10(F(R[i])))
   n_array.append(np.log10(N(R[i])))
   fractionDM.append( n_array[i]/f_array[i] )  

fig = plt.figure()
gs = gridspec.GridSpec(2, 1, height_ratios=[2, 1]) 

# the fisrt subplot
ax0 = plt.subplot(gs[0])
#line0, = ax0.plot(np.log10(R), f_array, color='r')
line0, = ax0.plot(np.log10(R), f_array, '-', c = 'r', label = r'$\mathrm{Stellar\:Mass}$', lw = 2)
line0, = ax0.plot(np.log10(R), n_array, '-', c = 'b', label = r'$\mathrm{NFW\:Profile\:Mass}$', lw = 2)
plt.ylabel(r'$\mathrm{\log M_{\odot}}$',fontsize=18)
plt.legend(frameon=False,bbox_to_anchor=(0.95, 0.3), loc=1, borderaxespad=0.)

#the second subplot
# shared axis X
ax1 = plt.subplot(gs[1], sharex = ax0)
line1, = ax1.plot(np.log10(R), fractionDM, '-', c = 'g', label = r'$\mathrm{M_{DM}/M_{star}}$', lw = 2)
plt.xlabel(r'$\log R(kpc)$',fontsize=18)
plt.ylabel(r'$\mathrm{Ratio}$',fontsize=18)
plt.legend(frameon=False,bbox_to_anchor=(0.95, 0.35), loc=1, borderaxespad=0.)

plt.setp(ax0.get_xticklabels(), visible=False)
# remove last tick label for the second subplot
yticks = ax1.yaxis.get_major_ticks()
yticks[-2].label1.set_visible(False)

# remove vertical gap between subplots
plt.subplots_adjust(hspace=.0)
plt.savefig("DM_fraction.png")
plt.show()
