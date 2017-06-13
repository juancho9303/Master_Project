import numpy as np
from photutils import aperture_photometry,CircularAperture
from photutils import CircularAnnulus
from astropy.io import fits
from astropy.table import Table

A1=fits.getdata('A754gready.fits') 
B=Table.read('filtered_flux_g.dat',format='ascii') 
A2=fits.getdata('A754rready.fits') 
A3=fits.getdata('A754iready.fits') 
A4=fits.getdata('A754uready.fits') 

positions = [B['col4'], B['col5']]
apertures = CircularAperture(positions, r=3.2)

positions2 = [(30., 30.)]
apertures2 = CircularAperture(positions2, r=3.)

#apertures = CircularAperture(positions, r=3.2)
annulus_apertures = CircularAnnulus(positions, r_in=6., r_out=7.5)

apers = [apertures, annulus_apertures]
phot_tableg = aperture_photometry(A1, apers) 
phot_tabler = aperture_photometry(A2, apers)   
phot_tablei = aperture_photometry(A3, apers)   
phot_tableu = aperture_photometry(A4, apers)

bkg_mean = phot_tableg['aperture_sum_1'] / annulus_apertures.area()
bkg_mean = phot_tabler['aperture_sum_1'] / annulus_apertures.area()
bkg_mean = phot_tablei['aperture_sum_1'] / annulus_apertures.area()
bkg_mean = phot_tableu['aperture_sum_1'] / annulus_apertures.area()

bkg_sum = bkg_mean * apertures.area()

final_sum = phot_tableg['aperture_sum_0'] - bkg_sum
phot_tableg['residual_aperture_sum'] = final_sum
print(phot_tableg) 
#print(phot_tableg['residual_aperture_sum'])    

final_sum = phot_tabler['aperture_sum_0'] - bkg_sum
phot_tabler['residual_aperture_sum'] = final_sum
print(phot_tabler) 
#print(phot_tabler['residual_aperture_sum'])    

final_sum = phot_tablei['aperture_sum_0'] - bkg_sum
phot_tablei['residual_aperture_sum'] = final_sum
print(phot_tablei) 
#print(phot_tablei['residual_aperture_sum'])    

final_sum = phot_tableu['aperture_sum_0'] - bkg_sum
phot_tableu['residual_aperture_sum'] = final_sum
print(phot_tableu) 
#print(phot_tableu['residual_aperture_sum'])    

import matplotlib.pylab as plt

plt.imshow(A1,interpolation='None',origin='lower',vmin=-1e3)
apertures.plot()
annulus_apertures.plot()
plt.show()
