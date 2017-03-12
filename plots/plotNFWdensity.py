import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

mpl.rcParams['text.usetex'] = True

delta_c  = 6716.38
#rho_c   = 1.36*10**(-14) in SI
rho_c    = 2.9*10**(-7) 
#r_s     = 1.234*10**21 in SI
r_s      = 40
r        = np.arange(0.001, 1000, 0.001)
rho      = (delta_c*rho_c)/((r/r_s)*(1+(r/r_s))**2)
plt.yscale('log')
plt.xscale('log')
plt.plot(r,rho)
plt.xlabel('$Radius\,(kpc)$')
plt.ylabel('$Density\,(M_{\odot}/pc^{3})$')
plt.title('$Density\,\,Profile$')
plt.grid(True)
plt.savefig("Density_profile.png")
plt.show()
