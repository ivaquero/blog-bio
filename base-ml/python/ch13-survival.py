import matplotlib.pyplot as plt
import numpy as np
from lifelines.plotting import plot_lifetimes
from scipy import stats

np.set_printoptions(precision=2)
N = 20
study_duration = 12

func1 = stats.expon(scale=18)
func2 = stats.expon(scale=3)
func3 = stats.uniform()

actual_subs = np.array([
    [func1.rvs(), func2.rvs()][func3.rvs() < 0.5] for _ in range(N)
])
observed_subs = np.minimum(actual_subs, study_duration)
observed = actual_subs < study_duration

plt.xlim(0, 24)
plt.vlines(12, 0, 30, lw=1.5, linestyles="--")
plt.xlabel("time")
plt.title("Subscription Times, at $t=12$  months")
plot_lifetimes(observed_subs, event_observed=observed)
# plt.savefig('../../images/ch18/survival.png')
plt.show()
