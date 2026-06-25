import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(12, 6))

ax.set_xlim(0, 12)
ax.set_ylim(0, 8)

ax.axis("off")

# --------------------------------------------------
# Boxen
# --------------------------------------------------

boxes = {
    "State\n$s_t$": (1, 5),
    "Agent\n(Hedger)": (4, 5),
    "Action\n$a_t$": (7, 5),
    "Environment\n(Markt)": (10, 5),
    "Reward\n$r_t$": (10, 2),
    "Next State\n$s_{t+1}$": (4, 2)
}

for text, (x, y) in boxes.items():
    ax.text(
        x,
        y,
        text,
        ha="center",
        va="center",
        fontsize=12,
        bbox=dict(
            boxstyle="round,pad=0.5",
            edgecolor="black",
            facecolor="white"
        )
    )

# --------------------------------------------------
# Pfeile
# --------------------------------------------------

arrow = dict(arrowstyle="->", lw=2)

ax.annotate("", xy=(3.2, 5), xytext=(1.8, 5), arrowprops=arrow)
ax.annotate("", xy=(6.2, 5), xytext=(4.8, 5), arrowprops=arrow)
ax.annotate("", xy=(9.2, 5), xytext=(7.8, 5), arrowprops=arrow)

ax.annotate("", xy=(10, 2.7), xytext=(10, 4.3), arrowprops=arrow)

ax.annotate("", xy=(4.8, 2), xytext=(9.2, 2), arrowprops=arrow)

ax.annotate("", xy=(1.4, 4.4), xytext=(3.6, 2.6), arrowprops=arrow)

# --------------------------------------------------
# Zusätzliche Beschriftungen
# --------------------------------------------------

ax.text(
    1,
    6.3,
    "Marktpreise\nPortfolio\nZeit",
    fontsize=10,
    ha="center"
)

ax.text(
    7,
    6.3,
    "Kaufen / Verkaufen",
    fontsize=10,
    ha="center"
)

ax.text(
    10,
    0.8,
    "Gewinn / Verlust",
    fontsize=10,
    ha="center"
)

# --------------------------------------------------
# Titel
# --------------------------------------------------

plt.title(
    "Markov Decision Process für Deep Hedging",
    fontsize=16,
    pad=20
)

plt.tight_layout()

plt.savefig(
    "figure_13_mdp_hedging.png",
    dpi=300,
    bbox_inches="tight"
)

plt.savefig(
    "figure_13_mdp_hedging.pdf",
    bbox_inches="tight"
)

plt.show()
