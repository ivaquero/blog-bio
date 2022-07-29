import numpy as np
from stats_utils.record_rnd import *


def rnd_replace_with_const(n_groups,
                           n_samples,
                           constant=0,
                           col_ind=0,
                           sort=-1,
                           seed=None,
                           record=None):
    if seed:
        np.random.seed(seed)
    rnd_matrix = np.random.rand(n_groups, n_samples)
    if sort:
        rnd_matrix.sort(axis=sort)

    the_col = np.ones(n_groups) * constant
    rnd_matrix[:, col_ind] = the_col

    if record == 'time':
        record_by_time(rnd_2d_from.__name__, n_groups, output)

    return rnd_matrix
