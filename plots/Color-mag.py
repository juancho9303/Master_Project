from pylab import genfromtxt;
import numpy as np  
import matplotlib as mpl
from numpy import arange
import matplotlib.pyplot as plt
mpl.rcParams['text.usetex'] = True

mat0 = genfromtxt("sA1068g.cat");
mat1 = genfromtxt("sA1068r.cat");

x = mat0[:,1]
y = mat1[:,1]

filter = (mat0[:,4]<38.0)&(mat0[:,5]>0.001)
#filter = (mat0[:,4]<8.0)&(mat0[:,5]>0.029)   THIS IS THE REAL FILTER
plt.plot(x[filter]-y[filter],y[filter], '*', label = r"$\mathrm{Stars}$")

filter = (mat0[:,4]>8.0)&(mat0[:,5]<0.029)
plt.plot(x[filter]-y[filter],y[filter], 'o', c = 'darkorange', label = r"$\mathrm{Galaxies}$")

plt.ylim(15,27)
plt.xlim(0,2)
plt.xlabel(r'$\mathrm{m_{g}-m_{r}}$',fontsize=18)
plt.ylabel(r'$\mathrm{m_{r}}$',fontsize=18)
#plt.title(r'$\mathrm{Color\:Magnitude\:Diagram\:A1068}$',fontsize=20)
plt.legend(bbox_to_anchor=(0.95, 0.2), loc=1, borderaxespad=0.)
plt.savefig("color_mag.png")
plt.show();

# NOW, FOR THE OTHER PLOT

z = mat1[:,6]

filter = (mat0[:,4]<38.0)&(mat0[:,5]>0.0001)
plt.plot(np.log10(z[filter]), y[filter], '*', label = r"$\mathrm{Stars}$");

filter = (mat0[:,4]>8.0)&(mat0[:,5]<0.029)
plt.plot(np.log10(z[filter]), y[filter], 'o', c = 'darkorange', label = r"$\mathrm{Galaxies}$");

plt.ylim(27,14)
plt.xlim(0.15,1.35)
#plot "sA1068r.cat" using ($5>8.0 && $6<0.032?$7:1/0):2 w p ls 7 notitle
#plt.xscale( "log" )
plt.xlabel(r'$\mathrm{\log Flux\:Radius}$',fontsize=18)
plt.ylabel(r'$\mathrm{m_{r}}$',fontsize=18)
#plt.xticks(arange(1,13,1))
#plt.title(r'$\mathrm{Magnitude\:vs\:Flux\:Radius}$',fontsize=20)
plt.legend()
plt.savefig("mag_vs_flux_rad.png")
plt.show();
