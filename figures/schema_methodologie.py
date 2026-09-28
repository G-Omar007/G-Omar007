"""Schéma de la chaîne de traitement (Pléiades 2015/2020 – SuperView Neo-1 2024).

Produit schema_methodologie.png (300 dpi), .svg et .pdf dans le même dossier.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle

plt.rcParams["font.family"] = "DejaVu Sans"

# Palette : (bordure, bandeau de titre, fond)
STYLES = {
    "data": ("#3B6EA8", "#D6E4F5", "#F4F8FD"),
    "catalyst": ("#C7772B", "#F9DDBF", "#FEF7EE"),
    "python": ("#3E8E4F", "#D3EBD7", "#F2F9F3"),
    "result": ("#7E4A9E", "#E6D5F0", "#F9F4FC"),
    "valid": ("#A88A10", "#F6E9A8", "#FFFBE8"),
}
LEGEND = [
    ("data", "Données"),
    ("catalyst", "CATALYST Professional"),
    ("python", "Python (scripts)"),
    ("result", "Résultats"),
    ("valid", "Validation / interprétation"),
]
INK = "#1F2328"
MUTED = "#4A5360"
ARROW = "#5B6573"

W, H = 100, 142
X0, X1 = 15, 98  # zone utile des boîtes
GAP = 3
COL_W = (X1 - X0 - 2 * GAP) / 3
COLS = [X0 + i * (COL_W + GAP) for i in range(3)]
HEADER_H = 4.2

fig, ax = plt.subplots(figsize=(10, 14.2))
ax.set_xlim(0, W)
ax.set_ylim(0, H)
ax.set_aspect("equal")
ax.axis("off")
fig.subplots_adjust(0, 0, 1, 1)


def box(x, y_top, w, h, kind, title, body, body_size=8.2):
    """Boîte arrondie avec bandeau de titre coloré. Retourne (cx, top, bottom)."""
    edge, head, fill = STYLES[kind]
    y = y_top - h
    outline = FancyBboxPatch(
        (x, y), w, h, boxstyle="round,pad=0,rounding_size=1.4",
        fc=fill, ec=edge, lw=1.4, zorder=3,
    )
    ax.add_patch(outline)
    band = Rectangle((x, y_top - HEADER_H), w, HEADER_H, fc=head, ec="none", zorder=3.1)
    band.set_clip_path(outline)
    ax.add_patch(band)
    ax.plot([x, x + w], [y_top - HEADER_H] * 2, color=edge, lw=0.8, alpha=0.6, zorder=3.2)
    ax.text(x + w / 2, y_top - HEADER_H / 2, title, ha="center", va="center",
            fontsize=10.5, fontweight="bold", color=INK, zorder=4)
    ax.text(x + w / 2, y + (h - HEADER_H) / 2, body, ha="center", va="center",
            fontsize=body_size, color=MUTED, linespacing=1.55, zorder=4)
    return x + w / 2, y_top, y


def arrow(x0, y0, x1, y1):
    ax.annotate("", xy=(x1, y1), xytext=(x0, y0), zorder=2,
                arrowprops=dict(arrowstyle="-|>,head_length=0.55,head_width=0.28",
                                color=ARROW, lw=1.3, shrinkA=0, shrinkB=0.5))


def line(xs, ys):
    ax.plot(xs, ys, color=ARROW, lw=1.3, solid_capstyle="round", zorder=2)


def lane(y_top, y_bot, label, shaded):
    if shaded:
        ax.add_patch(Rectangle((1, y_bot), W - 2, y_top - y_bot, fc="#F3F5F8",
                               ec="none", zorder=0))
    ax.add_patch(Rectangle((1, y_bot), 1.0, y_top - y_bot, fc="#AEB6C2", ec="none", zorder=1))
    ax.text(7.5, (y_top + y_bot) / 2, label, rotation=90, ha="center", va="center",
            fontsize=10, fontweight="bold", color="#5A6472")


# --- Titre et légende --------------------------------------------------------
ax.text(W / 2, 139, "Chaîne de traitement méthodologique", ha="center", va="center",
        fontsize=15, fontweight="bold", color=INK)
ax.text(W / 2, 135.6, "Pléiades 1A (2015, 2020) et SuperView Neo-1 (2024) · zone d'étude ≈ 101 ha",
        ha="center", va="center", fontsize=9.5, color=MUTED, style="italic")

# Largeur réelle de chaque étiquette, mesurée en unités de données
renderer = fig.canvas.get_renderer()
units_per_px = W / ax.get_window_extent(renderer).width
items = []
for kind, label in LEGEND:
    t = ax.text(0, 0, label, fontsize=8.6)
    items.append((kind, label, t.get_window_extent(renderer).width * units_per_px))
    t.remove()
SWATCH, PAD, SEP = 2.6, 1.0, 4.0
total = sum(SWATCH + PAD + w for *_, w in items) + SEP * (len(items) - 1)
lx = (W - total) / 2
for kind, label, tw in items:
    edge, head, _ = STYLES[kind]
    ax.add_patch(FancyBboxPatch((lx, 130.6), SWATCH, 1.8,
                                boxstyle="round,pad=0,rounding_size=0.4",
                                fc=head, ec=edge, lw=1.1))
    ax.text(lx + SWATCH + PAD, 131.5, label, va="center", fontsize=8.6, color=INK)
    lx += SWATCH + PAD + tw + SEP

# --- Bandes de phase ---------------------------------------------------------
lane(128.5, 110.5, "DONNÉES", True)
lane(110.5, 55.3, "PRÉTRAITEMENT", False)
lane(55.3, 38.5, "ANALYSES", True)
lane(38.5, 21.5, "RÉSULTATS", False)
lane(21.5, 3.5, "SYNTHÈSE", True)

# --- Données -----------------------------------------------------------------
data = [
    ("Pléiades 1A · 2015", "8 juillet · MS 2 m\n8 bits · géométrie capteur"),
    ("Pléiades 1A · 2020", "27 juillet · MS 2 m\n8 bits · géométrie capteur"),
    ("SuperView Neo-1 · 2024", "7 juillet · MS 1,2 m\n11 bits · L2A (UTM 18N)"),
]
data_boxes = [box(x, 126.5, COL_W, 14, "data", t, b, 8.6) for x, (t, b) in zip(COLS, data)]

# --- Prétraitement -----------------------------------------------------------
full_w = X1 - X0
cx = X0 + full_w / 2
_, atcor_top, atcor_bot = box(
    X0, 105.5, full_w, 14.5, "catalyst",
    "①  Correction atmosphérique — ATCOR (CATALYST Professional)",
    "MASKING (voile, nuages, saturation)  →  HAZEREM (suppression du voile, 50 %)  →  ATCOR (réflectance au sol)\n"
    "Été subarctique · visibilité 5 km (2015), 80 km (2020), 40 km (2024)\n"
    "Profil SuperView-1 + gains CRESDA (2024)",
)
for bx, _, bb in data_boxes:
    arrow(bx, bb, bx, atcor_top)

_, geo_top, geo_bot = box(
    X0, 87.0, full_w, 12, "python",
    "②  Géométrie (Python — rasterio / GDAL)",
    "Orthorectification des images Pléiades : modèle RPC + MNT Copernicus GLO-30\n"
    "Grille commune UTM 18N à 2 m (SuperView agrégé 1,2 → 2 m) · co-recalage sur 2024 (corrélation de phase)",
)
arrow(cx, atcor_bot, cx, geo_top)

_, norm_top, norm_bot = box(
    X0, 71.0, full_w, 12, "python",
    "③  Normalisation radiométrique relative (Python)",
    "IR-MAD : pixels invariants 2015→2020 et 2024→2020 · régression orthogonale par bande\n"
    "Correction de la tendance spatiale du voile (σ = 300 m) · validation sur pixels invariants indépendants",
)
arrow(cx, geo_bot, cx, norm_top)

# --- Répartition vers les analyses (bus + étiquette) -------------------------
bus_y = 54.6
analyses_top = 52.5
col_cx = [x + COL_W / 2 for x in COLS]
line([cx, cx], [norm_bot, bus_y])
line([col_cx[0], col_cx[2]], [bus_y, bus_y])
for c in col_cx:
    arrow(c, bus_y, c, analyses_top)
ax.text(cx, (norm_bot + bus_y) / 2 + 0.3, "Réflectances au sol comparables",
        ha="center", va="center", fontsize=8.6, style="italic", color=INK, zorder=5,
        bbox=dict(boxstyle="round,pad=0.35,rounding_size=0.8", fc="white", ec="#AEB6C2", lw=0.9))

# --- Analyses ----------------------------------------------------------------
analyses = [
    ("④a  Histogrammes", "Réflectance par bande\net par date,\navant et après normalisation"),
    ("④b  NDVI", "5 intervalles (mêmes seuils)\nΔNDVI (|Δ| > 0,10)\nTransitions entre classes"),
    ("④c  Classification", "K-means multidate (12 grappes)\n→ 7 classes thématiques\nMatrices de transition"),
]
an_boxes = [box(x, analyses_top, COL_W, 12.5, "python", t, b)
            for x, (t, b) in zip(COLS, analyses)]

# --- Résultats ---------------------------------------------------------------
results = [
    ("Comparabilité", "Distributions superposées\ndes 3 dates"),
    ("Dynamique du couvert", "Cartes NDVI et ΔNDVI\nSuperficies par classe"),
    ("Changements du milieu", "Cartes des classes\nTrajectoires (thermokarst,\nfermeture du couvert)"),
]
res_boxes = [box(x, 36.0, COL_W, 12.5, "result", t, b) for x, (t, b) in zip(COLS, results)]
for (ax_, _, ab), (_, rt, _) in zip(an_boxes, res_boxes):
    arrow(ax_, ab, ax_, rt)

# --- Validation --------------------------------------------------------------
val_top = 18.5
_, _, _ = box(
    X0, val_top, full_w, 13, "valid",
    "⑤  Validation et interprétation",
    "Photo-interprétation de 630 points (matrices de confusion, kappa) · données climatiques ECCC (phénologie)\n"
    "Discussion : dégel du pergélisol, expansion arbustive, limites et recommandations",
)
merge_y = 20.9
for rx, _, rb in res_boxes:
    line([rx, rx], [rb, merge_y])
line([col_cx[0], col_cx[2]], [merge_y, merge_y])
arrow(cx, merge_y, cx, val_top)

out = Path(__file__).with_suffix("")
for ext in ("png", "svg", "pdf"):
    fig.savefig(f"{out}.{ext}", dpi=300, facecolor="white")
print("OK")
