from pylab import genfromtxt;
import numpy as np  
import matplotlib as mpl
from numpy import arange
import matplotlib.pyplot as plt
mpl.rcParams['text.usetex'] = True

mat1 = genfromtxt("sA1068r.cat");

y = mat1[:,1] #mag
z = mat1[:,6] #flux radius

filter1 = (mat1[:,1]<23.3)&(mat1[:,6]<2.25)
filter4 = (mat1[:,1]<18)&(mat1[:,6]<3.25)
filter5 = (mat1[:,1]<24)&(mat1[:,6]<2)
filter2 = (mat1[:,1]<16.0)
filter3 = (mat1[:,1]<30.0)

plt.plot(np.log10(z), y, '.', c = 'darkorange', label = r"$\mathrm{Galaxies}$", alpha=0.4);
plt.plot(np.log10(z[filter1]), y[filter1], '.', c = 'black', alpha=0.8);
plt.plot(np.log10(z[filter5]), y[filter5], '.', c = 'black', alpha=0.8);
plt.plot(np.log10(z[filter4]), y[filter4], '.', c = 'black', alpha=0.8);
plt.plot(np.log10(z[filter2]), y[filter2], '.', c = 'black', label = r"$\mathrm{Stars}$", alpha=0.8);

plt.ylim(27,13)
plt.xlim(0.15,1.35)
#plot "sA1068r.cat" using ($5>8.0 && $6<0.032?$7:1/0):2 w p ls 7 notitle
plt.xlabel(r'$\mathrm{Flux\:Radius}$',fontsize=18)
plt.ylabel(r'$\mathrm{m_{r}}$',fontsize=18)
plt.legend()
plt.savefig("mag_vs_flux_rad.png")
plt.show();
