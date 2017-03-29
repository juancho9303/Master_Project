import numpy as np
from scipy import integrate
from scipy.integrate import quad
import matplotlib as mpl
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
mpl.rcParams['text.usetex'] = True

c        = 4.46           # concentration parameter (Paper Dutton and Maccio)
delta_c = (200./3)*(c**3)/(np.log(1+c)-c/(1+c))
rho_c    = 197.8            # Critical density in M_sun/kpc^3 (197.8)
r_s      = 100            # Characteristic radius (kpc) 
#sigma_c  = 4.76*10**8          # Critical surface mass density
sigma_c  = 10**8          # Critical surface mass density for z=1
sigma_c2 = 5.4*10**7      # Critical surface mass density for z=1.5     
sigma_c3 = 2*10**7        # Critical surface mass density for z=2

x1 = np.arange(0.001,0.99,0.0001)
plt.plot(x1*r_s,((r_s*delta_c*rho_c)/(sigma_c))*( ((8.*np.arctanh(np.sqrt((1-x1)/(1+x1))))/(x1*x1*np.sqrt(1-x1*x1))) + ((4*(np.log(x1/2)))/(x1*x1)) - ((2)/(x1*x1-1)) + ((4*np.arctanh(np.sqrt((1-x1)/(1+x1))))/((x1*x1-1)*(1-x1*x1)**0.5))))
x2 = 1
plt.plot(x2*r_s,((r_s*delta_c*rho_c)/(sigma_c))*(10./3.+4.*np.log(0.5)))
x3 = np.arange(1.0001,10,0.0001)
plt.plot(x3*r_s,((r_s*delta_c*rho_c)/(sigma_c))*( ((8.*np.arctan(np.sqrt((x3-1)/(1+x3))))/(x3*x3*np.sqrt(x3*x3-1))) + ((4*(np.log(x3/2)))/(x3*x3)) - ((2)/(x3*x3-1)) + ((4*np.arctan(np.sqrt((x3-1)/(1+x3))))/((x3*x3-1)**1.5))), label='z=1')

x4 = np.arange(0.001,0.99,0.0001)
plt.plot(x4*r_s,((r_s*delta_c*rho_c)/(sigma_c2))*( ((8.*np.arctanh(np.sqrt((1-x4)/(1+x4))))/(x4*x4*np.sqrt(1-x4*x4))) + ((4*(np.log(x4/2)))/(x4*x4)) - ((2)/(x4*x4-1)) + ((4*np.arctanh(np.sqrt((1-x4)/(1+x4))))/((x4*x4-1)*(1-x4*x4)**0.5))))
x5 = np.arange(1.0001,10,0.0001)
plt.plot(x5*r_s,((r_s*delta_c*rho_c)/(sigma_c2))*( ((8.*np.arctan(np.sqrt((x5-1)/(1+x5))))/(x5*x5*np.sqrt(x5*x5-1))) + ((4*(np.log(x5/2)))/(x5*x5)) - ((2)/(x5*x5-1)) + ((4*np.arctan(np.sqrt((x5-1)/(1+x5))))/((x5*x5-1)**1.5))), label='z=1.5')

x6 = np.arange(0.001,0.99,0.0001)
plt.plot(x6*r_s,((r_s*delta_c*rho_c)/(sigma_c3))*( ((8.*np.arctanh(np.sqrt((1-x6)/(1+x6))))/(x6*x6*np.sqrt(1-x6*x6))) + ((4*(np.log(x6/2)))/(x6*x6)) - ((2)/(x6*x6-1)) + ((4*np.arctanh(np.sqrt((1-x6)/(1+x6))))/((x6*x6-1)*(1-x6*x6)**0.5))))
x7 = np.arange(1.0001,10,0.0001)
plt.plot(x7*r_s,((r_s*delta_c*rho_c)/(sigma_c3))*( ((8.*np.arctan(np.sqrt((x7-1)/(1+x7))))/(x7*x7*np.sqrt(x7*x7-1))) + ((4*(np.log(x7/2)))/(x7*x7)) - ((2)/(x7*x7-1)) + ((4*np.arctan(np.sqrt((x7-1)/(1+x7))))/((x7*x7-1)**1.5))), label='z=2')

plt.axhline(y=.5, xmin=0., xmax=10., linewidth=1, color = 'k')

plt.ylim(0,3)
plt.xlabel('$R(kpc)$')
plt.ylabel('$\gamma_{NFW}$')
plt.title('Shear dependence on radius')
plt.grid(True)
plt.legend()
plt.savefig("Shear dependence on radius.png")
plt.show()
