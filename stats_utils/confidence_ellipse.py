import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import matplotlib.transforms as transforms


def confidence_ellipse(x, y, ax, n_std=3.0, facecolor='none', **kwargs):
    if x.size != y.size:
        raise ValueError("x and y must be the same size")

    cov = np.cov(x, y)
    lambda_, v = np.linalg.eig(cov)

    angle = np.rad2deg(np.arccos(v[0, 0]))  #

    ell_radius_x = np.sqrt(n_std * lambda_[0])
    ell_radius_y = np.sqrt(n_std * lambda_[1])

    mean_x, mean_y = np.mean(x), np.mean(y)
    ellipse = Ellipse((mean_x, mean_y),
                      width=ell_radius_x * 2,
                      height=ell_radius_y * 2,
                      facecolor=facecolor,
                      angle=angle,
                      **kwargs)

    return ax.add_patch(ellipse)
