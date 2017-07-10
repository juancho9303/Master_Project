from pylab import genfromtxt;
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn
import numpy as np
mpl.rcParams['text.usetex'] = True

mat1 = genfromtxt("A85.txt");
mat2 = genfromtxt("wavelengths.txt");

mg = mat1[:,1]
mr = mat1[:,3]
mi = mat1[:,5]
mu = mat1[:,7]

x1 = mat2[:,0]
x2 = mat2[:,1]
x3 = mat2[:,2]
x4 = mat2[:,3]

#x1 = 4770 
#x2 = 6237 
#x3 = 7625
#x4 = 3543

plt.plot(x1,mg, label=r'$\mathrm{m}<22$', marker='o', linestyle='--')
plt.plot(x2,mr, label=r'$\mathrm{m}<23$', marker='o', linestyle='--')
plt.plot(x3,mi, label=r'$\mathrm{m}<24$', marker='o', linestyle='--')
plt.plot(x4,mu, label=r'$\mathrm{m}<25$', marker='o', linestyle='--')

plt.xlabel(r'$\mathrm{Redshift}$',fontsize=18)
plt.ylabel(r'$\mathrm{Galaxies\:/arcmin^{2}/0.2z}$',fontsize=18)
plt.legend(loc=2,prop={'size':12})
plt.legend(frameon=True)
plt.savefig("magnitude_distribution.png")
plt.show()
