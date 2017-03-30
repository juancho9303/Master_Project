import numpy as np
from scipy import integrate
from scipy.integrate import quad
import matplotlib as mpl
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
mpl.rcParams['text.usetex'] = True

c        = 4.46                                   # concentration parameter (Paper Dutton and Maccio)
delta_c = (200./3)*(c**3)/(np.log(1+c)-c/(1+c))
rho_c    = 197.8                                  # Critical density in M_sun/kpc^3 (197.8)
r_s      = 100                                    # Characteristic radius (kpc) 
#sigma_c  = 4.76*10**8                            # Critical surface mass density
sigma_c  = 10**8                                  # Critical surface mass density for z=1
sigma_c2 = 5.4*10**7                              # Critical surface mass density for z=1.5     
sigma_c3 = 2*10**7                                # Critical surface mass density for z=2

x = np.arange(0.001,0.99,0.0001)
plt.plot(x*r_s,((r_s*delta_c*rho_c)/(sigma_c))*( ((8.*np.arctanh(np.sqrt((1-x)/(1+x))))/(x*x*np.sqrt(1-x*x))) + ((4*(np.log(x/2)))/(x*x)) - (2/(x*x-1)) + ((4*np.arctanh(np.sqrt((1-x)/(1+x))))/((x*x-1)*(1-x*x)**0.5))), c='blue', lw=1.5)
x = 1
plt.plot(x*r_s,((r_s*delta_c*rho_c)/(sigma_c))*(10./3.+4.*np.log(0.5)))
x = np.arange(1.0001,10,0.0001)
plt.plot(x*r_s,((r_s*delta_c*rho_c)/(sigma_c))*( ((8.*np.arctan(np.sqrt((x-1)/(1+x))))/(x*x*np.sqrt(x*x-1))) + ((4*(np.log(x/2)))/(x*x)) - (2/(x*x-1)) + ((4*np.arctan(np.sqrt((x-1)/(1+x))))/((x*x-1)**1.5))), label='$\mathrm{z = 1}$', c='blue', lw=1.5)

x = np.arange(0.001,0.99,0.0001)
plt.plot(x*r_s,((r_s*delta_c*rho_c)/(sigma_c2))*( ((8.*np.arctanh(np.sqrt((1-x)/(1+x))))/(x*x*np.sqrt(1-x*x))) + ((4*(np.log(x/2)))/(x*x)) - (2/(x*x-1)) + ((4*np.arctanh(np.sqrt((1-x)/(1+x))))/((x*x-1)*(1-x*x)**0.5))), c='red', lw=1.5)
x = np.arange(1.0001,10,0.0001)
plt.plot(x*r_s,((r_s*delta_c*rho_c)/(sigma_c2))*( ((8.*np.arctan(np.sqrt((x-1)/(1+x))))/(x*x*np.sqrt(x*x-1))) + ((4*(np.log(x/2)))/(x*x)) - (2/(x*x-1)) + ((4*np.arctan(np.sqrt((x-1)/(1+x))))/((x*x-1)**1.5))), label='$\mathrm{z = 1.5}$', c='red', lw=1.5)

x = np.arange(0.001,0.99,0.0001)
plt.plot(x*r_s,((r_s*delta_c*rho_c)/(sigma_c3))*( ((8.*np.arctanh(np.sqrt((1-x)/(1+x))))/(x*x*np.sqrt(1-x*x))) + ((4*(np.log(x/2)))/(x*x)) - (2/(x*x-1)) + ((4*np.arctanh(np.sqrt((1-x)/(1+x))))/((x*x-1)*(1-x*x)**0.5))), c='green', lw=1.5)
x = np.arange(1.0001,10,0.0001)
plt.plot(x*r_s,((r_s*delta_c*rho_c)/(sigma_c3))*( ((8.*np.arctan(np.sqrt((x-1)/(1+x))))/(x*x*np.sqrt(x*x-1))) + ((4*(np.log(x/2)))/(x*x)) - (2/(x*x-1)) + ((4*np.arctan(np.sqrt((x-1)/(1+x))))/((x*x-1)**1.5))), label='$\mathrm{z = 2}$', c='green', lw=1.5)

plt.axhline(y=.5, xmin=0., xmax=10.,linewidth=1, color = 'k', linestyle='--')

plt.ylim(0,3)
plt.xlabel(r'$\mathrm{R(kpc)}$', fontsize=18) 
plt.ylabel('$\mathrm{\gamma_{NFW}}$', fontsize=18)
plt.title(r'$\mathrm{Shear\:dependence\:on\:radius}$', fontsize=20)
#plt.grid(True)
plt.legend(frameon=False)#plt.legend(frameon=False,bbox_to_anchor=(0.95, 0.2), loc=1, borderaxespad=0.)
plt.savefig("Shear dependence on radius.png")
plt.show()
