import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
import matplotlib.patches as mpatches

mpl.rcParams['text.usetex'] = True

# This plot is made for the cluster ABELL 1068

c        = 7.46           # concentration parameter
delta_c  = 6716.38        # Dimensionless overdensity using 4.46
# delta_c = 25315          # Dimensionless overdensity using c =  7.9
# delta_c = 44779          #Dimensionless overdensity for c=10
rho_c    = 200            # Critical density in M_sun/kpc^3 (197.8)
r_s      = 100            # characteristic radius (kpc) 
I_e      = 2.6*10**6      # Effective brightness (I(Re))
b        = 7.67           # Lokas and Mamon paper
R_e      = 18             # Half of the total light (kpc)

# Mass density profile from NFW density profile:

x1 = np.arange(0.001,1,0.0001)
plt.plot(x1,((2*r_s*delta_c*rho_c)/((x1*x1)-1))*(1-(2)/(np.sqrt(1-(x1*x1)))*np.arctanh(np.sqrt((1-x1)/(1+x1)))))
x2 = 1
plt.plot(x2,(2*r_s*delta_c*rho_c)/3)
x3 = np.arange(1.0001,100,0.0001)
plt.plot(x3,((2*r_s*delta_c*rho_c)/((x3*x3)-1))*(1-(2)/(np.sqrt((x3*x3)-1))*np.arctan(np.sqrt((x3-1)/(1+x3)))),label='NFW profile')

# Mass density profile from mass to light ratio and de Vaucouleurs profile:

x = np.arange(0.1,10000,0.001)
plt.plot(x/r_s,4*I_e*np.exp(-b*(((x)/(R_e))**(0.25)-1)),label='Stellar surface mass')  #4*I(R) where I(R) is de Vaucouleurs

plt.yscale('log')
plt.xscale('log')
plt.xlabel('$R/r_{s}$')
plt.ylabel('$\Sigma_{NFW}(M_{\odot }/ kpc^{2})$')
plt.title('Surface Mass Density')
plt.grid(True)
plt.legend()
plt.savefig("Surface_mass_density_full.png")
plt.show()
