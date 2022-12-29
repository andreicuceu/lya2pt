import numpy as np

from lya2pt.cosmo import Cosmology

DEFAULT_SETTINGS = {'rp-min': 0., 'rp-max': 200., 'rt-min': 0., 'rt-max': 200.,
                    'num-rp': int(50), 'num-rt': int(50), 'z-cut-min': 0., 'z-cut-max': 10.,
                    'z-ref': 2.25, 'z-evol': 2.9, 'fid-Om': 0.3153, 'no-project': False,
                    'nside': int(16), 'nspec': None, 'rebin-factor': None}


class Lya2pt:
    """Main lya2pt interface
    """
    def __init__(self, outfile: str, in_dir: str, in_dir2: str = None,
                 settings: dict = DEFAULT_SETTINGS) -> None:

        cosmo = Cosmology(settings['fid-Om'])
