"""
TEMPLATE: Filled Contour Plot
==============================
This template shows how to create filled contour plots with contour lines.
Suitable for: Topographic data, scalar fields, level sets, parameter landscapes
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

# Create coordinate arrays
M = 150  # Resolution in y-direction
N = 150  # Resolution in x-direction

x = np.linspace(-3, 3, N)
y = np.linspace(-3, 3, M)

# Create 2D meshgrid
X, Y = np.meshgrid(x, y)

# Generate 2D data
# Example: Multiple Gaussian peaks creating a landscape
Z = (2.0 * np.exp(-((X-1)**2 + (Y-1)**2)/0.5) + 
     1.5 * np.exp(-((X+1)**2 + (Y+1)**2)/0.8) +
     1.0 * np.exp(-((X-0.5)**2 + (Y+0.5)**2)/0.3) -
     0.5 * np.exp(-((X)**2 + (Y)**2)/2))

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
# DEFINE CONTOUR LEVELS
# ============================================================================

# Option 1: Automatic levels
n_levels = 15
levels = np.linspace(Z.min(), Z.max(), n_levels)

# Option 2: Custom levels
# levels = [-1, -0.5, 0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0]

# Option 3: Logarithmic levels
# levels = np.logspace(-1, 1, 10)

# ============================================================================
# CREATE FILLED CONTOURS
# ============================================================================

# Create filled contour plot
# cmap options: 'viridis', 'plasma', 'coolwarm', 'RdBu', 'RdYlBu', 'jet', 'rainbow'
# extend options: 'neither', 'both', 'min', 'max'
#   'both' adds triangular extensions for values outside level range

contourf = ax.contourf(X, Y, Z, levels=levels, cmap='coolwarm', 
                       extend='both', alpha=0.9)

# For smooth interpolation:
# contourf = ax.contourf(X, Y, Z, levels=100, cmap='viridis', extend='both')

# ============================================================================
# ADD CONTOUR LINES
# ============================================================================

# Add contour lines on top of filled contours
# Choose subset of levels for lines (every 2nd or 3rd level)
line_levels = levels[::2]  # Every other level

contours = ax.contour(X, Y, Z, levels=line_levels, colors='k', 
                     linewidths=linewidth, linestyles='solid')

# Add labels to contour lines
ax.clabel(contours, inline=True, fontsize=0.6*fs, fmt='%0.1f',
          inline_spacing=5)

# For specific line styles at different levels:
# contours_pos = ax.contour(X, Y, Z, levels=[0.5, 1.0, 1.5], 
#                          colors='k', linewidths=2, linestyles='solid')
# contours_neg = ax.contour(X, Y, Z, levels=[-1.0, -0.5], 
#                          colors='gray', linewidths=1.5, linestyles='dashed')

# ============================================================================
# HIGHLIGHT SPECIFIC CONTOUR
# ============================================================================

# Highlight a specific contour (e.g., zero level)
# highlight = ax.contour(X, Y, Z, levels=[0], colors='white', 
#                       linewidths=3, linestyles='solid')

# ============================================================================
# COLORBAR
# ============================================================================

# Add colorbar
cbar = fig.colorbar(contourf, shrink=0.85, pad=0.02, 
                   spacing='proportional', extend='both')

# Set colorbar label
cbar.set_label(r'$Z$ value (units)', fontsize=fs, labelpad=10)

# Customize colorbar ticks
cbar.ax.tick_params(labelsize=r*fs)

# Set specific ticks
# cbar.set_ticks([-1, 0, 1, 2, 3])

# For many levels, reduce number of tick labels:
# tick_locator = matplotlib.ticker.MaxNLocator(nbins=5)
# cbar.locator = tick_locator
# cbar.update_ticks()

# ============================================================================
# AXIS CONFIGURATION
# ============================================================================

# Set axis limits
ax.set_xlim(x.min(), x.max())
ax.set_ylim(y.min(), y.max())

# Set tick positions
ax.xaxis.set_ticks(np.arange(-3, 3.1, 1))
ax.yaxis.set_ticks(np.arange(-3, 3.1, 1))

# Enable minor ticks
ax.minorticks_on()

# Set labels
ax.set_xlabel(r'$x$ coordinate (units)', color='k', fontsize=fs)
ax.set_ylabel(r'$y$ coordinate (units)', color='k', fontsize=fs)

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

# Mark maxima/minima
# Find peak
# idx_max = np.unravel_index(np.argmax(Z), Z.shape)
# x_max, y_max = X[idx_max], Y[idx_max]
# ax.plot(x_max, y_max, 'k*', markersize=15)
# ax.text(x_max + 0.2, y_max, 'Maximum', fontsize=r*fs)

# Add text annotation
# ax.text(-2, 2.5, r'Region A', fontsize=r*fs, color='white',
#        bbox=dict(boxstyle='round', facecolor='black', alpha=0.5))

# ============================================================================
# ASPECT RATIO
# ============================================================================

ratio = 1.0
ax.set_aspect(1.0/ax.get_data_ratio() * ratio)

# For equal aspect (preserves distances):
# ax.set_aspect('equal')

# ============================================================================
# SAVE AND DISPLAY
# ============================================================================

output_filename = 'contour_plot.pdf'
plt.savefig(output_filename, bbox_inches='tight', dpi=300)
plt.show()

# ============================================================================
# ADDITIONAL TIPS FOR CONTOUR PLOTS
# ============================================================================

# 1. Hatching patterns between levels:
#    contourf = ax.contourf(X, Y, Z, levels=levels, 
#                          hatches=['/', '\\', '|', '-', '+', 'x', 'o', 'O', '.', '*'],
#                          cmap='Blues', alpha=0.5)

# 2. Tricontour for irregular data:
#    from matplotlib.tri import Triangulation
#    # Assuming x, y, z are 1D arrays of scattered points
#    triangulation = Triangulation(x, y)
#    ax.tricontourf(triangulation, z, levels=levels, cmap='viridis')

# 3. Custom colormap with discrete levels:
#    import matplotlib.colors as mcolors
#    colors_list = ['blue', 'cyan', 'green', 'yellow', 'red']
#    n_bins = len(levels) - 1
#    cmap = mcolors.ListedColormap(colors_list)
#    norm = mcolors.BoundaryNorm(levels, cmap.N)
#    contourf = ax.contourf(X, Y, Z, levels=levels, cmap=cmap, norm=norm)

# 4. Fill between two contour levels:
#    level_low = 0.5
#    level_high = 1.5
#    ax.contourf(X, Y, Z, levels=[level_low, level_high], 
#               colors=['lightblue'], alpha=0.5)

# 5. Negative contours with dashed lines:
#    pos_levels = levels[levels >= 0]
#    neg_levels = levels[levels < 0]
#    ax.contour(X, Y, Z, levels=pos_levels, colors='k', linestyles='solid')
#    ax.contour(X, Y, Z, levels=neg_levels, colors='k', linestyles='dashed')

# 6. Add gradient/quiver plot overlay:
#    # Calculate gradient
#    dy, dx = np.gradient(Z)
#    # Subsample for clarity
#    skip = 10
#    ax.quiver(X[::skip, ::skip], Y[::skip, ::skip],
#             dx[::skip, ::skip], dy[::skip, ::skip],
#             color='white', alpha=0.7)

# 7. For topographic/elevation maps:
#    # Use terrain-like colormap
#    contourf = ax.contourf(X, Y, Z, levels=20, cmap='terrain')
#    # Add hillshade effect
#    from matplotlib.colors import LightSource
#    ls = LightSource(azdeg=315, altdeg=45)
#    rgb = ls.shade(Z, cmap=cm.terrain, blend_mode='soft')
#    ax.imshow(rgb, extent=[x.min(), x.max(), y.min(), y.max()], origin='lower')

# 8. Save contour data:
#    # Extract contour paths for further processing
#    for collection in contours.collections:
#        for path in collection.get_paths():
#            vertices = path.vertices
#            # Process vertices as needed
