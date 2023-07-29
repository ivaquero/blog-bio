import numpy as np


def pca(X):
    cov_matrix = np.cov(X, rowvar=False)
    v, e = np.linalg.eig(cov_matrix)
    return v, e


N = 1000

x_0 = np.random.normal(0, 100, N)
x_1 = 2 * x_0 + np.random.normal(0, 20, N)
X = np.column_stack((x_0, x_1))

principal_val, principal_vec = pca(X)
X_proj = np.dot(X, principal_vec[0])
print(X_proj)
