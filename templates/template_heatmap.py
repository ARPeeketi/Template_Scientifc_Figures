"""
TEMPLATE: Heatmap (Pcolormesh/Imshow)
======================================
This template shows how to create 2D heatmap visualizations.
Suitable for: Matrix data, spatial data, parameter sweeps, correlation matrices
"""

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import copy

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

# Create meshgrid for x and y coordinates
M = 100  # Number of points in y-direction
N = 100  # Number of points in x-direction

# Create coordinate arrays
x = np.linspace(0, 10, N)
y = np.linspace(0, 10, M)

# Create 2D meshgrid
X, Y = np.meshgrid(x, y)

# Generate 2D data (z-values)
# Example: Gaussian peaks
Z = (np.exp(-((X-3)**2 + (Y-3)**2)/2) + 
     0.5 * np.exp(-((X-7)**2 + (Y-7)**2)/3) +
     0.3 * np.exp(-((X-5)**2 + (Y-2)**2)/1))

# ============================================================================
# PLOT STYLING PARAMETERS
# ============================================================================

fs = 24.0           # Font size
r = 0.9             # Tick label font ratio
linewidth = 1.5     # Contour line width

# ============================================================================
# CREATE FIGURE
# ============================================================================

fig, ax = plt.subplots(figsize=(7.0, 6.0), dpi=50)

# ============================================================================
# CHOOSE COLORMAP
# ============================================================================

# Copy colormap to allow modification
cmap = copy.copy(matplotlib.colormaps["autumn_r"])

# Popular colormaps:
# Sequential: 'viridis', 'plasma', 'inferno', 'magma', 'cividis'
#            'Blues', 'Greens', 'Reds', 'YlOrRd', 'hot', 'cool', 'autumn', 'winter'
# Diverging: 'coolwarm', 'RdBu', 'RdYlBu', 'RdYlGn', 'Spectral', 'seismic'
# Perceptually uniform: 'viridis', 'plasma', 'inferno', 'magma', 'cividis'

# Add '_r' to reverse: 'autumn_r', 'viridis_r', etc.

# ============================================================================
# CREATE HEATMAP - OPTION 1: PCOLORMESH (Recommended for irregular grids)
# ============================================================================

# pcolormesh creates a pseudocolor plot with smooth interpolation
# shading options: 'flat' (default), 'gouraud' (smooth), 'nearest', 'auto'

heatmap = ax.pcolormesh(X, Y, Z, cmap=cmap, shading='gouraud', 
                        vmin=0, vmax=1.5, alpha=1.0, edgecolors='none')

# Set colors for values outside the range
heatmap.cmap.set_under('white')  # Color for values < vmin
heatmap.cmap.set_over('white')   # Color for values > vmax
heatmap.set_clim(0, 1.5)

# ============================================================================
# CREATE HEATMAP - OPTION 2: IMSHOW (Good for regular grids)
# ============================================================================

# Uncomment to use imshow instead of pcolormesh
# imshow is faster but requires regular grid

# heatmap = ax.imshow(Z, extent=[x.min(), x.max(), y.min(), y.max()],
#                     origin='lower', cmap=cmap, vmin=0, vmax=1.5,
#                     aspect='auto', interpolation='bilinear')

# interpolation options: 'none', 'nearest', 'bilinear', 'bicubic', 
#                       'spline16', 'spline36', 'gaussian'

# ============================================================================
# ADD CONTOUR LINES (Optional)
# ============================================================================

# Add contour lines on top of heatmap
contour_levels = [0.3, 0.6, 0.9, 1.2]
contours = ax.contour(X, Y, Z, levels=contour_levels, colors='k', 
                     linewidths=linewidth, linestyles='solid')

# Add labels to contour lines
# ax.clabel(contours, inline=True, fontsize=0.7*fs, fmt='%.1f')

# For dashed contours at specific level:
# contour_dashed = ax.contour(X, Y, Z, levels=[0.75], colors='k',
#                            linewidths=linewidth, linestyles='dashed')

# ============================================================================
# COLORBAR
# ============================================================================

# Add colorbar
cbar = fig.colorbar(heatmap, shrink=0.85, pad=0.02)

# Set colorbar label
# cbar.set_label(r'$Z$ value (units)', fontsize=fs, labelpad=10)

# Customize colorbar ticks
cbar.ax.tick_params(labelsize=r*fs)
cbar.set_ticks([0, 0.5, 1.0, 1.5])

# For custom tick labels:
# cbar.set_ticklabels(['Low', 'Medium', 'High', 'Very High'])

# ============================================================================
# AXIS CONFIGURATION
# ============================================================================

# Set axis limits (for pcolormesh, this is automatic; for imshow, use extent)
ax.set_xlim(x.min(), x.max())
ax.set_ylim(y.min(), y.max())

# Set tick positions
ax.xaxis.set_ticks(np.arange(0, 11, 2))
ax.yaxis.set_ticks(np.arange(0, 11, 2))

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
# ANNOTATIONS (Optional)
# ============================================================================

# Mark specific points
# ax.plot(3, 3, 'ko', markersize=8)
# ax.text(3.2, 3.2, r'Peak 1', fontsize=r*fs, color='k')

# Add annotations with arrows
# ax.annotate('Maximum', xy=(3, 3), xytext=(5, 5),
#            arrowprops=dict(arrowstyle='->', lw=1.5, color='black'),
#            fontsize=r*fs)

# ============================================================================
# ASPECT RATIO
# ============================================================================

ratio = 1.0
ax.set_aspect(1.0/ax.get_data_ratio() * ratio)

# For equal aspect (square pixels):
# ax.set_aspect('equal')

# ============================================================================
# SAVE AND DISPLAY
# ============================================================================

output_filename = 'heatmap.pdf'
plt.savefig(output_filename, bbox_inches='tight', dpi=300)
plt.show()

# ============================================================================
# ADDITIONAL TIPS FOR HEATMAPS
# ============================================================================

# 1. Logarithmic color scale:
#    import matplotlib.colors as colors
#    heatmap = ax.pcolormesh(X, Y, Z, cmap=cmap,
#                           norm=colors.LogNorm(vmin=0.1, vmax=100))

# 2. Symmetric diverging colormap (centered at zero):
#    vmax = np.abs(Z).max()
#    heatmap = ax.pcolormesh(X, Y, Z, cmap='RdBu_r', 
#                           vmin=-vmax, vmax=vmax)

# 3. Discrete color levels:
#    import matplotlib.colors as colors
#    levels = [0, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5]
#    norm = colors.BoundaryNorm(levels, cmap.N)
#    heatmap = ax.pcolormesh(X, Y, Z, cmap=cmap, norm=norm)

# 4. Custom colormap:
#    import matplotlib.colors as mcolors
#    colors_list = ['blue', 'cyan', 'yellow', 'red']
#    n_bins = 100
#    cmap_custom = mcolors.LinearSegmentedColormap.from_list('custom', 
#                                                            colors_list, N=n_bins)

# 5. Add gridlines:
#    ax.grid(True, which='major', color='white', linestyle='-', linewidth=0.5, alpha=0.5)

# 6. For correlation matrix:
#    # Assuming data is correlation matrix
#    heatmap = ax.imshow(data, cmap='RdBu_r', vmin=-1, vmax=1)
#    # Add text annotations
#    for i in range(len(data)):
#        for j in range(len(data)):
#            text = ax.text(j, i, f'{data[i, j]:.2f}',
#                         ha="center", va="center", color="black")

# 7. Masked values (hide certain regions):
#    Z_masked = np.ma.masked_where(Z < 0.2, Z)
#    heatmap = ax.pcolormesh(X, Y, Z_masked, cmap=cmap)

# 8. Transparency based on another variable:
#    # Create alpha channel based on another 2D array
#    alpha_values = np.clip(Z / Z.max(), 0.3, 1.0)
#    # Note: alpha with pcolormesh is tricky; use imshow or multiple layers instead
