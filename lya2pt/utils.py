import numpy as np
from numpy.typing import ArrayLike


def project_forest(wave: ArrayLike, delta: ArrayLike, weights: ArrayLike) -> ArrayLike:
    """Project the delta field. See equations 5 and 6 of du Mas des Bourboux et al. 2020
    """
    # 2nd term in equation 6
    sum_weights = np.sum(weights)
    if sum_weights > 0.0:
        mean_delta = np.average(delta, weights=weights)
    else:
        return delta

    log_wave = np.log10(wave)

    # 3rd term in equation 6
    mean_log_lambda = np.average(log_wave, weights=weights)
    meanless_log_lambda = log_wave - mean_log_lambda
    mean_delta_log_lambda = (np.sum(weights * delta * meanless_log_lambda) /
                             np.sum(weights * meanless_log_lambda**2))

    return delta - mean_delta - mean_delta_log_lambda * meanless_log_lambda


def rebin_forest(wave: ArrayLike, delta: ArrayLike, weights: ArrayLike,
                 factor: int) -> tuple[ArrayLike, ArrayLike, ArrayLike]:
    dwave = wave[1] - wave[0]
    if not np.isclose(dwave, wave[-1] - wave[-2]):
        raise ValueError('Delta rebinning only implemented for linear lambda bins')

    start = wave.min() - dwave / 2
    num_bins = np.ceil(((wave[-1] - wave[0]) / dwave + 1) / factor)

    edges = np.arange(num_bins) * dwave * factor + start

    new_indx = np.searchsorted(edges, wave)

    binned_delta = np.bincount(new_indx, weights=delta*weights, minlength=edges.size+1)[1:-1]
    binned_weight = np.bincount(new_indx, weights=weights, minlength=edges.size+1)[1:-1]

    mask = binned_weight != 0
    binned_delta[mask] /= binned_weight[mask]

    new_wave = (edges[1:] + edges[:-1]) / 2

    return new_wave[mask], binned_delta[mask], binned_weight[mask]
