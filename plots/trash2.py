import numpy as np
from scipy import integrate
from scipy.integrate import quad
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import gridspec
mpl.rcParams['text.usetex'] = True
'''
f = lambda r: 2.0*np.pi*r/r_s*( ( 2.0*r_s*delta_c*rho_c )/( (r/r_s)**2 - 1.0 ) )*( 1.0 - 2.0/( np.sqrt( 1.0 - (r/r_s)**2 ) )*np.arctanh( np.sqrt( ( 1.0-r/r_s )/( 1.0 + r/r_s ) ) ) ) if r<r_s\ 
	2.0*r_s*delta_c*rho_c/3.0 elif r==r_s\
	else 2.0*np.pi*r/r_s*( ( 2.0*r_s*delta_c*rho_c )/( (r/r_s)**2 - 1.0 ) )*( 1.0 - 2.0/( np.sqrt( (r/r_s)**2 - 1.0 ) )*np.arctan( np.sqrt( ( r/r_s - 1.0 )/( 1 + r/r_s ) ) ) )
inte = integrate.quad(f,0,6)[0]
print inte
'''

inte = integrate.quad(lambda x:np.piecewise(x, [x < 3, x >= 3], 
     [lambda x: np.polyval([1,3,0],x), 
      lambda x: np.polyval([-2,2,0],x)]),
     0,6)
print inte
