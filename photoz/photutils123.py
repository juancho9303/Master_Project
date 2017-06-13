import numpy as np
from photutils import aperture_photometry,CircularAperture
from astropy.io import fits
from astropy.table import Table

A1=fits.getdata('A754gready.fits') 
B1=Table.read('filtered_flux_g.dat',format='ascii') 
A2=fits.getdata('A754rready.fits') 
B2=Table.read('filtered_flux_r.dat',format='ascii') 
A3=fits.getdata('A754iready.fits') 
B3=Table.read('filtered_flux_i.dat',format='ascii') 
A4=fits.getdata('A754uready.fits') 
B4=Table.read('filtered_flux_u.dat',format='ascii') 

positions = [B1['col4'], B1['col5']]
apertures = CircularAperture(positions, r=3.1)
positions = [B2['col4'], B2['col5']]
apertures = CircularAperture(positions, r=3.1)
positions = [B3['col4'], B3['col5']]
apertures = CircularAperture(positions, r=3.1)
positions = [B4['col4'], B4['col5']]
apertures = CircularAperture(positions, r=3.1)

phot_tableg = aperture_photometry(A1, apertures)
print(phot_tableg)  
phot_tabler = aperture_photometry(A2, apertures)
print(phot_tabler)    
phot_tablei = aperture_photometry(A3, apertures)
print(phot_tablei)    
phot_tableu = aperture_photometry(A4, apertures)
print(phot_tableu)      
