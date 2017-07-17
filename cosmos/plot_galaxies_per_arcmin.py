import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn
import numpy as np
mpl.rcParams['text.usetex'] = True

x1, y1 = np.loadtxt('zbins_matched_22.dat', delimiter='\t', unpack=True)
x2, y2 = np.loadtxt('zbins_matched_23.dat', delimiter='\t', unpack=True)
x3, y3 = np.loadtxt('zbins_matched_24.dat', delimiter='\t', unpack=True)
x4, y4 = np.loadtxt('zbins_matched_25.dat', delimiter='\t', unpack=True)
x5, y5 = np.loadtxt('zbins_matched_26.dat', delimiter='\t', unpack=True)
plt.plot(x1,y1, label=r'$\mathrm{m}<22$', marker='o', linestyle='--')
plt.plot(x2,y2, label=r'$\mathrm{m}<23$', marker='o', linestyle='--')
plt.plot(x3,y3, label=r'$\mathrm{m}<24$', marker='o', linestyle='--')
plt.plot(x4,y4, label=r'$\mathrm{m}<25$', marker='o', linestyle='--')
plt.plot(x5,y5, label=r'$\mathrm{m}<26$', marker='o', linestyle='--')
plt.axvline(0.2, c = 'black', linestyle='--')
plt.axvline(0.4, c = 'black', linestyle='--')
plt.axvline(0.6, c = 'black', linestyle='--')
plt.axvline(0.8, c = 'black', linestyle='--')
plt.axvline(1.0, c = 'black', linestyle='--')
plt.axvline(1.2, c = 'black', linestyle='--')

#plt.xlim(0.,1.5)
plt.xlabel(r'$\mathrm{Redshift}$',fontsize=18)
plt.ylabel(r'$\mathrm{Galaxies\:/arcmin^{2}/0.2z}$',fontsize=18)
#plt.xlabel(r'$\mathrm{z}$',fontsize=18)
#plt.ylabel(r'$\mathrm{n}$',fontsize=18)
#plt.title(r'$\mathrm{Galaxies\:per\:arcmin\:in\:radial\:bins}$',fontsize=18)
plt.legend(loc=2,prop={'size':12})
plt.legend(frameon=True)
plt.savefig("galaxies_per_arcmin.png")
plt.show()
