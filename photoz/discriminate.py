from pylab import genfromtxt;
import numpy as np  
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.rcParams['text.usetex'] = True

mat0 = genfromtxt("A754g.cat");
mat1 = genfromtxt("A754r.cat");
mat2 = genfromtxt("A754u.cat");
mat3 = genfromtxt("A754i.cat");

x = mat0[:,3]
y = mat0[:,4]

filter = (mat0[:,5]>8.0)&(mat0[:,6]<0.029)

mierda  = list(x[filter])
mierda2 = list(y[filter])

Matrix[[]]

np.savetxt('test.out', Matrix)
#np.savetxt('test.out', [x[filter],y[filter]])
#np.savetxt('test.out', [x[filter],y[filter]])
#np.savetxt('test.out', [x[filter],y[filter]])
