import matplotlib.pyplot as plt
from matplotlib.patches import Circle

fig, ax = plt.subplots(figsize=(12, 6))

ax.set_xlim(0, 12)
ax.set_ylim(0, 10)

ax.axis("off")

# --------------------------------------------------
# Layer Definition
# --------------------------------------------------

input_layer = [(2, y) for y in [2, 4, 6, 8]]

hidden_layer_1 = [(5, y) for y in [1.5, 3.5, 5.5, 7.5, 9]]

hidden_layer_2 = [(8, y) for y in [2.5, 5, 7.5]]

output_layer = [(11, 5)]

# --------------------------------------------------
# Connections
# --------------------------------------------------

for x1, y1 in input_layer:
    for x2, y2 in hidden_layer_1:
        ax.plot([x1, x2], [y1, y2], linewidth=0.8)

for x1, y1 in hidden_layer_1:
    for x2, y2 in hidden_layer_2:
        ax.plot([x1, x2], [y1, y2], linewidth=0.8)

for x1, y1 in hidden_layer_2:
    for x2, y2 in output_layer:
        ax.plot([x1, x2], [y1, y2], linewidth=0.8)

# --------------------------------------------------
# Draw Nodes
# --------------------------------------------------

def draw_nodes(nodes):
    for x, y in nodes:
        ax.add_patch(
            Circle(
                (x, y),
                radius=0.22,
                fill=False,
                linewidth=2
            )
        )

draw_nodes(input_layer)
draw_nodes(hidden_layer_1)
draw_nodes(hidden_layer_2)
draw_nodes(output_layer)

# --------------------------------------------------
# Input Labels
# --------------------------------------------------

input_labels = [
    "ATX",
    "OMV",
    "EBS",
    "VER"
]

for (x, y), label in zip(input_layer, input_labels):
    ax.text(
        x - 1.2,
        y,
        label,
        fontsize=11,
        va="center"
    )

# --------------------------------------------------
# Network Labels
# --------------------------------------------------

ax.text(
    5,
    9.8,
    "Hidden Layer 1",
    ha="center",
    fontsize=11
)

ax.text(
    8,
    9.8,
    "Hidden Layer 2",
    ha="center",
    fontsize=11
)

# --------------------------------------------------
# State
# --------------------------------------------------

ax.text(
    0.5,
    9,
    r"$s_t$",
    fontsize=18
)

ax.text(
    0.3,
    8.2,
    "Market State",
    fontsize=11
)

# --------------------------------------------------
# Output
# --------------------------------------------------

ax.text(
    11.6,
    5,
    r"$a_t$",
    fontsize=18
)

ax.text(
    11.5,
    4.1,
    "Hedge Position",
    fontsize=11
)

# --------------------------------------------------
# Formula
# --------------------------------------------------

ax.text(
    6,
    0.6,
    r"$a_t = \pi_\theta(s_t)$",
    fontsize=18,
    ha="center"
)

# --------------------------------------------------
# Title
# --------------------------------------------------

plt.title(
    "Neural Network Approximation of the Hedging Policy",
    fontsize=16,
    pad=20
)

plt.tight_layout()

plt.savefig(
    "figure_16_why_neural_networks.png",
    dpi=300,
    bbox_inches="tight"
)

plt.savefig(
    "figure_16_why_neural_networks.pdf",
    bbox_inches="tight"
)

plt.show()
