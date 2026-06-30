import matplotlib.pyplot as plt

# Figure
fig, ax = plt.subplots(figsize=(7, 10))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis("off")

steps = [
    "Simulierte\nPreiswege",
    "Neuronales Netz\n(Policy)",
    "Hedging-\nEntscheidungen",
    "Portfolio-\nentwicklung",
    "Berechnung des\nRisikomaßes\n(CVaR)",
    "Gradienten-\nberechnung\n(Backpropagation)",
    "Aktualisierung der\nNetzwerkparameter\n(Adam)"
]

# y-Positionen
ys = [0.92, 0.79, 0.66, 0.53, 0.40, 0.25, 0.10]

# Kästen zeichnen
for y, step in zip(ys, steps):
    ax.text(
        0.5, y, step,
        ha="center", va="center",
        fontsize=13,
        bbox=dict(boxstyle="round,pad=0.4",
                  edgecolor="black",
                  facecolor="#E8F1FA")
    )

# Pfeile
for i in range(len(ys)-1):
    ax.annotate(
        "",
        xy=(0.5, ys[i+1]+0.04),
        xytext=(0.5, ys[i]-0.04),
        arrowprops=dict(arrowstyle="->", lw=2)
    )

# Rückkopplungsschleife
ax.annotate(
    "",
    xy=(0.84, ys[0]),
    xytext=(0.84, ys[-1]),
    arrowprops=dict(arrowstyle="->", lw=2)
)

ax.plot([0.50,0.84],[ys[0],ys[0]],lw=2)
ax.plot([0.50,0.84],[ys[-1],ys[-1]],lw=2)

ax.text(
    0.87,
    0.50,
    "Nächster\nTrainingsdurchlauf",
    fontsize=12,
    rotation=90,
    va="center"
)

plt.tight_layout()
plt.show()
