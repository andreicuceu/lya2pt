import argparse

from lya2pt import Lya2pt

if __name__ == '__main__':
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter,
                                     description='Compute the auto-correlation of delta fields')

    parser.add_argument('--out', type=str, default=None, required=True,
                        help='Output file name')

    parser.add_argument('--in-dir', type=str, default=None, required=True,
                        help='Directory to delta files')

    parser.add_argument('--in-dir2', type=str,default=None, required=False,
                        help='Directory to 2nd delta files')

    parser.add_argument('--rp-min', type=float, default=0., required=False,
                        help='Min r-parallel [h^-1 Mpc]')

    parser.add_argument('--rp-max', type=float, default=200., required=False,
                        help='Max r-parallel [h^-1 Mpc]')

    parser.add_argument('--rt-min', type=float, default=0., required=False,
                        help='Max r-transverse [h^-1 Mpc]')

    parser.add_argument('--rt-max', type=float, default=200., required=False,
                        help='Max r-transverse [h^-1 Mpc]')

    parser.add_argument('--num-rp', type=int, default=50, required=False,
                        help='Number of r-parallel bins')

    parser.add_argument('--num-rt', type=int, default=50, required=False,
                        help='Number of r-transverse bins')

    parser.add_argument('--z-cut-min', type=float, default=0., required=False,
                        help=('Use only pairs of forest x object with the mean '
                              'of the last absorber redshift and the object '
                              'redshift larger than z-cut-min'))

    parser.add_argument('--z-cut-max', type=float, default=10., required=False,
                        help=('Use only pairs of forest x object with the mean '
                              'of the last absorber redshift and the object '
                              'redshift smaller than z-cut-max'))

    parser.add_argument('--z-ref', type=float, default=2.25, required=False,
                        help='Reference redshift')

    parser.add_argument('--z-evol', type=float, default=2.9, required=False,
                        help=('Exponent of the redshift evolution of the delta field'))

    parser.add_argument('--fid-Om', type=float, default=0.3153, required=False,
                        help=('Omega_matter(z=0) of fiducial LambdaCDM cosmology'))

    parser.add_argument('--no-project', action='store_true', required=False,
                        help='Do not project out continuum fitting modes')

    parser.add_argument('--nside', type=int, default=16, required=False,
                        help='Healpix nside')

    # parser.add_argument('--nproc', type=int, default=None, required=False,
    #                     help='Number of processors')

    parser.add_argument('--nspec', type=int, default=None, required=False,
                        help='Maximum number of spectra to read')

    parser.add_argument('--rebin-factor', type=int, default=None, required=False,
                        help='Rebin factor for deltas. If not None, deltas will '
                             'be rebinned by that factor')

    args = parser.parse_args()

    settings = {'rp-min': args.rp_min, 'rp-max': args.rp_max,
                'rt-min': args.rt_min, 'rt-max': args.rt_max,
                'num-rp': args.num_rp, 'num-rt': args.num_rt,
                'z-cut-min': args.z_cut_min, 'z-cut-max': args.z_cut_max,
                'z-ref': args.z_ref, 'z-evol': args.z_evol, 'fid-Om': args.fid_Om,
                'no-project': args.no_project, 'nside': args.nside, 'nspec': args.nspec,
                'rebin-factor': args.rebin_factor}

    lya2pt = Lya2pt(args.out, args.in_dir, args.in_dir2, settings)
