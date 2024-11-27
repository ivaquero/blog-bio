import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import MaxAbsScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import Normalizer
from sklearn.preprocessing import RobustScaler
from sklearn.preprocessing import StandardScaler

rng = np.random.default_rng(42)
height = rng.normal(loc=175, scale=5, size=1000).reshape(-1, 1)
weight = rng.normal(loc=60, scale=10, size=1000).reshape(-1, 1)

test_arr = np.concatenate((height, weight), axis=1)

std_sca = StandardScaler()
mm_sca = MinMaxScaler()
ma_sca = MaxAbsScaler()
nor_sca = Normalizer()
rbt_sca = RobustScaler()

test_nor = nor_sca.fit_transform(test_arr)
test_ma = ma_sca.fit_transform(test_arr)
test_mm = mm_sca.fit_transform(test_arr)
test_std = std_sca.fit_transform(test_arr)
test_rbt = rbt_sca.fit_transform(test_arr)

_, axes = plt.subplots(3, 2, figsize=(10, 8), constrained_layout=True)

titles = [
    "Original Array",
    "After Unit Normalization",
    "After Min-Max Normalization",
    "After Max-Abs Normalization",
    "After Standardization",
    "After Robust Normalization",
]

for (ind, array), ax in zip(
    enumerate([test_arr, test_nor, test_mm, test_ma, test_std, test_rbt]),
    axes.flatten(),
):
    ax.hist(array[:, 0:1], bins=50, alpha=0.8, label="height")
    ax.hist(array[:, 1:2], bins=50, alpha=0.8, label="weight")

    ax.set(title=f"{titles[ind]}")

# plt.savefig('../../images/ch08/scaling.png')
plt.show()
