
import numpy as np
from matplotlib import pyplot as plt

plt.style.use("dark_presentation")

def gaussian(x, A, x0, sigma):
    return A * np.exp(-(x - x0)**2. / (2 * sigma**2.))


def draw_plot(x, y):
    fig, ax = plt.subplots(figsize=(10, 2))

    ax.plot(x, y,) #color="#3a5ca7", alpha=0.8)

    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.set_xticks([])
    ax.set_yticks([])
    return fig, ax

np.random.seed(30)

x = np.linspace(0., 20., 10000)

y = np.zeros(x.size)

centers = np.random.rand(6) * 20.
amplitudes = np.random.rand(6)
widths = np.random.rand(6) + 0.3

for center, amp, width in zip(centers, amplitudes, widths):
    y += gaussian(x, amp, center, width)

y += np.random.normal(scale=0.05, size=y.size)

fig, ax = draw_plot(x, y)

fig.savefig("dsp_spectrum.svg", transparent=True)

y += (-0.3 * x + 0.3) + np.sin(x)

fig, ax = draw_plot(x, y)

fig.savefig("raw_spectrum.svg", transparent=True)
