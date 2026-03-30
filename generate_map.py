import matplotlib.pyplot as plt

# Approximate city-center coordinates used as plotting proxies when branch coordinates
# are not publicly published in reviewed pages.
# tuple schema: (longitude, latitude, label, bank)
points = [
    (35.3035, 32.6061, "Afula", "Discount"),
    (35.2137, 31.7683, "Jerusalem", "Discount"),
    (34.7818, 32.0853, "Tel Aviv-Yafo", "Discount"),
    (34.9732, 32.3226, "Kalansuwa", "Leumi"),
    (34.8729, 31.9316, "Ramla", "Leumi"),
    (35.2137, 31.7683, "Jerusalem Romema", "Bank of Jerusalem"),
    (34.7818, 32.0853, "Tel Aviv", "Bank of Jerusalem"),
    (35.3035, 32.6061, "Afula", "FIBI"),
    (34.6553, 31.8014, "Ashdod", "FIBI"),
]

brand_colors = {
    "Discount": "#1f9d55",          # green
    "Leumi": "#5bc0eb",             # light blue
    "Bank of Jerusalem": "#f4a261", # orange
    "FIBI": "#264653",              # dark blue
}

fig, ax = plt.subplots(figsize=(7, 10))

# Simplified geographic frame for Israel.
ax.set_xlim(34.2, 35.9)
ax.set_ylim(29.4, 33.4)
ax.set_title("Israel Bank Service Points Map (from reviewed public sources)")
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")
ax.grid(alpha=0.25)

for lon, lat, _label, bank in points:
    ax.scatter(lon, lat, c=brand_colors[bank], s=65, edgecolor="black", linewidth=0.4)

# Legend handles
for bank, color in brand_colors.items():
    ax.scatter([], [], c=color, s=65, edgecolor="black", linewidth=0.4, label=bank)

ax.legend(loc="lower left", frameon=True)
plt.tight_layout()

# Use SVG (text-based) to avoid binary-file limitations in some environments.
output_file = "israel_bank_service_points_map.svg"
plt.savefig(output_file, format="svg")
print(f"saved {output_file}")
