import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

mpl.rcParams['text.usetex'] = True

delta_c  = 6716.38        # Dimensionless overdensity
rho_c    = 2900           # Critical density in m_sun/kpc^3
r_s      = 40             # 40 kp
I_e  = 1.27            # Effective brightness (I(Re)) 
b    = 7.67               # (Lokas and Mamon paper)
R_e  = 30                 # 30 kp

x1 = np.arange(0.001,1,0.00001)
plt.plot(x1,((2*r_s*delta_c*rho_c)/((x1*x1)-1))*(1-(2)/(np.sqrt(1-(x1*x1)))*np.arctanh(np.sqrt((1-x1)/(1+x1)))))
x2 = 1
plt.plot(x2,(2*r_s*delta_c*rho_c)/3)
x3 = np.arange(1.00001,500,0.00001)
plt.plot(x3,((2*r_s*delta_c*rho_c)/((x3*x3)-1))*(1-(2)/(np.sqrt((x3*x3)-1))*np.arctanh(np.sqrt((x3-1)/(1+x3)))))

x = np.arange(0.001,500,0.0001)
plt.plot(x,I_e*np.exp(-b*((x/R_e)**(0.25)-1)))

plt.yscale('log')
plt.xscale('log')
plt.xlabel('$R/r_{s}$')
plt.ylabel('$\Sigma_{NFW}(M_{\odot }/ kpc^{2})$')
plt.title('$Surface\,Mass\,Density$')
plt.grid(True)
plt.savefig("Surface_mass_density_full.png")
plt.show()
