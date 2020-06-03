
import pandas as pd
from matplotlib import pyplot as plt
plt.style.use("dark_presentation")

data = pd.read_csv("sgrb2_data.tsv", delim_whitespace=True, comment="#")
data.columns = ["Frequency", "Temperature"]
data.sort_values("Frequency", inplace=True)
# data["Frequency"] *= 1e3

fig, ax = plt.subplots(figsize=(8, 5))

ax.plot(data["Frequency"], data["Temperature"], lw=0.5, alpha=0.8, color="#f03b20")

for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

ax.axvspan(96. - 1, 96 + 1, alpha=0.4, color="k")
ax.axvspan(96. - 4, 96 + 4, alpha=0.4, color="r")
ax.axvspan(96. - 32, 96 + 32, alpha=0.4, color="blue")

fig.tight_layout()

fig.savefig("../figures/sgrb2n_spectrum.svg", transparent=True)
