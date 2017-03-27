import numpy as np
from scipy import integrate
from scipy.integrate import quad
import matplotlib as mpl
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
mpl.rcParams['text.usetex'] = True

c        = 4.46           # concentration parameter (Paper Dutton and Maccio) this was checked many times 
delta_c = (200./3)*(c*c*c)/(np.log(1+c)-c/(1+c))
rho_c    = 197.8            # Critical density in M_sun/kpc^3 (197.8)
r_s      = 100            # Characteristic radius (kpc) 
I_e      = 5.1*10**8      # Effective brightness I(Re) 2.6e6
b        = 7.67           # Lokas and Mamon paper
R_e      = 73.7             # Half of the total light in kpc

#MASS ENCLOSED BY LIGHT (DE VAUCOULEURS PROFILE)

def surf_bright(r):
	return 2*np.pi*I_e*np.exp(-b*((r/(R_e))**(0.25)-1))
R = np.arange(0.1,10000,0.1)
def F(r):
    res = np.zeros_like(r)
    for i,val in enumerate(r):
        y,err = integrate.quad(surf_bright,0,val)
        res[i]=y
    return res
plt.plot(R,F(R),label='Mass in Stars')

#NOW FOR THE MASS OF THE NFW PROFILE

def NFW(x):
	if (x<1.0):
		surf_mass = 2.*np.pi*x*((2*r_s*delta_c*rho_c)/((x*x)-1))*(1-(2)/(np.sqrt(1-(x*x)))*np.arctanh(np.sqrt((1-x)/(1+x))))
	elif (x==1.0):
		surf_mass = (2.*r_s*delta_c*rho_c)/3
	else:
		surf_mass = 2.*np.pi*x*((2*r_s*delta_c*rho_c)/((x*x)-1))*(1-(2)/(np.sqrt((x*x)-1))*np.arctan(np.sqrt((x-1)/(1+x))))
	return surf_mass
	
X = np.arange(0.001,100,0.1)

def Mass(x):
    res2 = np.zeros_like(x)
    for j,val in enumerate(x):
        y,err = integrate.quad(NFW,0,val)
        res2[j]=y
    return res2
plt.plot(X*r_s,Mass(X),label='Dynamical Mass')

plt.yscale('log')
plt.xscale('log')
plt.xlabel('$R(kpc)$')
plt.ylabel('$M_{\odot }$')
plt.title('Enclosed Mass')
plt.grid(True)
plt.legend()
plt.savefig("Enclosed Mass.png")
plt.show()
