from pylab import genfromtxt;
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn
import numpy as np
mpl.rcParams['text.usetex'] = True

mat1 = genfromtxt("A1650.txt");
mat2 = genfromtxt("A1650.zout");

z_a = mat2[:,2]
id1 = mat2[:,0]

filter1 = (mat2[:,2]<1.5)&(mat2[:,2]>0.0)

filtered_z_a = z_a[filter1]
filtered_id = id1[filter1]

print filtered_id

mg = mat1[:,1][filter1]
mr = mat1[:,3][filter1]
mi = mat1[:,5][filter1]
mu = mat1[:,7][filter1]
 
x = [3543,4770,6237,7625]

for i in range(0,len(filtered_id)):
		
	mg[i] = mat1[i,1]
	mr[i] = mat1[i,3]
	mi[i] = mat1[i,5]
	mu[i] = mat1[i,7]
	m = [mg[i], mr[i], mi[i], mu[i]]
	plt.plot(x,m, label=filtered_id[i], marker='o',linestyle='--')
		
plt.xlabel(r'$\lambda$',fontsize=18)
plt.ylabel(r'$\mathrm{Flux}$',fontsize=18)
plt.legend(loc=2,prop={'size':12})
plt.legend(frameon=True)
plt.savefig("magnitude_distribution_A1650.png")
plt.show()
