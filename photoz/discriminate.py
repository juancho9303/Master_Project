from pylab import genfromtxt;
import numpy as np  
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.rcParams['text.usetex'] = True

# THIS PROGRAM SELECTS THE GALAXIES FROM THE SEXTRACTOR OUTPUT SO THAT WE CAN USE THEM TO DO PHOTOMETRIC REDSHIFTS
# IT SAVES THE COORDINATES, THE MAGNITUDE AND THE MAGNITUDE ERROR FOR THE G,R,U,I BANDS. 

mat0 = genfromtxt("A754g.cat"); mat1 = genfromtxt("A754r.cat"); mat2 = genfromtxt("A754u.cat"); mat3 = genfromtxt("A754i.cat");

xg = mat0[:,3]; yg = mat0[:,4]; mag_g = mat0[:,1]; mag_err_g = mat0[:,2] 
xr = mat1[:,3]; yr = mat1[:,4]; mag_r = mat1[:,1]; mag_err_r = mat1[:,2]
xu = mat2[:,3]; yu = mat2[:,4]; mag_u = mat2[:,1]; mag_err_u = mat2[:,2]
xi = mat3[:,3]; yi = mat3[:,4]; mag_i = mat3[:,1]; mag_err_i = mat3[:,2]

filters = (mat0[:,5]>8.0)&(mat0[:,6]<0.029)&(mat1[:,5]>8.0)&(mat1[:,6]<0.029)&\
          (mat2[:,5]>8.0)&(mat2[:,6]<0.029)&(mat3[:,5]>8.0)&(mat3[:,6]<0.029)&\
          (mat0[:,1]<30.0)&(mat1[:,1]<30.0)&(mat2[:,1]<30.0)&(mat3[:,1]<30.0)

coordx_g  = list(xg[filters]); coordy_g  = list(yg[filters]); m_g = list(mag_g[filters]); m_err_g = list(mag_err_g[filters])
coordx_r  = list(xr[filters]); coordy_r  = list(yr[filters]); m_r = list(mag_r[filters]); m_err_r = list(mag_err_r[filters])
coordx_u  = list(xu[filters]); coordy_u  = list(yu[filters]); m_u = list(mag_u[filters]); m_err_u = list(mag_err_u[filters])
coordx_i  = list(xi[filters]); coordy_i  = list(yi[filters]); m_i = list(mag_i[filters]); m_err_i = list(mag_err_i[filters])

Matrix_g = np.matrix([coordx_g, coordy_g, m_g, m_err_g])
Matrix_r = np.matrix([coordx_r, coordy_r, m_r, m_err_r])
Matrix_u = np.matrix([coordx_u, coordy_u, m_u, m_err_u])
Matrix_i = np.matrix([coordx_i, coordy_i, m_i, m_err_i])

np.savetxt('filtered_g.dat', Matrix_g.T,fmt='%f')
np.savetxt('filtered_r.dat', Matrix_r.T,fmt='%f')
np.savetxt('filtered_u.dat', Matrix_u.T,fmt='%f')
np.savetxt('filtered_i.dat', Matrix_i.T,fmt='%f')
