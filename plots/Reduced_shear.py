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
rho_0_2 = 248.6; rho_0_3 = 316.1; rho_0_4 = 384.8; rho_0_5 = 485.6; rho_0_6 = 589.3;
rho_0_7 = 706.9; rho_0_8 = 839.1; rho_0_9 = 986.9; rho_1 = 1200;

rhos  = [rho_0_2,rho_0_3,rho_0_4,rho_0_5,rho_0_6,rho_0_7,rho_0_8,rho_0_9,rho_1]
redshifts = ['z = 0.2','z = 0.3','z = 0.4','z = 0.5','z = 0.6','z = 0.7','z = 0.8','z = 0.9','z = 1']
colors = ['blue','red','green','yellow','orange','black','darkorange','darkred','darkblue','darkgreen']
sigmas    =[sig_0_2,sig_0_3,sig_0_4,sig_0_5,sig_0_6,sig_0_7,sig_0_8,sig_0_9,sig_1]


for i in range(len(sigmas)):
	r = np.arange(1.0,99,0.01)
	plt.plot(np.log10(r),1/((r_s*delta_c*rhos[i])*( ((8.*np.arctanh(np.sqrt((1-r/r_s)/(1+r/r_s))))/((r/r_s)**2*np.sqrt(1-(r/r_s)**2))) +\
	               ((4.*(np.log((r/r_s)/2.)))/((r/r_s)**2)) - (2./((r/r_s)**2-1)) + ((4.*np.arctanh(np.sqrt((1-(r/r_s))/(1+(r/r_s)))))/\
	               (((r/r_s)**2-1)*(1-(r/r_s)**2)**0.5))))/((sigmas[i])-(( 2.0*r_s*delta_c*rhos[i] )/( (r/r_s)**2 - 1.0 )*( 1.0 -\
	                2.0/( np.sqrt( 1.0 - (r/r_s)**2 ) )*np.arctanh( np.sqrt( (1.0-(r/r_s))/(1.0+(r/r_s)) ) ) ))), c=colors[i], lw=1.5)
	r = r_s
	plt.plot(np.log10(r),1/((r_s*delta_c*rhos[i])*(10./3.+4.*np.log(0.5)))/(sigmas[i]-2.0*r_s*delta_c*rhos[i]/3.0)) 
	r = np.arange(101,10000,0.01)
	plt.plot(np.log10(r),1/(((r_s*delta_c*rhos[i]))*( ((8.*np.arctan(np.sqrt(((r/r_s)-1)/(1+(r/r_s)))))/((r/r_s)**2*np.sqrt((r/r_s)**2-1))) +\
				   ((4*(np.log((r/r_s)/2.)))/((r/r_s)**2)) - (2./((r/r_s)**2-1.)) + ((4*np.arctan(np.sqrt(((r/r_s)-1)/(1+(r/r_s)))))/(((r/r_s)**2-1)**1.5))))/\
				   (sigmas[i]-( 2.0*r_s*delta_c*rhos[i] )/( (r/r_s)**2 - 1.0 ) *( 1.0 - 2.0/( np.sqrt( (r/r_s)**2 - 1.0 ) )*\
				   np.arctan( np.sqrt( ( (r/r_s)-1.0 )/( 1+(r/r_s) ) ) ) )),\
					label= redshifts[i], c=colors[i], lw=1.5)


#plt.axhline(y=.5, xmin=0., xmax=10.,linewidth=1, color = 'k', linestyle='--')
#plt.xlim(0,1.5)
plt.xlabel(r'$\mathrm{\log R(kpc)}$', fontsize=18) 
plt.ylabel('$\mathrm{g_{NFW}}$', fontsize=18)
#plt.title(r'$\mathrm{Reduced\:Shear}$', fontsize=20)
plt.legend(frameon=False) #plt.legend(frameon=False,bbox_to_anchor=(0.95, 0.2), loc=1, borderaxespad=0.)
plt.savefig("Reduced Shear.png")
plt.show()
