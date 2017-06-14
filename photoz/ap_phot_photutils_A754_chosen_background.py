import numpy as np
from photutils import aperture_photometry,CircularAperture
from photutils import CircularAnnulus
from astropy.io import fits
from astropy.table import Table
import matplotlib.pylab as plt

A1=fits.getdata('A754gready.fits') 
A2=fits.getdata('A754rready.fits') 
A3=fits.getdata('A754iready.fits') 
A4=fits.getdata('A754uready.fits') 
B=Table.read('filtered_flux_g.dat',format='ascii') 

#The background in a smooth region
background_coords = [(30., 30.)]
apertures2 = CircularAperture(background_coords, r=3.2)
#print(apertures2)

#The objects found by sextractor
positions = [B['col4'], B['col5']]
apertures = CircularAperture(positions, r=3.2)

annulus_apertures = CircularAnnulus(positions, r_in=6., r_out=7.5)

apers = [apertures, annulus_apertures]
phot_tableg = aperture_photometry(A1, apers) 
phot_tabler = aperture_photometry(A2, apers)   
phot_tablei = aperture_photometry(A3, apers)   
phot_tableu = aperture_photometry(A4, apers)

bkg_meang = phot_tableg['aperture_sum_1'] / annulus_apertures.area()
bkg_meanr = phot_tabler['aperture_sum_1'] / annulus_apertures.area()
bkg_meani = phot_tablei['aperture_sum_1'] / annulus_apertures.area()
bkg_meanu = phot_tableu['aperture_sum_1'] / annulus_apertures.area()


bkg_sumg = 0.04 * apertures.area()
bkg_sumr = 0.06 * apertures.area()
bkg_sumi = 0.1 * apertures.area()
bkg_sumu = 0.01 * apertures.area()

final_sum = phot_tableg['aperture_sum_0'] - bkg_sumg
phot_tableg['residual_aperture_sum'] = final_sum
print(phot_tableg) 
#np.savetxt('ap_phot_A754g.dat', phot_tableg, fmt='%f')   

final_sum = phot_tabler['aperture_sum_0'] - bkg_sumr
phot_tabler['residual_aperture_sum'] = final_sum
print(phot_tabler)     

final_sum = phot_tablei['aperture_sum_0'] - bkg_sumi
phot_tablei['residual_aperture_sum'] = final_sum
print(phot_tablei)     

final_sum = phot_tableu['aperture_sum_0'] - bkg_sumu
phot_tableu['residual_aperture_sum'] = final_sum
print(phot_tableu)    

phot_tableg.write('ap_phot_g_chosen_background.txt',format='ascii.ipac')
phot_tabler.write('ap_phot_r_chosen_background.txt',format='ascii.ipac')
phot_tablei.write('ap_phot_i_chosen_background.txt',format='ascii.ipac')
phot_tableu.write('ap_phot_u_chosen_background.txt',format='ascii.ipac')
