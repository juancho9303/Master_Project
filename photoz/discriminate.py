from pylab import genfromtxt;
import numpy as np  
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.rcParams['text.usetex'] = True

# THIS PROGRAM SELECTS THE GALAXIES FROM THE SEXTRACTOR OUTPUT SO THAT WE CAN USE THEM TO DO PHOTOMETRIC REDSHIFTS
# IT SAVES THE COORDINATES, THE FLUXES AND THE FLUX ERROR FOR THE G,R,U,I BANDS. 

mat0 = genfromtxt("A754g.cat"); mat1 = genfromtxt("A754r.cat"); mat2 = genfromtxt("A754u.cat"); mat3 = genfromtxt("A754i.cat");

xg = mat0[:,3]; yg = mat0[:,4]; flu_g = mat0[:,1]; flu_err_g = mat0[:,2] 
xr = mat1[:,3]; yr = mat1[:,4]; flu_r = mat1[:,1]; flu_err_r = mat1[:,2]
xu = mat2[:,3]; yu = mat2[:,4]; flu_u = mat2[:,1]; flu_err_u = mat2[:,2]
xi = mat3[:,3]; yi = mat3[:,4]; flu_i = mat3[:,1]; flu_err_i = mat3[:,2]
id_n = mat0[:,0]

filters = (mat0[:,5]>8.0)&(mat0[:,6]<0.029)&(mat1[:,5]>8.0)&(mat1[:,6]<0.029)&\
          (mat2[:,5]>8.0)&(mat2[:,6]<0.029)&(mat3[:,5]>8.0)&(mat3[:,6]<0.029)

coordx_g  = list(xg[filters]); coordy_g  = list(yg[filters]); F_g = list(flu_g[filters]); F_err_g = list(flu_err_g[filters])
coordx_r  = list(xr[filters]); coordy_r  = list(yr[filters]); F_r = list(flu_r[filters]); F_err_r = list(flu_err_r[filters])
coordx_u  = list(xu[filters]); coordy_u  = list(yu[filters]); F_u = list(flu_u[filters]); F_err_u = list(flu_err_u[filters])
coordx_i  = list(xi[filters]); coordy_i  = list(yi[filters]); F_i = list(flu_i[filters]); F_err_i = list(flu_err_i[filters])
id_num = list(id_n[filters])

#Matrix_g = np.matrix([id_num, F_g, F_err_g, F_r, F_err_r, F_u, F_err_u, F_i, F_err_i])
Matrix_g = np.matrix([id_num, coordx_g, coordy_g, F_g, F_err_g])
Matrix_r = np.matrix([id_num, coordx_r, coordy_r, F_r, F_err_r])
Matrix_u = np.matrix([id_num, coordx_u, coordy_u, F_u, F_err_u])
Matrix_i = np.matrix([id_num, coordx_i, coordy_i, F_i, F_err_i])

#np.savetxt('fluxes.dat', Matrix_g.T,fmt='%f')
np.savetxt('filtered_flux_g.dat', Matrix_g.T,fmt='%f')
np.savetxt('filtered_flux_r.dat', Matrix_r.T,fmt='%f')
np.savetxt('filtered_flux_u.dat', Matrix_u.T,fmt='%f')
np.savetxt('filtered_flux_i.dat', Matrix_i.T,fmt='%f')
