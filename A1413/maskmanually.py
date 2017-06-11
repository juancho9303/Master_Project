import matplotlib.pyplot as plt
import matplotlib.cm as cm
from astropy.io import fits
import pyregion
import pyfits
import numpy as np

cluster_name = "blanckimage.fits"
image        = fits.open(cluster_name)

#cluster_name = sys.argv[1]
#output_image = sys.argv[2]

try:
    from astropy.wcs import WCS
    from wcsaxes import WCSAxes

    wcs = WCS(image[0].header)
    fig = plt.figure()
    ax = WCSAxes(fig, [0.1, 0.1, 0.8, 0.8], wcs=wcs)
    fig.add_axes(ax)
except ImportError:
    ax = plt.subplot(111)

ax.imshow(image[0].data, cmap=cm.gray, vmin=0., vmax=0.00038, origin="lower")

reg_name  = "A2029fullregions.reg"
r         = pyregion.open(reg_name).as_imagecoord(header=image[0].header)
from pyregion.mpl_helper import properties_func_default

def fixed_color(shape, saved_attrs):
    attr_list, attr_dict  = saved_attrs
    attr_dict["color"]    = "red"
    kwargs                = properties_func_default(shape, (attr_list, attr_dict))

    return kwargs

myfilter = r.get_filter()
mask_1and2 = (myfilter).mask((image[0].data.shape))

image[0].data[mask_1and2] = 30.0

image.writeto('A2029maskready.fits')

#image.writeto(output_image)
