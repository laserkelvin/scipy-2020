
import pandas as pd
from matplotlib import pyplot as plt
plt.style.use("dark_presentation")

data = pd.read_csv("sgrb2_data.tsv", delim_whitespace=True, comment="#")
data.columns = ["Frequency", "Temperature"]
# data["Frequency"] *= 1e3

fig, axarray = plt.subplots(2, 1, figsize=(8, 6))

ax = axarray[0]

ax.plot(data["Frequency"], data["Temperature"], lw=0.5, alpha=0.8, color="w")

for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)
    
ax.set(xlabel="Frequency (GHz)", ylabel="Temperature (K)", xlim=[80, 116], ylim=[-0.5, 20.])
ax.set_xlabel("Frequency (GHz)")

ax = axarray[1]

ax.plot(data["Frequency"], data["Temperature"], lw=0.5, alpha=0.8, color="w")
ax.set(
    xlabel="Frequency (GHz)", 
    ylabel="Temperature (K)", 
    xlim=[90, 92], 
    ylim=[-0.5, 7.5],
    xticks=[90, 90.5, 91, 91.5, 92.],
    yticks=[0., 2.5, 5, 7.5],
    )

for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

fig.tight_layout()

fig.savefig("../figures/sgrb2n_spectrum.svg", transparent=True)