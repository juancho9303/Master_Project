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

annulus_apertures = CircularAnnulus(positions, r_in=6., r_out=8.)

errorg = 0.1 * A1
errorr = 0.1 * A2
errori = 0.1 * A3
erroru = 0.1 * A4

apers = [apertures, annulus_apertures]
phot_tableg = aperture_photometry(A1, apers, error=errorg) 
phot_tabler = aperture_photometry(A2, apers, error=errorr)   
phot_tablei = aperture_photometry(A3, apers, error=errori)   
phot_tableu = aperture_photometry(A4, apers, error=erroru)

bkg_meang = phot_tableg['aperture_sum_1'] / annulus_apertures.area()
bkg_meanr = phot_tabler['aperture_sum_1'] / annulus_apertures.area()
bkg_meani = phot_tablei['aperture_sum_1'] / annulus_apertures.area()
bkg_meanu = phot_tableu['aperture_sum_1'] / annulus_apertures.area()

#print(bkg_mean)

bkg_sumg = ((bkg_meang+0.04)/2.) * apertures.area()
bkg_sumr = ((bkg_meanr+0.06)/2.) * apertures.area()
bkg_sumi = ((bkg_meani+0.1)/2.) * apertures.area()
bkg_sumu = ((bkg_meanu+0.01)/2.) * apertures.area()

final_sum = phot_tableg['aperture_sum_0'] - bkg_sumg
phot_tableg['residual_aperture_sum'] = final_sum
print(phot_tableg)   

final_sum = phot_tabler['aperture_sum_0'] - bkg_sumr
phot_tabler['residual_aperture_sum'] = final_sum
print(phot_tabler)     

final_sum = phot_tablei['aperture_sum_0'] - bkg_sumi
phot_tablei['residual_aperture_sum'] = final_sum
print(phot_tablei)     

final_sum = phot_tableu['aperture_sum_0'] - bkg_sumu
phot_tableu['residual_aperture_sum'] = final_sum
print(phot_tableu)    

phot_tableg.write('ap_phot_g_average.txt',format='ascii.ipac')
phot_tabler.write('ap_phot_r_average.txt',format='ascii.ipac')
phot_tablei.write('ap_phot_i_average.txt',format='ascii.ipac')
phot_tableu.write('ap_phot_u_average.txt',format='ascii.ipac') 
