import matplotlib.pyplot as plt
from lifelines import KaplanMeierFitter
from lifelines.datasets import load_waltons

df = load_waltons()

T = df["T"]
E = df["E"]
groups = df["group"]
ix = groups == "miR-137"

kmf = KaplanMeierFitter()

fig, ax = plt.subplots(1, 1)

kmf.fit(T[~ix], E[~ix], label="control")
kmf.plot(ax=ax)
kmf.fit(T[ix], E[ix], label="miR-137")
kmf.plot(ax=ax)

plt.ylabel("Survival Probability")
# plt.savefig('../../images/ch18/kaplan_meier.png')
plt.show()
