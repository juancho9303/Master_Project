import numpy as np
from scipy import integrate
from scipy.integrate import quad
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import gridspec
mpl.rcParams['text.usetex'] = True
from operator import truediv

c          = 4.46                                      # Concentration parameter (Paper Dutton and Maccio) 
delta_c    = ((200./3)*c**3)/(np.log(1.0+c)-c/(1.0+c)) # Characteristic overdensity of the halo
rho_c      = 212                                       # Critical density in M_sun/kpc^3 (212)
r_s        = 307.1                                     # Characteristic radius (kpc) calculated using M200 of 9.8e15 
I_e        = 10**7                                     # Effective brightness I(Re)
b          = 7.67                                      # Lokas and Mamon paper
R_e        = 73.7                                      # Half of the total light in kpc
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

# NFW MASS PROFILE
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
	
def F1(val):
  h = lambda x: surf_bright1(x)
  return integrate.quad(h, 0.01, val)[0]
  
def F2(val):
  h = lambda x: surf_bright2(x)
  return integrate.quad(h, 0.01, val)[0]
  
def F3(val):
  h = lambda x: surf_bright3(x)
  return integrate.quad(h, 0.01, val)[0]

def N(val):
  g = lambda y: NFW(y)
  return integrate.quad(g, 0.01, val)[0]
     
for i in range(len(R)):
   f_array1.append(np.log10(F1(R[i])))
   f_array2.append(np.log10(F2(R[i])))
   f_array3.append(np.log10(F3(R[i])))
   n_array.append(np.log10(N(R[i])))
   n_array_plus.append(np.log10(1.3*N(R[i]))) 
   n_array_minus.append(np.log10(0.7*N(R[i])))
   fractionDM1.append( 10**((n_array[i])-(f_array1[i])) ) 
   fractionDM2.append( 10**((n_array[i])-(f_array2[i])) ) 
   fractionDM3.append( 10**((n_array[i])-(f_array3[i])) ) 

#pepito = map(truediv,n_array,f_array1)
  
fig = plt.figure()
gs = gridspec.GridSpec(2, 1, height_ratios=[2, 1]) 

ax0 = plt.subplot(gs[0])
line0, = ax0.plot((R), (f_array1), '-.', c='darkorange', label = r'$\mathrm{Salpeter}$', lw = 2)
line0, = ax0.plot((R), (f_array2), '--', c='darkred', label = r'$\mathrm{Kroupa}$', lw = 2)
line0, = ax0.plot((R), (f_array3), '-.', c='darkgreen', label = r'$\mathrm{Chabrier}$', lw = 2)
line0, = ax0.plot((R), (n_array), '-', c='black', label = r'$\mathrm{NFW\:Mass\:Profile}$', lw = 2)
plt.fill_between(R, n_array_minus, n_array_plus, alpha=0.2)
plt.ylabel(r'$\mathrm{\log M_{\odot}}$',fontsize=18)
plt.legend(frameon=False,bbox_to_anchor=(0.95, 0.45), loc=1, borderaxespad=0.,prop={'size':13})

ax1 = plt.subplot(gs[1], sharex = ax0)
plt.xscale('log')
plt.yscale('log')
line1, = ax1.plot((R), (fractionDM1), '-.', c='darkorange', label = r'$\mathrm{M_{DM}/M_{\star}\:Salpeter}$', lw = 2)
line1, = ax1.plot((R), (fractionDM2), '--', c='darkred', label = r'$\mathrm{M_{DM}/M_{\star}\:Kroupa}$', lw = 2)
line1, = ax1.plot((R), (fractionDM3), ':', c='darkgreen', label = r'$\mathrm{M_{DM}/M_{\star}\:Chabrier}$', lw = 2)
plt.xlabel(r'$\mathrm{R(kpc)}$',fontsize=18)
plt.ylabel(r'$\mathrm{Ratio}$',fontsize=18)
plt.legend(frameon=False,bbox_to_anchor=(0.35, 0.95), loc=1, borderaxespad=0.,prop={'size':12})

plt.setp(ax0.get_xticklabels(), visible=False)
yticks = ax1.yaxis.get_major_ticks()
yticks[-2].label1.set_visible(False)

plt.axhline(1.0, c = 'black', linestyle='--')

plt.subplots_adjust(hspace=.0)
plt.savefig("DM_fraction_all_IMFs.png")
plt.show()
