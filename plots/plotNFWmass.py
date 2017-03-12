import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

mpl.rcParams['text.usetex'] = True

delta_c  = 6716.38
rho_c    = 2.9*10**(-7) 
r_s      = 4*10**9
r        = np.arange(0.001, 1000, 0.001)

x1 = np.arange(0.001,1,0.00001)
plt.plot(x1,((2*r_s*delta_c*rho_c)/((x1*x1)-1))*(1-(2)/(np.sqrt(1-(x1*x1)))*np.arctanh(np.sqrt((1-x1)/(1+x1)))))
x2 = 1
plt.plot(x2,(2*r_s*delta_c*rho_c)/3)
x3 = np.arange(1.00001,100,0.00001)
plt.plot(x3,((2*r_s*delta_c*rho_c)/((x3*x3)-1))*(1-(2)/(np.sqrt((x3*x3)-1))*np.arctanh(np.sqrt((x3-1)/(1+x3)))))
plt.yscale('log')
plt.xscale('log')
plt.xlabel('$R/r_{s}$')
plt.ylabel('$\Sigma_{NFW}(M_{\odot }/ kpc^{2})$')
plt.title('$Surface\,Mass\,Density$')
plt.grid(True)
plt.savefig("test2.png")

plt.show()
