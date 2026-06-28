import matplotlib.pyplot as plt

# ----------------------------------------------------------
# Figure
# ----------------------------------------------------------

fig, ax = plt.subplots(figsize=(15,4))

ax.set_xlim(0,10)
ax.set_ylim(-1.8,2)

ax.axis("off")

# ----------------------------------------------------------
# Timeline
# ----------------------------------------------------------

ax.plot([0.8,9.2],[0,0],linewidth=3)

times=["$t_0$","$t_1$","$t_2$","...","$T$"]
x=[1,3,5,7,9]

for xi,label in zip(x,times):

    ax.scatter(xi,0,s=80)

    ax.text(
        xi,
        -0.35,
        label,
        ha="center",
        fontsize=13
    )

# ----------------------------------------------------------
# Events
# ----------------------------------------------------------

events=[

"Observe\nState\n$s_0$",

"Policy\n$a_1=\\pi_\\theta(s_1)$",

"Portfolio\nUpdate",

"Repeat",

"Terminal\nPortfolio\n$X_T$"

]

for xi,event in zip(x,events):

    ax.annotate(
        "",
        xy=(xi,0.05),
        xytext=(xi,0.85),
        arrowprops=dict(
            arrowstyle="->",
            linewidth=1.8
        )
    )

    ax.text(
        xi,
        1.05,
        event,
        ha="center",
        fontsize=11
    )

# ----------------------------------------------------------
# Bottom explanation
# ----------------------------------------------------------

bottom=[

"Market\nObservation",

"Hedge\nDecision",

"Trading",

"Rebalancing",

"Risk\nEvaluation"

]

for xi,text in zip(x,bottom):

    ax.text(
        xi,
        -1.15,
        text,
        ha="center",
        fontsize=10
    )

# ----------------------------------------------------------
# Transition arrows
# ----------------------------------------------------------

for i in range(len(x)-1):

    ax.annotate(
        "",
        xy=(x[i+1]-0.25,-0.75),
        xytext=(x[i]+0.25,-0.75),
        arrowprops=dict(
            arrowstyle="->",
            linewidth=1.5,
            linestyle="dashed"
        )
    )

# ----------------------------------------------------------
# Title
# ----------------------------------------------------------

plt.title(
    "Trading Timeline in Deep Hedging",
    fontsize=18,
    pad=20
)

plt.tight_layout()

plt.savefig(
    "figure_18_trading_timeline.png",
    dpi=300,
    bbox_inches="tight"
)

plt.savefig(
    "figure_18_trading_timeline.pdf",
    bbox_inches="tight"
)

plt.show()
