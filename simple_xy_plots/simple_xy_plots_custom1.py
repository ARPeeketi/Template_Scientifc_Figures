import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import os

"""
FINAL CLEANED & FULLY COMMENTED PLOTTING TEMPLATE
-------------------------------------------------------------------------------
This file is designed for **students, beginners, and researchers** who want a
fully customizable and extremely clear Matplotlib template.

Every section includes:
    ✔ What the code does
    ✔ How to modify it
    ✔ Tips for common customizations (colors, markers, ticks, fonts, styles)
    ✔ Notes about publication-quality vs. presentation-quality settings

Use this file as a base for ALL your plotting work.
-------------------------------------------------------------------------------
"""

# ============================================================================
# 1. OPTIONAL: LATEX RENDERING + FONT CONFIGURATION
# ============================================================================
# These settings provide publication-quality fonts using LaTeX.
# LaTeX MUST be installed on your system for this to work.
# If you get errors, simply comment out the entire block.
# ---------------------------------------------------------------------------
try:
    preamble = '\usepackage{times}\n\usepackage{newtxmath}\n\usepackage{siunitx}'
    plt.rc('text', usetex=True)
    plt.rc('text.latex', preamble=preamble)
    matplotlib.rcParams['font.serif'] = "Times New Roman"   # Good for journals
    matplotlib.rcParams['font.family'] = "serif"
except Exception:
    print("LaTeX not detected. Using Matplotlib default fonts.")


# ============================================================================
# 2. LOAD DATA (FILE OR SAMPLE)
# ============================================================================
# Students: Edit 'fname' to point to your file.
# If the file is missing, the script automatically generates example data.
# ---------------------------------------------------------------------------

directory = os.getcwd()
fname = 'your_data_file.dat'     # <--- CHANGE THIS TO YOUR FILE

try:
    A = np.genfromtxt(fname, delimiter=',')  # For CSV-style data
    x_data = A[:, 0]
    y_data = A[:, 1]
    print(f"Loaded data from {fname}")
except Exception:
    print(f"Warning: {fname} not found. Using generated example data...")
    x_data = np.linspace(0, 10, 100)
    y_data = np.sin(x_data) * np.exp(-x_data / 10)


# ============================================================================
# 3. GLOBAL PLOT SETTINGS
# ============================================================================
# These apply to ALL figures unless overridden.
# Students: modify these depending on whether you're making
# a publication figure, presentation slide, or homework assignment.
# ---------------------------------------------------------------------------
r = 0.9            # Tick label scaling factor (0.8–1.2 works well)
fs = 24.0          # Axis label font size
lwidth = 2.0       # Line width (increase for visibility)
figsize = (6.5, 6.0)   # Standard size for journal figures


# ============================================================================
# 4. FIGURE 1 — SIMPLE X-Y LINE PLOT
# ============================================================================
figname = 'simple_xy.pdf'
fig, ax = plt.subplots(figsize=figsize, dpi=100)

# MAIN PLOT LINE -------------------------------------------------------------
# Students: Customize line color, width, marker, and style here.
ax.plot(x_data, y_data, color='b', linewidth=lwidth)

# AXIS LIMITS ----------------------------------------------------------------
# Adjust manually if needed: ax.set_xlim(0, 10), ax.set_ylim(-1, 1)
ax.set_xlim(x_data.min(), x_data.max())
ax.set_ylim(y_data.min() * 1.1, y_data.max() * 1.1)

# AXIS LABELS -----------------------------------------------------------------
ax.set_xlabel(r"X variable (units)", fontsize=fs)
ax.set_ylabel(r"Y variable (units)", fontsize=fs)

# TICK CUSTOMIZATION ----------------------------------------------------------
ax.minorticks_on()
for t in ax.get_xticklabels(): t.set_fontsize(r * fs)
for t in ax.get_yticklabels(): t.set_fontsize(r * fs)
ax.tick_params(which='major', direction='in', length=10, width=1.5)
ax.tick_params(which='minor', direction='in', length=5, width=1.5)

# SAVE SETTINGS ---------------------------------------------------------------
plt.savefig(
    figname,
    bbox_inches='tight',   # removes excess white borders
    dpi=300                # 300 dpi = publication quality
)
print(f"Saved: {figname}")
plt.show()


# ============================================================================
# 5. FIGURE 2 — MULTIPLE LINES
# ============================================================================
figname = 'multi_line.pdf'
fig, ax = plt.subplots(figsize=figsize, dpi=100)

# CREATE MORE DATA -----------------------------------------------------------
y1 = np.sin(x_data)
y2 = np.cos(x_data)
y3 = 0.5 * np.sin(x_data)

# PLOT MULTIPLE LINES --------------------------------------------------------
ax.plot(x_data, y1, 'r', linewidth=lwidth, label='Data 1')
ax.plot(x_data, y2, 'b', linewidth=lwidth, label='Data 2')
ax.plot(x_data, y3, 'g', linewidth=lwidth, label='Data 3')

# LABELS ---------------------------------------------------------------------
ax.set_xlabel(r"X variable (units)", fontsize=fs)
ax.set_ylabel(r"Y variable (units)", fontsize=fs)

# TICKS ----------------------------------------------------------------------
ax.minorticks_on()
for t in ax.get_xticklabels(): t.set_fontsize(r * fs)
for t in ax.get_yticklabels(): t.set_fontsize(r * fs)
ax.tick_params(which='major', direction='in', length=10, width=1.5)
ax.tick_params(which='minor', direction='in', length=5, width=1.5)

# LEGEND --------------------------------------------------------------------
# Students: move legend with loc='lower left', 'best', etc.
ax.legend(loc='upper right', frameon=False, fontsize=r * fs)

plt.savefig(figname, bbox_inches='tight', dpi=300)
print(f"Saved: {figname}")
plt.show()


# ============================================================================
# 6. FIGURE 3 — LINE PLOT WITH MARKERS
# ============================================================================
figname = 'xy_with_markers.pdf'
fig, ax = plt.subplots(figsize=figsize, dpi=100)

# MARKER OPTIONS -------------------------------------------------------------
# marker='o', 's', '^', 'd', '*', 'x', '+'
ax.plot(
    x_data, y_data,
    'bo-',                    # b=blue, o=circle marker, -=line
    linewidth=lwidth,
    markersize=6,
    markevery=5,              # show markers every 5 points
    label='Measured'
)

# LABELS/TICKS ---------------------------------------------------------------
ax.set_xlabel(r"X variable (units)", fontsize=fs)
ax.set_ylabel(r"Y variable (units)", fontsize=fs)
ax.set_xlim(x_data.min(), x_data.max())
ax.set_ylim(y_data.min() * 1.1, y_data.max() * 1.1)

ax.minorticks_on()
for t in ax.get_xticklabels(): t.set_fontsize(r * fs)
for t in ax.get_yticklabels(): t.set_fontsize(r * fs)
ax.tick_params(which='major', direction='in', length=10, width=1.5)
ax.tick_params(which='minor', direction='in', length=5, width=1.5)

# LEGEND ---------------------------------------------------------------------
ax.legend(loc='best', frameon=False, fontsize=r * fs)

# GRID -----------------------------------------------------------------------
ax.grid(alpha=0.3, linestyle='--')

plt.savefig(figname, bbox_inches='tight', dpi=300)
print(f"Saved: {figname}")
plt.show()


# ============================================================================
# 7. FIGURE 4 — SCATTER PLOT + POLYNOMIAL FIT
# ============================================================================
figname = 'xy_scatter_fit.pdf'
fig, ax = plt.subplots(figsize=figsize, dpi=100)

# SCATTER POINTS -------------------------------------------------------------
ax.scatter(
    x_data, y_data,
    s=50,                   # marker size
    c='red',                # color
    edgecolors='black',
    linewidth=0.5,
    alpha=0.6,
    label='Data'
)

# POLYNOMIAL FIT -------------------------------------------------------------
# Students: change degree=1 (linear), 3, 4, etc.
coeffs = np.polyfit(x_data, y_data, deg=2)
poly = np.poly1d(coeffs)
y_fit = poly(x_data)
ax.plot(x_data, y_fit, 'b-', linewidth=lwidth, label='Fit')

# LABELS/TICKS ---------------------------------------------------------------
ax.set_xlabel(r"X variable (units)", fontsize=fs)
ax.set_ylabel(r"Y variable (units)", fontsize=fs)
ax.set_xlim(x_data.min(), x_data.max())

ax.minorticks_on()
for t in ax.get_xticklabels(): t.set_fontsize(r * fs)
for t in ax.get_yticklabels(): t.set_fontsize(r * fs)
ax.tick_params(which='major', direction='in', length=10, width=1.5)
ax")){
    "multiple": false
}]}
