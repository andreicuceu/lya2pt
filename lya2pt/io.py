import fitsio
import numpy as np

from lya2pt.cpu_data import CPUDelta
from lya2pt.utils import project_forest, rebin_forest

LAMBDA_LYA = 1215.67


def read_file(filename, cosmo, no_project, rebin_factor):
    hdul = fitsio.FITS(filename)
    deltas = np.array([read_forest(hdu, cosmo, no_project, rebin_factor) for hdu in hdul[1:]])

    return deltas


def read_forest(hdu, cosmo, no_project, rebin_factor):
    header = hdu.read_header()

    ra = header['RA']
    dec = header['DEC']
    z_qso = header['Z']

    if 'THING_ID' in header:
        los_id = header['THING_ID']
    elif 'LOS_ID' in header:
        los_id = header['LOS_ID']
    else:
        raise Exception("Could not find THING_ID or LOS_ID")

    if 'LOGLAM' in hdu.get_colnames():
        wave = 10**(hdu['LOGLAM'][:].astype(float))
    elif 'LAMBDA' in hdu.get_colnames():
        wave = hdu['LAMBDA'][:].astype(float)
    else:
        raise KeyError("Did not find LOGLAM or LAMBDA in delta file")

    delta = hdu['DELTA'][:].astype(float)
    weights = hdu['WEIGHT'][:].astype(float)

    if rebin_factor is not None:
        wave, delta, weights = rebin_forest(wave, delta, weights, rebin_factor)

    z = wave / LAMBDA_LYA - 1.
    dist_c = cosmo.comovin_distance(z)
    dist_m = cosmo.comovin_transverse_distance(z)

    if not no_project:
        delta = project_forest(wave, delta, weights)

    return CPUDelta(z, wave, delta, weights, dist_c, dist_m,
                    ra, dec, z_qso, los_id)
