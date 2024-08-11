import numpy as np


def pca(x):
    cov_matrix = np.cov(x, rowvar=False)
    v, e = np.linalg.eig(cov_matrix)
    return v, e


N = 1000

x_0 = np.random.normal(0, 100, N)
x_1 = 2 * x_0 + np.random.normal(0, 20, N)
x = np.column_stack((x_0, x_1))

principal_val, principal_vec = pca(x)
x_proj = x @ principal_vec[0]
print(x_proj)
