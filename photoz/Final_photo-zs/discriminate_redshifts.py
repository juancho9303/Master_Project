from pylab import genfromtxt;
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn
import numpy as np
mpl.rcParams['text.usetex'] = True

mat1 = genfromtxt("A85.zout");

z_a = mat1[:,2]
id1 = mat1[:,0]
#print z_a

filter1 = (mat1[:,2]<2.0)&(mat1[:,2]>0.0)

filtered_z_a = z_a[filter1]
filtered_id = id1[filter1]

print filtered_id 
"""
filter4 = (mat1[:,1]<16.0)

coordx_g  = list(xg[filters])
 
plt.plot(x,m, marker='o',linestyle='--')
		
plt.xlabel(r'$\lambda$',fontsize=18)
plt.ylabel(r'$\mathrm{Flux}$',fontsize=18)
plt.legend(loc=2,prop={'size':12})
plt.legend(frameon=True)
plt.savefig("magnitude_distribution.png")
plt.show()
"""
