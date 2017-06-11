#THIS PROGRAM READS A SEGMENTATION IMAGE (COULD BE ANOTHER TYPE OF IMAGE) AND CREATES ANOTHER MASK IMAGE CHANGING THE VALUES OF PIXELS ACCORDING TO THE USER'S COMMAND

#!/usr/bin/python
import sys
import pyfits
import numpy as np

#PRINTS THE ORDER OF THE COMMANDS TO BE PUT IN THE TERMINAL

print 'makemask input_image output_image object_id'

#DEFINES THE ORDER OF THE COMMANDS AS SYS.ARGV ARGUMENTS

input_image=sys.argv[1]
output_image=sys.argv[2]
obj_exclude=int(sys.argv[3])

#READS THE IMAGE AND SHOWS THE NUMBER OF ROWS AND COLUMNS

data, header=pyfits.getdata(input_image, 0, header=True)
row,col= data.shape
print 'The image is ',row, 'by ',col, 'pixels'

#CREATES THE MASK FILE CHANGING THE VALUE IN THE DESIRED PIXELS

mask=np.where(data==obj_exclude,0,data)
mask=np.uint8(mask)
pyfits.writeto(output_image,mask,header,clobber=True)

