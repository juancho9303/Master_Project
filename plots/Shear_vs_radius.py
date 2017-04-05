import numpy as np
from scipy import integrate
from scipy.integrate import quad
import matplotlib as mpl
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
mpl.rcParams['text.usetex'] = True

c        = 4.46                                   # Concentration parameter
delta_c = (200./3)*(c**3.)/(np.log(1+c)-c/(1+c))
rho_c    = 197.8                                  # Critical density in M_sun/kpc^3 (197.8)
r_s      = 100                                    # Characteristic radius (kpc) 
sig_0_2 = 9.07e9;  sig_0_3 = 5.2e9; sig_0_4 = 4.29e9;  sig_0_5 = 3.88e9;
sig_0_6 = 3.65e9;  sig_0_7 = 3.5e9; sig_0_8 = 3.39e9;  sig_0_9 = 3.32e9; sig_1   = 3.26e9;

redshifts = ['z = 0.2','z = 0.3','z = 0.4','z = 0.5','z = 0.6','z = 0.7','z = 0.8','z = 0.9','z = 1']
sigmas    =[sig_0_2,sig_0_3,sig_0_4,sig_0_5,sig_0_6,sig_0_7,sig_0_8,sig_0_9,sig_1]
"""
for i in range(len(sigmas)):
	x = np.arange(0.001,0.99,0.0001)
	plt.plot(x*r_s,((r_s*delta_c*rho_c)*( ((8.*np.arctanh(np.sqrt((1-x)/(1+x))))/(x**2*np.sqrt(1-x**2))) +\
	               ((4.*(np.log(x/2.)))/(x**2)) - (2./(x**2-1)) + ((4.*np.arctanh(np.sqrt((1-x)/(1+x))))/\
	               ((x*x-1)*(1-x*x)**0.5))))/((sigmas[i])-(( 2.0*r_s*delta_c*rho_c )/( x**2 - 1.0 )*( 1.0 -\
	                2.0/( np.sqrt( 1.0 - x**2 ) )*np.arctanh( np.sqrt( (1.0-x)/(1.0+x) ) ) ))), c='blue', lw=1.5)
	x = 1
	plt.plot(x*r_s,((r_s*delta_c*rho_c)*(10./3.+4.*np.log(0.5)))/(sigmas[i]-2.0*r_s*delta_c*rho_c/3.0)) 
	x = np.arange(1.0001,10,0.0001)
	plt.plot(x*r_s,(((r_s*delta_c*rho_c))*( ((8.*np.arctan(np.sqrt((x-1)/(1+x))))/(x**2*np.sqrt(x**2-1))) +\
				   ((4*(np.log(x/2.)))/(x**2)) - (2./(x**2-1.)) + ((4*np.arctan(np.sqrt((x-1)/(1+x))))/((x*x-1)**1.5))))/\
				   (sigmas[i]-( 2.0*r_s*delta_c*rho_c )/( x**2 - 1.0 ) *( 1.0 - 2.0/( np.sqrt( x**2 - 1.0 ) )*\
				   np.arctan( np.sqrt( ( x-1.0 )/( 1+x ) ) ) )),\
					label= redshifts[i], c='blue', lw=1.5)
"""

for i in range(len(sigmas)):
	r = np.arange(1.0,99,0.001)
	plt.plot(r,((r_s*delta_c*rho_c)*( ((8.*np.arctanh(np.sqrt((1-r/r_s)/(1+r/r_s))))/((r/r_s)**2*np.sqrt(1-(r/r_s)**2))) +\
	               ((4.*(np.log((r/r_s)/2.)))/((r/r_s)**2)) - (2./((r/r_s)**2-1)) + ((4.*np.arctanh(np.sqrt((1-(r/r_s))/(1+(r/r_s)))))/\
	               (((r/r_s)**2-1)*(1-(r/r_s)**2)**0.5))))/((sigmas[i])-(( 2.0*r_s*delta_c*rho_c )/( (r/r_s)**2 - 1.0 )*( 1.0 -\
	                2.0/( np.sqrt( 1.0 - (r/r_s)**2 ) )*np.arctanh( np.sqrt( (1.0-(r/r_s))/(1.0+(r/r_s)) ) ) ))), c='blue', lw=1.5)
	r = r_s
	plt.plot(r,((r_s*delta_c*rho_c)*(10./3.+4.*np.log(0.5)))/(sigmas[i]-2.0*r_s*delta_c*rho_c/3.0)) 
	r = np.arange(101,10000,0.001)
	plt.plot(r,(((r_s*delta_c*rho_c))*( ((8.*np.arctan(np.sqrt(((r/r_s)-1)/(1+(r/r_s)))))/((r/r_s)**2*np.sqrt((r/r_s)**2-1))) +\
				   ((4*(np.log((r/r_s)/2.)))/((r/r_s)**2)) - (2./((r/r_s)**2-1.)) + ((4*np.arctan(np.sqrt(((r/r_s)-1)/(1+(r/r_s)))))/(((r/r_s)**2-1)**1.5))))/\
				   (sigmas[i]-( 2.0*r_s*delta_c*rho_c )/( (r/r_s)**2 - 1.0 ) *( 1.0 - 2.0/( np.sqrt( (r/r_s)**2 - 1.0 ) )*\
				   np.arctan( np.sqrt( ( (r/r_s)-1.0 )/( 1+(r/r_s) ) ) ) )),\
					label= redshifts[i], c='blue', lw=1.5)


#plt.axhline(y=.5, xmin=0., xmax=10.,linewidth=1, color = 'k', linestyle='--')
#plt.ylim(0,0.05)
plt.xlabel(r'$\mathrm{R(kpc)}$', fontsize=18) 
plt.ylabel('$\mathrm{g_{NFW}}$', fontsize=18)
plt.title(r'$\mathrm{Mean\:Magnification}$', fontsize=20)
plt.legend(frameon=False) #plt.legend(frameon=False,bbox_to_anchor=(0.95, 0.2), loc=1, borderaxespad=0.)
plt.savefig("Mean Magnification.png")
plt.show()
