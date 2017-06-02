from pylab import genfromtxt;
import numpy as np  
import seaborn
import matplotlib as mpl
from numpy import arange
import matplotlib.pyplot as plt
mpl.rcParams['text.usetex'] = True

mat0 = genfromtxt("sA1068g.cat");
mat1 = genfromtxt("sA1068r.cat");

mg = mat0[:,1]
mr = mat1[:,1]
fg = mat1[:,1] #mag
fr = mat1[:,6] #flux radius
col = mg-mr

filter1 = (mat1[:,1]<23.3)&(mat1[:,6]<2.25)
filter4 = (mat1[:,1]<18)&(mat1[:,6]<3.25)
filter5 = (mat1[:,1]<24)&(mat1[:,6]<2)
filter2 = (mat1[:,1]<16.0)

plt.plot(mg-mr, mr, '.', c = 'darkorange', label = r"$\mathrm{Galaxies}$", alpha=0.5);
plt.plot((col[filter1]), mr[filter1], '.', c = 'black', alpha=0.8);
plt.plot((col[filter5]), mr[filter5], '.', c = 'black', alpha=0.8);
plt.plot((col[filter4]), mr[filter4], '.', c = 'black', alpha=0.8);
plt.plot((col[filter2]), mr[filter2], '.', c = 'black', label = r"$\mathrm{Stars}$", alpha=0.8);

plt.ylim(15,27)
plt.xlim(-0.1,2.3)
#plot "sA1068r.cat" using ($5>8.0 && $6<0.032?$7:1/0):2 w p ls 7 notitle
plt.xlabel(r'$\mathrm{m_{g}-m_{r}}$',fontsize=18)
plt.ylabel(r'$\mathrm{m_{r}}$',fontsize=18)
plt.legend(bbox_to_anchor=(0.95, 0.35))
plt.savefig("color_mag.png")
plt.show();
