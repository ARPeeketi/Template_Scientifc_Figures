"""
TEMPLATE: Multiple Subplots
============================
This template shows how to create figures with multiple subplots.
Suitable for: Comparing multiple datasets, showing different aspects of data
"""

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import matplotlib.gridspec as gridspec

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
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(2*x)
y4 = np.exp(-0.3*x) * np.sin(x)

# For heatmap
X, Y = np.meshgrid(np.linspace(0, 5, 50), np.linspace(0, 5, 50))
Z = np.sin(X) * np.cos(Y)

# ============================================================================
# PLOT STYLING PARAMETERS
# ============================================================================

fs = 20.0           # Font size (smaller for subplots)
r = 0.9             # Tick label font ratio
linewidth = 2.0     # Line width

# ============================================================================
# METHOD 1: SIMPLE GRID (2x2 or similar regular grids)
# ============================================================================

# Create figure with 2 rows and 2 columns
fig, axes = plt.subplots(2, 2, figsize=(12, 10), dpi=50)

# Access individual subplots
# axes[row, column] for 2D array
# axes[index] for 1D array (single row or column)

# -------- Subplot 1: Top-left (axes[0, 0]) --------
ax = axes[0, 0]
ax.plot(x, y1, 'r-', linewidth=linewidth, label=r'sin($x$)')
ax.plot(x, y2, 'b-', linewidth=linewidth, label=r'cos($x$)')

ax.set_xlim(0, 10)
ax.set_ylim(-1.5, 1.5)
ax.set_xlabel(r'$x$ (units)', fontsize=fs)
ax.set_ylabel(r'$y$ (units)', fontsize=fs)
ax.legend(loc='upper right', fontsize=0.8*fs)
ax.grid(True, alpha=0.3)

# Add subplot label
ax.text(0.05, 0.95, '(a)', transform=ax.transAxes, 
       fontsize=fs, fontweight='bold', va='top')

# -------- Subplot 2: Top-right (axes[0, 1]) --------
ax = axes[0, 1]
scatter = ax.scatter(x, y3, c=x, cmap='viridis', s=30, alpha=0.7)

ax.set_xlim(0, 10)
ax.set_ylim(-1.5, 1.5)
ax.set_xlabel(r'$x$ (units)', fontsize=fs)
ax.set_ylabel(r'$y$ (units)', fontsize=fs)

# Add colorbar
cbar = plt.colorbar(scatter, ax=ax, shrink=0.8)
cbar.set_label(r'$x$ value', fontsize=0.8*fs)

ax.text(0.05, 0.95, '(b)', transform=ax.transAxes,
       fontsize=fs, fontweight='bold', va='top')

# -------- Subplot 3: Bottom-left (axes[1, 0]) --------
ax = axes[1, 0]
categories = ['A', 'B', 'C', 'D']
values = [25, 32, 28, 35]

ax.bar(categories, values, color='steelblue', edgecolor='black', 
      linewidth=1.5, alpha=0.7)

ax.set_ylabel(r'Value (units)', fontsize=fs)
ax.set_ylim(0, 40)

ax.text(0.05, 0.95, '(c)', transform=ax.transAxes,
       fontsize=fs, fontweight='bold', va='top')

# -------- Subplot 4: Bottom-right (axes[1, 1]) --------
ax = axes[1, 1]
contourf = ax.contourf(X, Y, Z, levels=15, cmap='coolwarm')

ax.set_xlabel(r'$x$ (units)', fontsize=fs)
ax.set_ylabel(r'$y$ (units)', fontsize=fs)
ax.set_aspect('equal')

cbar = plt.colorbar(contourf, ax=ax, shrink=0.8)
cbar.set_label(r'$Z$ value', fontsize=0.8*fs)

ax.text(0.05, 0.95, '(d)', transform=ax.transAxes,
       fontsize=fs, fontweight='bold', va='top', color='white')

# Format all subplots
for ax in axes.flat:
    ax.minorticks_on()
    ax.tick_params(which='major', direction='in', length=8, width=1.2)
    ax.tick_params(which='minor', direction='in', length=4, width=1.2)
    ax.tick_params(which='both', top=True, right=True)
    
    for tick in ax.get_xticklabels():
        tick.set_fontsize(r * fs)
    for tick in ax.get_yticklabels():
        tick.set_fontsize(r * fs)

# Adjust spacing between subplots
plt.tight_layout()
# Or manually: plt.subplots_adjust(hspace=0.3, wspace=0.3)

# ============================================================================
# METHOD 2: CUSTOM GRID LAYOUT (using GridSpec)
# ============================================================================

# Uncomment to use this method instead

# fig = plt.figure(figsize=(12, 10), dpi=50)
# gs = gridspec.GridSpec(3, 3, figure=fig, hspace=0.3, wspace=0.3)
# 
# # Large subplot spanning 2 columns
# ax1 = fig.add_subplot(gs[0, :2])  # Row 0, columns 0-1
# ax1.plot(x, y1, 'r-', linewidth=linewidth)
# ax1.set_title('Large subplot (2 columns)', fontsize=fs)
# 
# # Small subplot
# ax2 = fig.add_subplot(gs[0, 2])   # Row 0, column 2
# ax2.plot(x, y2, 'b-', linewidth=linewidth)
# ax2.set_title('Small subplot', fontsize=fs)
# 
# # Wide subplot spanning all columns
# ax3 = fig.add_subplot(gs[1, :])   # Row 1, all columns
# ax3.plot(x, y3, 'g-', linewidth=linewidth)
# ax3.set_title('Wide subplot (3 columns)', fontsize=fs)
# 
# # Two regular subplots
# ax4 = fig.add_subplot(gs[2, 0])   # Row 2, column 0
# ax4.plot(x, y4, 'm-', linewidth=linewidth)
# 
# ax5 = fig.add_subplot(gs[2, 1:])  # Row 2, columns 1-2
# ax5.scatter(x, y1, c=x, cmap='viridis')

# ============================================================================
# METHOD 3: SHARED AXES
# ============================================================================

# Uncomment to use this method

# fig, axes = plt.subplots(2, 2, figsize=(12, 10), dpi=50,
#                         sharex='col',  # Share x-axis within columns
#                         sharey='row')  # Share y-axis within rows
# 
# # Or share all: sharex='all', sharey='all'
# 
# # Plot data on each subplot
# axes[0, 0].plot(x, y1, 'r-')
# axes[0, 1].plot(x, y2, 'b-')
# axes[1, 0].plot(x, y3, 'g-')
# axes[1, 1].plot(x, y4, 'm-')
# 
# # Only label bottom row for x
# axes[1, 0].set_xlabel(r'$x$ (units)', fontsize=fs)
# axes[1, 1].set_xlabel(r'$x$ (units)', fontsize=fs)
# 
# # Only label left column for y
# axes[0, 0].set_ylabel(r'$y$ (units)', fontsize=fs)
# axes[1, 0].set_ylabel(r'$y$ (units)', fontsize=fs)

# ============================================================================
# METHOD 4: SUBPLOTS WITH DIFFERENT SIZES
# ============================================================================

# Uncomment to use this method

# fig = plt.figure(figsize=(12, 10), dpi=50)
# 
# # Define grid: rows, columns, index (1-based)
# ax1 = plt.subplot(2, 2, 1)  # Top-left
# ax2 = plt.subplot(2, 2, 2)  # Top-right
# ax3 = plt.subplot(2, 1, 2)  # Bottom (spans both columns)
# 
# ax1.plot(x, y1, 'r-')
# ax2.plot(x, y2, 'b-')
# ax3.plot(x, y3, 'g-')
# 
# plt.tight_layout()

# ============================================================================
# INSET PLOT (Plot within a plot)
# ============================================================================

# Uncomment to add an inset to subplot (a)

# from mpl_toolkits.axes_grid1.inset_locator import inset_axes
# 
# ax_main = axes[0, 0]
# 
# # Create inset axes
# # Position: [x, y, width, height] in axes coordinates (0-1)
# ax_inset = ax_main.inset_axes([0.55, 0.55, 0.4, 0.4])
# 
# # Plot zoomed region
# x_zoom = x[(x > 2) & (x < 4)]
# y1_zoom = y1[(x > 2) & (x < 4)]
# ax_inset.plot(x_zoom, y1_zoom, 'r-', linewidth=linewidth)
# 
# # Mark zoomed region on main plot
# ax_main.indicate_inset_zoom(ax_inset, edgecolor='black', linewidth=2)
# 
# # Format inset
# ax_inset.tick_params(labelsize=0.6*fs)

# ============================================================================
# SAVE AND DISPLAY
# ============================================================================

output_filename = 'subplots.pdf'
plt.savefig(output_filename, bbox_inches='tight', dpi=300)
plt.show()

# ============================================================================
# ADDITIONAL TIPS FOR SUBPLOTS
# ============================================================================

# 1. Single row or column:
#    fig, axes = plt.subplots(1, 3, figsize=(15, 5))  # 1 row, 3 columns
#    fig, axes = plt.subplots(3, 1, figsize=(5, 15))  # 3 rows, 1 column

# 2. Accessing flattened axes:
#    for i, ax in enumerate(axes.flat):
#        ax.plot(x, data[i])

# 3. Different subplot sizes with width/height ratios:
#    fig, axes = plt.subplots(1, 2, figsize=(12, 5),
#                            gridspec_kw={'width_ratios': [2, 1]})

# 4. Remove unused subplots:
#    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
#    fig.delaxes(axes[1, 2])  # Remove bottom-right subplot

# 5. Common colorbar for multiple subplots:
#    # After creating all contourf plots with same levels/cmap
#    fig.colorbar(contourf, ax=axes.ravel().tolist(), 
#                shrink=0.6, aspect=30)

# 6. Super title for entire figure:
#    fig.suptitle('Main Figure Title', fontsize=1.2*fs, fontweight='bold', y=0.98)

# 7. Subplot labels (a, b, c, ...):
#    labels = ['(a)', '(b)', '(c)', '(d)']
#    for ax, label in zip(axes.flat, labels):
#        ax.text(0.05, 0.95, label, transform=ax.transAxes,
#               fontsize=fs, fontweight='bold', va='top')

# 8. Share specific axes:
#    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
#    # ax1 and ax2 now share x-axis

# 9. Complex layouts with GridSpecFromSubplotSpec:
#    from matplotlib.gridspec import GridSpecFromSubplotSpec
#    fig = plt.figure(figsize=(12, 10))
#    gs = gridspec.GridSpec(2, 2)
#    # Subdivide one subplot
#    gs_sub = GridSpecFromSubplotSpec(2, 2, subplot_spec=gs[0, 0])
#    ax1 = fig.add_subplot(gs_sub[0, 0])
#    ax2 = fig.add_subplot(gs_sub[0, 1])
#    # etc.
