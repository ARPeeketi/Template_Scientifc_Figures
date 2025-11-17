"""
TEMPLATE: Simple Line Plot
===========================
This template shows how to create publication-quality line plots with multiple lines.
Suitable for: Time series, function plots, comparing multiple datasets
"""

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, AutoMinorLocator

# ============================================================================
# FONT AND TEXT CONFIGURATION
# ============================================================================

# Option 1: Use LaTeX rendering for professional typography (requires LaTeX installation)
plt.rc('text', usetex=True)
preamble = '\\usepackage{times}\n\\usepackage{newtxmath}\n\\usepackage{siunitx}\n'
plt.rc('text.latex', preamble=preamble)

# Option 2: Use standard fonts (comment out LaTeX options above if using this)
# matplotlib.rcParams['font.family'] = 'serif'
# matplotlib.rcParams['font.serif'] = ['Times New Roman', 'DejaVu Serif']

# For non-LaTeX rendering, set font
matplotlib.rcParams['font.serif'] = "Times New Roman"
matplotlib.rcParams['font.family'] = "serif"

# ============================================================================
# DATA GENERATION (Replace with your actual data)
# ============================================================================

# Create sample x data
x = np.linspace(0, 10, 100)

# Create sample y data for multiple lines
y1 = np.sin(x)
y2 = np.cos(x)
y3 = 0.5 * np.sin(2*x)

# ============================================================================
# PLOT STYLING PARAMETERS
# ============================================================================

# Font sizes
fs = 24.0          # Main font size for labels
r = 0.9            # Ratio for tick label font size (0.9 * fs)

# Line properties
linewidth = 2.0    # Line width (1.0-3.0 typical)

# Figure size
fig_width = 6.2    # Figure width in inches
fig_height = 6.0   # Figure height in inches
dpi = 50          # DPI for display (use 300 for saving high-quality figures)

# ============================================================================
# CREATE FIGURE AND AXES
# ============================================================================

fig, ax = plt.subplots(figsize=(fig_width, fig_height), dpi=dpi)

# ============================================================================
# PLOT DATA
# ============================================================================

# Plot multiple lines with different colors and labels
# Color options: 'r' (red), 'g' (green), 'b' (blue), 'c' (cyan), 'm' (magenta),
#                'y' (yellow), 'k' (black), or hex codes like '#FF5733'
# Line style options: '-' (solid), '--' (dashed), '-.' (dash-dot), ':' (dotted)
# Marker options: 'o' (circle), 's' (square), '^' (triangle), 'D' (diamond), etc.

ax.plot(x, y1, 'r-', linewidth=linewidth, label=r'sin($x$)')
ax.plot(x, y2, 'g-', linewidth=linewidth, label=r'cos($x$)')
ax.plot(x, y3, 'c-', linewidth=linewidth, label=r'0.5 sin($2x$)')

# For line with markers:
# ax.plot(x, y1, 'ro-', linewidth=linewidth, markersize=6, markevery=5, label='Data')

# ============================================================================
# AXIS LIMITS AND TICKS
# ============================================================================

# Set axis limits
ax.set_xlim(0.0, 10.0)
ax.set_ylim(-1.5, 1.5)

# Set custom tick positions
ax.xaxis.set_ticks(np.arange(0, 10.1, 2.0))     # Major ticks every 2 units
ax.yaxis.set_ticks(np.arange(-1.5, 1.51, 0.5))  # Major ticks every 0.5 units

# Enable minor ticks (automatically placed between major ticks)
ax.minorticks_on()

# Alternative: Set specific minor tick spacing
# ax.xaxis.set_minor_locator(MultipleLocator(0.5))
# ax.yaxis.set_minor_locator(MultipleLocator(0.1))

# ============================================================================
# AXIS LABELS
# ============================================================================

# Set x and y labels with LaTeX formatting
ax.set_xlabel(r'$x$ variable (units)', color='k', fontsize=fs)
ax.set_ylabel(r'$y$ variable (units)', color='k', fontsize=fs)

# For special symbols in LaTeX:
# Greek letters: \alpha, \beta, \gamma, \theta, \pi, etc.
# Math operators: \frac{a}{b}, \sqrt{x}, x^2, x_i, \sum, \int, etc.
# Example: ax.set_xlabel(r'$\kappa$ ($\SI{}{\nano\meter}$)', fontsize=fs)

# ============================================================================
# TICK LABEL FORMATTING
# ============================================================================

# Set tick label font size
for tick in ax.get_xticklabels():
    tick.set_fontsize(r * fs)
for tick in ax.get_yticklabels():
    tick.set_fontsize(r * fs)

# ============================================================================
# TICK APPEARANCE
# ============================================================================

# Customize tick appearance
# direction: 'in' (inside plot), 'out' (outside plot), 'inout' (both sides)
# length: tick length in points
# width: tick width in points
# colors: tick color

ax.tick_params(which='major', direction='in', length=10, width=1.5, colors='k')
ax.tick_params(which='minor', direction='in', length=5, width=1.5, colors='k')

# Show ticks on all sides of the plot
ax.tick_params(which='both', top=True, right=True)

# ============================================================================
# LEGEND
# ============================================================================

# Add legend
# Location options: 'upper left', 'upper right', 'lower left', 'lower right',
#                  'center left', 'center right', 'upper center', 'lower center', 'center'
# Or use bbox_to_anchor for precise positioning: (x, y) in axes coordinates (0-1)

ax.legend(loc='upper right', fontsize=r*fs, frameon=True, shadow=False,
          ncol=1, columnspacing=0.8, fancybox=False)

# For legend outside plot area:
# ax.legend(loc='upper left', bbox_to_anchor=(1.02, 1.0), fontsize=r*fs, frameon=False)

# ============================================================================
# GRID (Optional)
# ============================================================================

# Add grid lines
# ax.grid(True, which='major', linestyle='--', linewidth=0.5, alpha=0.7)
# ax.grid(True, which='minor', linestyle=':', linewidth=0.3, alpha=0.5)

# ============================================================================
# ANNOTATIONS AND TEXT (Optional)
# ============================================================================

# Add text annotation at specific location
# ax.text(5.0, 1.2, r'Peak', color='k', fontsize=r*fs)

# Add arrow annotation
# ax.annotate('Important point', xy=(3.14, 0), xytext=(5, 0.5),
#             arrowprops=dict(arrowstyle='->', lw=1.5, color='red'),
#             fontsize=r*fs)

# ============================================================================
# ASPECT RATIO (Optional)
# ============================================================================

# Control aspect ratio
ratio = 1.0
ax.set_aspect(1.0/ax.get_data_ratio() * ratio)

# For equal aspect ratio (useful for spatial data):
# ax.set_aspect('equal')

# ============================================================================
# SAVE AND DISPLAY
# ============================================================================

# Save figure
# Format options: 'pdf', 'png', 'svg', 'eps', 'jpg'
# bbox_inches='tight' removes extra whitespace
# dpi: resolution for raster formats (300 recommended for publication)

output_filename = 'line_plot.pdf'
plt.savefig(output_filename, bbox_inches='tight', dpi=300)

# Display the plot
plt.show()

# ============================================================================
# ADDITIONAL TIPS
# ============================================================================

# 1. Color palettes:
#    - Qualitative: tab10, tab20, Set1, Set2, Set3, Paired
#    - Sequential: Blues, Greens, Reds, YlOrRd, Purples
#    - Diverging: RdBu, RdYlBu, RdYlGn, Spectral
#    Usage: color = plt.cm.tab10(0)  # First color from tab10

# 2. Line styles can be combined: 'ro--' = red circles with dashed line

# 3. For scientific notation on axes:
#    from matplotlib.ticker import ScalarFormatter
#    formatter = ScalarFormatter(useMathText=True)
#    formatter.set_scientific(True)
#    formatter.set_powerlimits((-2, 2))
#    ax.yaxis.set_major_formatter(formatter)

# 4. For logarithmic axes:
#    ax.set_xscale('log')
#    ax.set_yscale('log')

# 5. Transparency: Add alpha parameter to plot:
#    ax.plot(x, y, 'r-', alpha=0.5)  # 50% transparent
