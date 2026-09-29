"""Schéma de la chaîne de traitement (Pléiades 2015/2020 – SuperView Neo-1 2024).

Produit schema_methodologie.png (300 dpi), .svg et .pdf dans le même dossier.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyBboxPatch, Rectangle

plt.rcParams["font.family"] = "DejaVu Sans"

# Palette : (bordure, bandeau de titre, fond)
STYLES = {
    "data": ("#2F63A0", "#D6E4F5", "#F4F8FD"),
    "catalyst": ("#C06A1E", "#F9DDBF", "#FEF7EE"),
    "python": ("#2F8043", "#D3EBD7", "#F2F9F3"),
    "result": ("#743F95", "#E6D5F0", "#F9F4FC"),
    "valid": ("#9C7F0C", "#F6E9A8", "#FFFBE8"),
}
LEGEND = [
    ("data", "Données"),
    ("catalyst", "CATALYST Professional"),
    ("python", "Python (scripts)"),
    ("result", "Résultats"),
    ("valid", "Validation"),
]
INK = "#1A1D21"
BODY = "#343B45"
ARROW = "#4F5967"

# Tailles de police (pt)
F_TITLE, F_BODY, F_LANE, F_LEGEND = 13.5, 11, 12, 11

W = 100
X0, X1 = 12.5, 99  # zone utile des boîtes
GAP = 2.5
COL_W = (X1 - X0 - 2 * GAP) / 3
COLS = [X0 + i * (COL_W + GAP) for i in range(3)]
COL_CX = [x + COL_W / 2 for x in COLS]
FULL_W = X1 - X0
CX = X0 + FULL_W / 2
HEADER_H = 5.0
LINE_H = 2.35  # hauteur d'une ligne de corps de texte (unités)
PAD_V = 3.4


def height(*bodies):
    return HEADER_H + max(b.count("\n") + 1 for b in bodies) * LINE_H + PAD_V


# --- Contenu -----------------------------------------------------------------
DATA = [
    ("Pléiades 1A · 2015", "Acquisition : 8 juillet\nMultispectral 2 m · 8 bits\nGéométrie capteur"),
    ("Pléiades 1A · 2020", "Acquisition : 27 juillet\nMultispectral 2 m · 8 bits\nGéométrie capteur"),
    ("SuperView Neo-1 · 2024", "Acquisition : 7 juillet\nMultispectral 1,2 m · 11 bits\nNiveau L2A (UTM 18N)"),
]
ATCOR = (
    "1", "Correction atmosphérique — ATCOR (CATALYST Professional)",
    "MASKING : masques du voile, des nuages et des pixels saturés\n"
    "HAZEREM : retrait du voile atmosphérique (50 %)  →  ATCOR : réflectance au sol\n"
    "Modèle été subarctique · visibilité 5 km (2015), 80 km (2020), 40 km (2024)\n"
    "SuperView Neo-1 : profil spectral SuperView-1 et gains d'étalonnage CRESDA",
)
GEOM = (
    "2", "Correction géométrique (Python — rasterio / GDAL)",
    "Orthorectification Pléiades : modèle RPC + MNT Copernicus GLO-30\n"
    "Grille commune UTM 18N à 2 m (SuperView rééchantillonné de 1,2 à 2 m)\n"
    "Co-recalage sur l'image 2024 par corrélation de phase",
)
NORM = (
    "3", "Normalisation radiométrique relative (Python)",
    "IR-MAD : sélection de pixels invariants (2015 → 2020 et 2024 → 2020)\n"
    "Régression orthogonale par bande · correction du gradient spatial du voile (σ = 300 m)\n"
    "Contrôle sur un échantillon indépendant de pixels invariants",
)
ANALYSES = [
    ("4a", "Histogrammes", "Réflectance par bande\net par date, avant et\naprès normalisation"),
    ("4b", "NDVI", "5 classes (seuils identiques)\nΔNDVI significatif : |Δ| > 0,10\nTransitions entre classes"),
    ("4c", "Classification", "K-means multidate (12 grappes)\nRegroupées en 7 classes\nMatrices de transition"),
]
RESULTS = [
    ("Comparabilité", "Distributions superposées\ndes trois dates"),
    ("Dynamique du couvert", "Cartes NDVI et ΔNDVI\nSuperficie par classe"),
    ("Changements du milieu", "Cartes des classes\nTrajectoires : thermokarst,\nfermeture du couvert"),
]
VALID = (
    "5", "Validation et interprétation",
    "Photo-interprétation de 630 points : matrices de confusion et indice kappa\n"
    "Contexte climatique et phénologique : données ECCC\n"
    "Discussion : dégel du pergélisol, expansion arbustive, limites et recommandations",
)

# --- Mise en page verticale (du haut vers le bas) ----------------------------
h_data = height(*(b for _, b in DATA))
h_atcor, h_geom, h_norm = height(ATCOR[2]), height(GEOM[2]), height(NORM[2])
h_an = height(*(b for *_, b in ANALYSES))
h_res = height(*(b for _, b in RESULTS))
h_val = height(VALID[2])
ARROW_GAP, LANE_PAD = 5.0, 2.0

y = 0
legend_y = y - 3.0
y -= 6.0
lanes = []
lane_top = y
y -= LANE_PAD
data_top = y; y -= h_data + LANE_PAD
lanes.append((lane_top, y, "DONNÉES")); lane_top = y
y -= ARROW_GAP - LANE_PAD
atcor_top = y; y -= h_atcor + ARROW_GAP
geom_top = y; y -= h_geom + ARROW_GAP
norm_top = y; y -= h_norm
label_y = y - 2.6
y -= 5.2
lanes.append((lane_top, y, "PRÉTRAITEMENT")); lane_top = y
bus_y = y - 1.0
y -= 3.2
an_top = y; y -= h_an + LANE_PAD
lanes.append((lane_top, y, "ANALYSES")); lane_top = y
y -= ARROW_GAP - LANE_PAD
res_top = y; y -= h_res + LANE_PAD
lanes.append((lane_top, y, "RÉSULTATS")); lane_top = y
merge_y = y - 1.0
y -= ARROW_GAP - LANE_PAD
val_top = y; y -= h_val + LANE_PAD
lanes.append((lane_top, y, "SYNTHÈSE"))
y_min = y - 0.8

H = -y_min
fig, ax = plt.subplots(figsize=(W / 10, H / 10))
ax.set_xlim(0, W)
ax.set_ylim(y_min, 0)
ax.set_aspect("equal")
ax.axis("off")
fig.subplots_adjust(0, 0, 1, 1)


def box(x, y_top, w, h, kind, title, body, badge=None):
    """Boîte arrondie avec bandeau de titre coloré. Retourne (cx, top, bottom)."""
    edge, head, fill = STYLES[kind]
    yb = y_top - h
    outline = FancyBboxPatch((x, yb), w, h, boxstyle="round,pad=0,rounding_size=1.3",
                             fc=fill, ec=edge, lw=1.6, zorder=3)
    ax.add_patch(outline)
    band = Rectangle((x, y_top - HEADER_H), w, HEADER_H, fc=head, ec="none", zorder=3.1)
    band.set_clip_path(outline)
    ax.add_patch(band)
    ax.plot([x, x + w], [y_top - HEADER_H] * 2, color=edge, lw=0.9, alpha=0.6, zorder=3.2)
    ty = y_top - HEADER_H / 2
    tx = x + w / 2
    if badge:
        r = 1.75
        bx = x + 1.2 + r
        ax.add_patch(Circle((bx, ty), r, fc=edge, ec="none", zorder=4))
        ax.text(bx, ty - 0.05, badge, ha="center", va="center", color="white",
                fontsize=F_BODY - (1.5 if len(badge) > 1 else 0), fontweight="bold", zorder=5)
        if w < 40:  # colonnes étroites : décaler le titre à droite de la pastille
            tx = x + (2 * r + 1.2 + w) / 2
    ax.text(tx, ty, title, ha="center", va="center",
            fontsize=F_TITLE if w > 40 else F_TITLE - 1,
            fontweight="bold", color=INK, zorder=4)
    ax.text(x + w / 2, yb + (h - HEADER_H) / 2, body, ha="center", va="center",
            fontsize=F_BODY, color=BODY, linespacing=1.5, zorder=4)
    return x + w / 2, y_top, yb


def arrow(x0, y0, x1, y1):
    ax.annotate("", xy=(x1, y1), xytext=(x0, y0), zorder=2,
                arrowprops=dict(arrowstyle="-|>,head_length=0.6,head_width=0.3",
                                color=ARROW, lw=1.5, shrinkA=0, shrinkB=0.5))


def line(xs, ys):
    ax.plot(xs, ys, color=ARROW, lw=1.5, solid_capstyle="round", zorder=2)


# --- Légende -----------------------------------------------------------------
renderer = fig.canvas.get_renderer()
units_per_px = W / ax.get_window_extent(renderer).width
items = []
for kind, label in LEGEND:
    t = ax.text(0, 0, label, fontsize=F_LEGEND)
    items.append((kind, label, t.get_window_extent(renderer).width * units_per_px))
    t.remove()
SWATCH, PAD, SEP = 3.0, 1.0, 3.8
total = sum(SWATCH + PAD + w for *_, w in items) + SEP * (len(items) - 1)
lx = (W - total) / 2
for kind, label, tw in items:
    edge, head, _ = STYLES[kind]
    ax.add_patch(FancyBboxPatch((lx, legend_y - 1.05), SWATCH, 2.1,
                                boxstyle="round,pad=0,rounding_size=0.45",
                                fc=head, ec=edge, lw=1.2))
    ax.text(lx + SWATCH + PAD, legend_y, label, va="center", fontsize=F_LEGEND, color=INK)
    lx += SWATCH + PAD + tw + SEP

# --- Bandes de phase ---------------------------------------------------------
for i, (top, bot, label) in enumerate(lanes):
    if i % 2 == 0:
        ax.add_patch(Rectangle((0.5, bot), W - 1, top - bot, fc="#F1F3F7", ec="none", zorder=0))
    ax.add_patch(Rectangle((0.5, bot), 1.0, top - bot, fc="#9EA8B6", ec="none", zorder=1))
    ax.text(6.2, (top + bot) / 2, label, rotation=90, ha="center", va="center",
            fontsize=F_LANE, fontweight="bold", color="#4F5967")

# --- Boîtes et liaisons ------------------------------------------------------
data_boxes = [box(x, data_top, COL_W, h_data, "data", t, b) for x, (t, b) in zip(COLS, DATA)]
_, _, atcor_bot = box(X0, atcor_top, FULL_W, h_atcor, "catalyst", ATCOR[1], ATCOR[2], ATCOR[0])
for bx, _, bb in data_boxes:
    arrow(bx, bb, bx, atcor_top)
_, _, geom_bot = box(X0, geom_top, FULL_W, h_geom, "python", GEOM[1], GEOM[2], GEOM[0])
arrow(CX, atcor_bot, CX, geom_top)
_, _, norm_bot = box(X0, norm_top, FULL_W, h_norm, "python", NORM[1], NORM[2], NORM[0])
arrow(CX, geom_bot, CX, norm_top)

line([CX, CX], [norm_bot, bus_y])
line([COL_CX[0], COL_CX[2]], [bus_y, bus_y])
for c in COL_CX:
    arrow(c, bus_y, c, an_top)
ax.text(CX, label_y, "Réflectances au sol comparables entre les trois dates",
        ha="center", va="center", fontsize=F_BODY, style="italic", color=INK, zorder=5,
        bbox=dict(boxstyle="round,pad=0.4,rounding_size=0.9", fc="white", ec="#9EA8B6", lw=1.0))

an_boxes = [box(x, an_top, COL_W, h_an, "python", t, b, n)
            for x, (n, t, b) in zip(COLS, ANALYSES)]
res_boxes = [box(x, res_top, COL_W, h_res, "result", t, b) for x, (t, b) in zip(COLS, RESULTS)]
for (ax_, _, ab), (_, rt, _) in zip(an_boxes, res_boxes):
    arrow(ax_, ab, ax_, rt)

box(X0, val_top, FULL_W, h_val, "valid", VALID[1], VALID[2], VALID[0])
for rx, _, rb in res_boxes:
    line([rx, rx], [rb, merge_y])
line([COL_CX[0], COL_CX[2]], [merge_y, merge_y])
arrow(CX, merge_y, CX, val_top)

out = Path(__file__).with_suffix("")
for ext in ("png", "svg", "pdf"):
    fig.savefig(f"{out}.{ext}", dpi=300, facecolor="white")
print("OK", round(W / 10, 1), "x", round(H / 10, 1), "po")
