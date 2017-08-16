import numpy as np

from evtk.hl import gridToVTK
from astropy.io import fits

# read in a fits file
def read_fits_file(filename):
    hdulist = fits.open(filename)
    return (hdulist[0].header, hdulist[0].data)

def write_structured_vtk(filename):
    pass

def main():
    pass
