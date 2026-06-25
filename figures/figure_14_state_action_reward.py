import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(12, 5))

ax.set_xlim(0, 12)
ax.set_ylim(0, 4)

ax.axis("off")

# --------------------------------------------------
# Boxen
# --------------------------------------------------

boxes = {
    "State\n$s_t$\n\nMarktzustand": (2, 2),
    "Action\n$a_t$\n\nHedge-Anpassung": (6, 2),
    "Reward\n$r_t$\n\nGewinn / Verlust": (10, 2)
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
            boxstyle="round,pad=0.6",
            facecolor="white",
            edgecolor="black"
        )
    )

# --------------------------------------------------
# Pfeile
# --------------------------------------------------

arrow = dict(
    arrowstyle="->",
    lw=2
)

ax.annotate(
    "",
    xy=(5, 2),
    xytext=(3, 2),
    arrowprops=arrow
)

ax.annotate(
    "",
    xy=(9, 2),
    xytext=(7, 2),
    arrowprops=arrow
)

# --------------------------------------------------
# Detailbeschriftungen
# --------------------------------------------------

ax.text(
    2,
    0.8,
    "$S_t$, $\\Delta_t$, $t$",
    fontsize=11,
    ha="center"
)

ax.text(
    6,
    0.8,
    "Kaufen / Verkaufen",
    fontsize=11,
    ha="center"
)

ax.text(
    10,
    0.8,
    "$r_t = -(L_t + \\lambda R_t)$",
    fontsize=11,
    ha="center"
)

# --------------------------------------------------
# Titel
# --------------------------------------------------

plt.title(
    "State, Action and Reward in Deep Hedging",
    fontsize=16,
    pad=20
)

plt.tight_layout()

plt.savefig(
    "figure_14_state_action_reward.png",
    dpi=300,
    bbox_inches="tight"
)

plt.savefig(
    "figure_14_state_action_reward.pdf",
    bbox_inches="tight"
)

plt.show()
