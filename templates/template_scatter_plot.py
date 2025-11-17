"""
TEMPLATE: Scatter Plot with Colormap
=====================================
This template shows how to create scatter plots where points are colored by a third variable.
Suitable for: 3D data visualization, parameter studies, correlation analysis
"""

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import matplotlib.cm as cm

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

# Generate random scatter data
np.random.seed(42)
n_points = 200

# x and y coordinates
x = np.random.randn(n_points) * 2 + 5
y = np.random.randn(n_points) * 3 + 10

# Color value for each point (third variable)
# This could represent: temperature, magnitude, category, etc.
color_values = x * y + np.random.randn(n_points) * 5

# ============================================================================
# PLOT STYLING PARAMETERS
# ============================================================================

fs = 24.0               # Font size
r = 0.9                 # Tick label font ratio
marker_size = 50        # Marker size (50-200 typical for scatter)
marker_alpha = 0.7      # Transparency (0=transparent, 1=opaque)

# ============================================================================
# CREATE FIGURE
# ============================================================================

fig, ax = plt.subplots(figsize=(7.0, 6.0), dpi=50)

# ============================================================================
# CREATE SCATTER PLOT
# ============================================================================

# Scatter plot with colormap
# marker options: 'o' (circle), 's' (square), '^' (triangle up), 'v' (triangle down),
#                 'D' (diamond), '*' (star), 'p' (pentagon), 'h' (hexagon)
# cmap options: 'viridis', 'plasma', 'inferno', 'magma', 'coolwarm', 'RdYlBu',
#               'autumn', 'winter', 'spring', 'summer', 'jet', 'rainbow'

scatter = ax.scatter(x, y, c=color_values, cmap='autumn_r', 
                    marker='s', s=marker_size, alpha=marker_alpha,
                    edgecolors='none')

# For scatter without colormap (single color):
# ax.scatter(x, y, c='blue', marker='o', s=marker_size, alpha=0.6, edgecolors='black')

# For categorical coloring:
# categories = np.random.choice(['A', 'B', 'C'], size=n_points)
# colors = {'A': 'red', 'B': 'green', 'C': 'blue'}
# for category in ['A', 'B', 'C']:
#     mask = categories == category
#     ax.scatter(x[mask], y[mask], c=colors[category], label=category, s=marker_size)

# ============================================================================
# COLORBAR
# ============================================================================

# Add colorbar
cbar = fig.colorbar(scatter, shrink=0.85)

# Set colorbar label
cbar.set_label(r'Color variable (units)', fontsize=fs, labelpad=10)

# Customize colorbar tick labels
cbar.ax.tick_params(labelsize=r*fs)

# Set custom colorbar ticks
# cbar.set_ticks([0, 20, 40, 60, 80, 100])

# For discrete color levels:
# cbar.set_ticks(np.linspace(color_values.min(), color_values.max(), 6))

# ============================================================================
# AXIS CONFIGURATION
# ============================================================================

# Set axis limits
ax.set_xlim(0, 10)
ax.set_ylim(0, 20)

# Set tick positions
ax.xaxis.set_ticks(np.arange(0, 11, 2))
ax.yaxis.set_ticks(np.arange(0, 21, 5))

# Enable minor ticks
ax.minorticks_on()

# Set labels
ax.set_xlabel(r'$x$ variable (units)', color='k', fontsize=fs)
ax.set_ylabel(r'$y$ variable (units)', color='k', fontsize=fs)

# ============================================================================
# TICK FORMATTING
# ============================================================================

# Format tick labels
for tick in ax.get_xticklabels():
    tick.set_fontsize(r * fs)
for tick in ax.get_yticklabels():
    tick.set_fontsize(r * fs)

# Customize tick appearance
ax.tick_params(which='major', direction='in', length=10, width=1.5, colors='k')
ax.tick_params(which='minor', direction='in', length=5, width=1.5, colors='k')
ax.tick_params(which='both', top=True, right=True)

# ============================================================================
# ADDITIONAL ELEMENTS (Optional)
# ============================================================================

# Add trend line
# z = np.polyfit(x, y, 1)
# p = np.poly1d(z)
# x_trend = np.linspace(x.min(), x.max(), 100)
# ax.plot(x_trend, p(x_trend), 'k--', linewidth=2, label='Trend')

# Add reference line
# ax.axhline(y=10, color='gray', linestyle='--', linewidth=1.5, alpha=0.5)
# ax.axvline(x=5, color='gray', linestyle='--', linewidth=1.5, alpha=0.5)

# Add text annotation
# ax.text(2, 18, r'Region of interest', fontsize=r*fs, color='k')

# ============================================================================
# LEGEND (if using categorical colors)
# ============================================================================

# ax.legend(loc='upper left', fontsize=r*fs, frameon=True, 
#          markerscale=1.5, scatterpoints=1)

# ============================================================================
# ASPECT RATIO
# ============================================================================

ratio = 1.0
ax.set_aspect(1.0/ax.get_data_ratio() * ratio)

# For equal aspect (square plot):
# ax.set_aspect('equal')

# ============================================================================
# SAVE AND DISPLAY
# ============================================================================

output_filename = 'scatter_plot.pdf'
plt.savefig(output_filename, bbox_inches='tight', dpi=300)
plt.show()

# ============================================================================
# ADDITIONAL TIPS FOR SCATTER PLOTS
# ============================================================================

# 1. Size variation (bubble chart):
#    sizes = np.random.rand(n_points) * 200
#    ax.scatter(x, y, s=sizes, c=color_values, cmap='viridis', alpha=0.6)

# 2. Edge colors for better visibility:
#    ax.scatter(x, y, c=color_values, cmap='viridis', 
#              edgecolors='black', linewidths=0.5)

# 3. Color limits (vmin, vmax):
#    scatter = ax.scatter(x, y, c=color_values, cmap='viridis',
#                        vmin=0, vmax=100)

# 4. Logarithmic color scale:
#    import matplotlib.colors as colors
#    scatter = ax.scatter(x, y, c=color_values, 
#                        norm=colors.LogNorm(vmin=1, vmax=1000),
#                        cmap='viridis')

# 5. Custom colormap:
#    import matplotlib.colors as mcolors
#    colors_list = ['blue', 'white', 'red']
#    n_bins = 100
#    cmap = mcolors.LinearSegmentedColormap.from_list('custom', colors_list, N=n_bins)

# 6. Hexbin alternative (for dense data):
#    hexbin = ax.hexbin(x, y, gridsize=20, cmap='Blues', mincnt=1)
#    cb = fig.colorbar(hexbin, ax=ax)

# 7. Correlation coefficient:
#    corr = np.corrcoef(x, y)[0, 1]
#    ax.text(0.05, 0.95, f'$r = {corr:.3f}$', 
#           transform=ax.transAxes, fontsize=r*fs)
