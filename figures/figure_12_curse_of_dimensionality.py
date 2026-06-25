import numpy as np
import matplotlib.pyplot as plt

# Anzahl Zustandsvariablen

dimensions = np.arange(1, 8)

# 100 Diskretisierungspunkte pro Dimension

grid_points = 100 ** dimensions

# Grafik

plt.figure(figsize=(10, 6))

plt.plot(
    dimensions,
    grid_points,
    marker="o",
    linewidth=3
)

plt.yscale("log")

plt.xlabel("Anzahl der Zustandsvariablen")

plt.ylabel("Anzahl der Gitterpunkte (log-Skala)")

plt.title("Fluch der Dimensionalität")

plt.grid(True)

# Werte beschriften

for x, y in zip(dimensions, grid_points):
    plt.annotate(
        f"{y:.0e}",
        (x, y),
        textcoords="offset points",
        xytext=(0, 8),
        ha="center"
    )

plt.tight_layout()

plt.savefig(
    "figure_12_curse_of_dimensionality.png",
    dpi=300
)

plt.savefig(
    "figure_12_curse_of_dimensionality.pdf"
)

plt.show()
