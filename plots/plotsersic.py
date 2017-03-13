import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
import math

mpl.rcParams['text.usetex'] = True

I_e  = 6716.38        # Dimensionless overdensity
b    = 7.67           # Critical density in m_sun/kpc^3
R_e  = 60             # 60 kp

x = np.arange(0.01,100,0.0001)
plt.plot(x,I_e*np.exp(-b*((x/R_e)**(0.25)-1)))

plt.yscale('log')
plt.xscale('log')
plt.xlabel('$R/r_{s}$')
plt.ylabel('$I(R)$')
plt.title('$deVaucouleurs$')
plt.grid(True)
plt.savefig("deVaucouleurs.png")
plt.show()
