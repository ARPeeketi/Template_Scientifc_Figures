"""
TEMPLATE: Filled Area Plots and Special Features
=================================================
This template shows fill_between, annotations, arrows, and other advanced features.
Suitable for: Uncertainty bands, shaded regions, highlighting areas of interest
"""

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, Ellipse, Polygon, FancyBboxPatch
from matplotlib.ticker import MultipleLocator

# ============================================================================
# FONT AND TEXT CONFIGURATION
# ============================================================================

plt.rc('text', usetex=True)
preamble = '\\usepackage{times}\n\\usepackage{newtxmath}\n\\usepackage{siunitx}\n'
plt.rc('text.latex', preamble=preamble)

matplotlib.rcParams['font.serif'] = "Times New Roman"
matplotlib.rcParams['font.family'] = "serif"

# ============================================================================
# DATA GENERATION (Replace with your actual data)
# ============================================================================

x = np.linspace(0, 10, 100)
y = np.sin(x)
y_upper = y + 0.3 + 0.1 * np.random.randn(len(x))
y_lower = y - 0.3 - 0.1 * np.random.randn(len(x))

# Additional data for demonstrations
y2 = np.cos(x) * 0.7

# ============================================================================
# PLOT STYLING PARAMETERS
# ============================================================================

fs = 24.0           # Font size
r = 0.9             # Tick label font ratio
linewidth = 2.0     # Line width

# ============================================================================
# FILL_BETWEEN (Shaded uncertainty bands)
# ============================================================================

fig, ax = plt.subplots(figsize=(7.0, 6.0), dpi=50)

# Plot main line
ax.plot(x, y, 'b-', linewidth=linewidth, label='Mean value', zorder=3)

# Fill between upper and lower bounds
# alpha: transparency (0=transparent, 1=opaque)
# zorder: drawing order (higher = on top)
ax.fill_between(x, y_lower, y_upper, 
                alpha=0.3, color='blue', 
                label='Uncertainty band',
                zorder=2)

# Alternative: Fill between line and y=0
# ax.fill_between(x, 0, y, where=(y > 0), alpha=0.3, color='green',
#                label='Positive region')
# ax.fill_between(x, 0, y, where=(y < 0), alpha=0.3, color='red',
#                label='Negative region')

# ============================================================================
# FILL_BETWEEN TWO CURVES
# ============================================================================

# Fill between two different curves
ax.plot(x, y2, 'r-', linewidth=linewidth, label='Second curve', zorder=3)
ax.fill_between(x, y, y2, 
                where=(y >= y2), 
                alpha=0.2, color='purple',
                interpolate=True,
                label='Area between curves')

# ============================================================================
# ANNOTATIONS AND ARROWS
# ============================================================================

# Simple text annotation
ax.text(3, 0.5, r'Important region', fontsize=r*fs, color='darkgreen',
       bbox=dict(boxstyle='round,pad=0.5', facecolor='yellow', alpha=0.5))

# Arrow annotation pointing to specific location
# arrowstyle options: '->', '-[', '-|>', '<->', '<|-|>', 'fancy', 'simple', 'wedge'
ax.annotate('Peak', 
           xy=(np.pi/2, 1.0),  # Point to annotate
           xytext=(4, 1.3),     # Text location
           arrowprops=dict(arrowstyle='->, head_length=0.7, head_width=0.5',
                         lw=2, color='red'),
           fontsize=r*fs, color='red')

# Double-headed arrow between two points
ax.annotate('', 
           xy=(8, -0.5),        # End point
           xytext=(6, -0.5),    # Start point  
           arrowprops=dict(arrowstyle='<->, head_length=0.7, head_width=0.5',
                         lw=2, color='black'))

# Add text label for the arrow
ax.text(7, -0.7, r'$\Delta x$', fontsize=r*fs, ha='center')

# Curved arrow
# from matplotlib.patches import FancyArrowPatch
# arrow = FancyArrowPatch((1, 0.5), (2, -0.5),
#                        arrowstyle='->', connectionstyle='arc3,rad=0.3',
#                        lw=2, color='purple')
# ax.add_patch(arrow)

# ============================================================================
# SHAPES AND PATCHES
# ============================================================================

# Rectangle
# Rectangle((x, y), width, height, ...)
rect = Rectangle((5, -1.2), 2, 0.4, 
                linewidth=2, edgecolor='orange', 
                facecolor='yellow', alpha=0.3)
ax.add_patch(rect)

# Circle
# Circle((x_center, y_center), radius, ...)
circle = Circle((8.5, 0.5), 0.3, 
               linewidth=2, edgecolor='green', 
               facecolor='lightgreen', alpha=0.4)
ax.add_patch(circle)

# Ellipse
# from matplotlib.patches import Ellipse
# ellipse = Ellipse((7, 0.8), width=1, height=0.5, angle=30,
#                  linewidth=2, edgecolor='purple',
#                  facecolor='lavender', alpha=0.4)
# ax.add_patch(ellipse)

# Polygon
# vertices = [(1, -0.8), (1.5, -1.2), (2, -0.8), (1.5, -0.4)]
# polygon = Polygon(vertices, closed=True,
#                  linewidth=2, edgecolor='brown',
#                  facecolor='tan', alpha=0.4)
# ax.add_patch(polygon)

# ============================================================================
# REFERENCE LINES
# ============================================================================

# Horizontal line across entire plot
ax.axhline(y=0, color='gray', linestyle='--', linewidth=1.5, 
          alpha=0.7, zorder=1)

# Vertical line
ax.axvline(x=5, color='gray', linestyle=':', linewidth=1.5,
          alpha=0.7, zorder=1)

# Horizontal span (shaded region)
ax.axhspan(-0.2, 0.2, alpha=0.15, color='gray', zorder=1,
          label='Baseline region')

# Vertical span
# ax.axvspan(2, 4, alpha=0.1, color='green', zorder=1)

# Line segment (not spanning entire axis)
ax.plot([0.5, 2.5], [1.2, 1.2], 'k-', linewidth=2)
ax.text(1.5, 1.3, 'Reference', fontsize=0.8*fs, ha='center')

# ============================================================================
# MATHEMATICAL NOTATIONS
# ============================================================================

# Complex equation example
# ax.text(1, -1.0, r'$f(x) = \int_0^x e^{-t^2} dt + \sum_{n=1}^{\infty} \frac{1}{n^2}$',
#        fontsize=r*fs, bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

# Greek letters and symbols
# ax.text(6, 1.0, r'$\alpha, \beta, \gamma, \Delta, \Omega, \theta$',
#        fontsize=r*fs)

# Fractions and square roots
# ax.text(6, 0.7, r'$\frac{a}{b}, \sqrt{x}, x^2, x_i, \bar{x}$',
#        fontsize=r*fs)

# ============================================================================
# AXIS CONFIGURATION
# ============================================================================

ax.set_xlim(0, 10)
ax.set_ylim(-1.5, 1.5)

ax.set_xlabel(r'$x$ variable (units)', fontsize=fs)
ax.set_ylabel(r'$y$ variable (units)', fontsize=fs)

# ============================================================================
# TICK FORMATTING
# ============================================================================

for tick in ax.get_xticklabels():
    tick.set_fontsize(r * fs)
for tick in ax.get_yticklabels():
    tick.set_fontsize(r * fs)

ax.minorticks_on()
ax.tick_params(which='major', direction='in', length=10, width=1.5, colors='k')
ax.tick_params(which='minor', direction='in', length=5, width=1.5, colors='k')
ax.tick_params(which='both', top=True, right=True)

# ============================================================================
# LEGEND
# ============================================================================

# Legend with custom properties
ax.legend(loc='upper right', fontsize=0.7*fs, frameon=True,
         shadow=False, fancybox=True, framealpha=0.9)

# ============================================================================
# SAVE AND DISPLAY
# ============================================================================

output_filename = 'filled_area_plot.pdf'
plt.savefig(output_filename, bbox_inches='tight', dpi=300)
plt.show()

# ============================================================================
# ADDITIONAL TIPS
# ============================================================================

# 1. Multiple fill_between with step edges:
#    ax.fill_between(x, y1, y2, step='pre', alpha=0.3)
#    # step options: 'pre', 'post', 'mid'

# 2. Conditional fill based on criteria:
#    threshold = 0.5
#    ax.fill_between(x, y, threshold, 
#                   where=(y > threshold), 
#                   color='green', alpha=0.3, label='Above threshold')
#    ax.fill_between(x, y, threshold,
#                   where=(y <= threshold),
#                   color='red', alpha=0.3, label='Below threshold')

# 3. Gradient-filled areas:
#    # Requires additional libraries or manual color mapping
#    from matplotlib.collections import PolyCollection
#    # Create color gradient manually

# 4. Text with math and units:
#    ax.text(5, 0, r'$T = \SI{300}{\kelvin}$', fontsize=fs)
#    ax.text(5, -0.3, r'$E = \SI{2.5e-19}{\joule}$', fontsize=fs)

# 5. Rotated text:
#    ax.text(3, 0, 'Rotated text', fontsize=fs, rotation=45,
#           ha='left', va='bottom')

# 6. Multi-line text:
#    ax.text(2, 1, 'Line 1\nLine 2\nLine 3', fontsize=fs,
#           ha='center', va='center',
#           bbox=dict(boxstyle='round', facecolor='wheat'))

# 7. Text with arrow pointing outward:
#    ax.annotate('Feature', xy=(np.pi, 0), xycoords='data',
#               xytext=(0.8, 0.95), textcoords='axes fraction',
#               arrowprops=dict(arrowstyle='->', lw=2),
#               fontsize=fs, ha='right')

# 8. Connection lines between points:
#    from matplotlib.patches import ConnectionPatch
#    con = ConnectionPatch((2, 0.5), (3, -0.5), "data", "data",
#                         arrowstyle="->", shrinkA=5, shrinkB=5,
#                         mutation_scale=20, fc="black")
#    ax.add_artist(con)

# 9. Fancy boxes for text:
#    ax.text(7, -1, 'Fancy box', fontsize=fs,
#           bbox=dict(boxstyle='round,pad=0.5', facecolor='cyan',
#                    edgecolor='blue', linewidth=2, alpha=0.5))
#    # boxstyle options: 'round', 'round4', 'square', 'larrow', 'rarrow',
#    #                   'darrow', 'sawtooth', 'roundtooth'

# 10. Highlighting regions of interest:
#     # Vertical bands for time periods/phases
#     phase1_end = 3
#     phase2_end = 7
#     ax.axvspan(0, phase1_end, alpha=0.1, color='blue', label='Phase 1')
#     ax.axvspan(phase1_end, phase2_end, alpha=0.1, color='green', label='Phase 2')
#     ax.axvspan(phase2_end, 10, alpha=0.1, color='red', label='Phase 3')

# 11. Confidence intervals with multiple bands:
#     # 1-sigma band
#     ax.fill_between(x, y - std1, y + std1, alpha=0.4, color='blue')
#     # 2-sigma band
#     ax.fill_between(x, y - std2, y + std2, alpha=0.2, color='blue')

# 12. Pattern fills (hatching):
#     ax.fill_between(x, y_lower, y_upper, alpha=0.3, color='blue',
#                    hatch='///', edgecolor='darkblue')
#     # hatch patterns: '/', '\\', '|', '-', '+', 'x', 'o', 'O', '.', '*'

# 13. Asymmetric fills:
#     # Different upper and lower bounds
#     upper_bound = y + 0.5 + 0.1 * x
#     lower_bound = y - 0.3 - 0.05 * x  
#     ax.fill_between(x, lower_bound, upper_bound, alpha=0.3)

# 14. Custom arrowstyles:
#     from matplotlib.patches import FancyArrowPatch
#     arrow = FancyArrowPatch((1, 0), (2, 0.5),
#                           arrowstyle='fancy, head_length=10, head_width=10',
#                           color='purple', lw=2)
#     ax.add_patch(arrow)

# 15. Coordinate systems for annotations:
#     # 'data': data coordinates (default)
#     # 'axes fraction': fraction of axes (0-1)
#     # 'figure fraction': fraction of entire figure (0-1)
#     ax.text(0.5, 0.95, 'Axes coordinates', 
#            transform=ax.transAxes, fontsize=fs, ha='center')
