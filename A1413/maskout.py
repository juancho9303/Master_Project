#THIS PROGRAM READS A SEGMENTATION IMAGE (COULD BE ANOTHER TYPE OF IMAGE) AND CREATES ANOTHER MASK IMAGE CHANGING THE VALUES OF PIXELS ACCORDING TO THE USER'S COMMAND

#!/usr/bin/python
import sys
import pyfits
import numpy as np

#DEFINES THE ORDER OF THE COMMANDS AS SYS.ARGV ARGUMENTS

input_image   = sys.argv[1]
segmap        = sys.argv[2]
output_image  = sys.argv[3]

#READS THE IMAGE AND SHOWS THE NUMBER OF ROWS AND COLUMNS

data, header  = pyfits.getdata(input_image, 0, header=True)
datos         = pyfits.getdata(segmap, 0)
row,col       = data.shape
row2,col2     = datos.shape
print 'The image is ',row, 'by ',col, 'pixels'
print 'The image is ',row2, 'by ',col2, 'pixels'

#CREATES THE MASK FILE CHANGING THE VALUE IN THE DESIRED PIXELS

mask = np.where(datos != 0, 0, data)
#mask = np.uint8(mask)
pyfits.writeto(output_image,mask,header,clobber = True)

