import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(10, 6))

ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

ax.axis("off")

# --------------------------------------------------
# Neuronenpositionen
# --------------------------------------------------

input_layer = [(2, y) for y in [2, 4, 6, 8]]

hidden_1 = [(5, y) for y in [1.5, 3.5, 5.5, 7.5, 9]]
hidden_2 = [(8, y) for y in [2.5, 5, 7.5]]

output_layer = [(11, 5)]

# --------------------------------------------------
# Verbindungen
# --------------------------------------------------

for x1, y1 in input_layer:
    for x2, y2 in hidden_1:
        ax.plot([x1, x2], [y1, y2], linewidth=0.7)

for x1, y1 in hidden_1:
    for x2, y2 in hidden_2:
        ax.plot([x1, x2], [y1, y2], linewidth=0.7)

for x1, y1 in hidden_2:
    for x2, y2 in output_layer:
        ax.plot([x1, x2], [y1, y2], linewidth=0.7)

# --------------------------------------------------
# Neuronen zeichnen
# --------------------------------------------------

def draw_layer(nodes):
    for x, y in nodes:
        circle = plt.Circle(
            (x, y),
            0.25,
            fill=False,
            linewidth=2
        )
        ax.add_patch(circle)

draw_layer(input_layer)
draw_layer(hidden_1)
draw_layer(hidden_2)
draw_layer(output_layer)

# --------------------------------------------------
# Beschriftungen
# --------------------------------------------------

ax.text(
    2,
    9.5,
    "Input Layer",
    ha="center",
    fontsize=12
)

ax.text(
    5,
    9.8,
    "Hidden Layer 1",
    ha="center",
    fontsize=12
)

ax.text(
    8,
    9.5,
    "Hidden Layer 2",
    ha="center",
    fontsize=12
)

ax.text(
    11,
    6.2,
    "Output",
    ha="center",
    fontsize=12
)

# --------------------------------------------------
# State und Action
# --------------------------------------------------

ax.text(
    0.3,
    5,
    r"$s_t$",
    fontsize=18
)

ax.arrow(
    0.8,
    5,
    0.8,
    0,
    length_includes_head=True,
    head_width=0.2
)

ax.text(
    11.6,
    5,
    r"$a_t$",
    fontsize=18
)

# --------------------------------------------------
# Titel
# --------------------------------------------------

plt.title(
    "Neural Network Policy Approximation",
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
