"""
================================================================================
SIMPLE X vs Y PLOTS
================================================================================
This file contains code to generate basic x vs y line plots for general
data visualization.

FIGURE TYPES:
    - Single line plot
    - Multiple lines on same axes
    - Line plot with markers
    - Scatter plot overlay
    
EXAMPLE FIGURES:
    - simple_xy.pdf: Basic x vs y plot
    - multi_line.pdf: Multiple data series
    - xy_with_markers.pdf: Line with data points

DATA REQUIREMENTS:
    - X-axis data array
    - Y-axis data array(s)
    
USAGE:
    1. Update data file path or create data arrays
    2. Adjust axis labels and ranges
    3. Run: python xy_plots.py
================================================================================
"""

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import os

# ============================================================================
# SETUP: LaTeX rendering and fonts for publication-quality figures
# ============================================================================
preamble = '\\usepackage{times}\n\\usepackage{newtxmath}\n\\usepackage{siunitx}\n'
plt.rc('text', usetex=True)
plt.rc('text.latex', preamble=preamble)
matplotlib.rcParams['font.serif'] = "Times New Roman"
matplotlib.rcParams['font.family'] = "serif"


# ============================================================================
# DATA LOADING: Load your data file OR create sample data
# ============================================================================
directory = os.getcwd()

# Option 1: Load from file
fname = 'your_data_file.dat'  # Update this path

# Try to load data from file
try:
    A = np.genfromtxt(fname, delimiter=',')
    print(f"Loaded data from {fname}")
    x_data = A[:, 0]  # First column as x
    y_data = A[:, 1]  # Second column as y
except:
    # Option 2: Generate sample data if file not found
    print(f"Warning: {fname} not found. Generating example data...")
    x_data = np.linspace(0, 10, 100)
    y_data = np.sin(x_data) * np.exp(-x_data/10)


# ============================================================================
# FIGURE 1: SIMPLE X vs Y LINE PLOT
# ============================================================================
figname = 'simple_xy.pdf'

# Plot settings
r = 0.9  # Font size ratio
fs = 24.0  # Font size
lwidth = 2.0  # Line width

# Create figure
fig, ax = plt.subplots(figsize=(6.5, 6.0), dpi=100)

# Plot x vs y
ax.plot(x_data, y_data, 'b', linewidth=lwidth)

# Set axis limits (adjust based on your data)
ax.set_xlim(x_data.min(), x_data.max())
ax.set_ylim(y_data.min() * 1.1, y_data.max() * 1.1)

# Set axis labels - MODIFY THESE for your data
ax.set_xlabel(r'X variable (units)', color='k', fontsize=fs)
ax.set_ylabel(r'Y variable (units)', color='k', fontsize=fs)

# Enable minor ticks
ax.minorticks_on()

# Format tick labels
for tick in ax.get_xticklabels():
    tick.set_fontsize(r * fs)
for tick in ax.get_yticklabels():
    tick.set_fontsize(r * fs)

# Tick parameters: inward pointing, major=10pt, minor=5pt
ax.tick_params(which='major', direction='in', length=10, width=1.5, colors='k')
ax.tick_params(which='minor', direction='in', length=5, width=1.5, colors='k')
ax.tick_params(which='both', top=False, right=False)

# if you want ticks on both right and top axis as well.
# ax.tick_params(which='both', top=True, right=True)

# Save figure
plt.savefig(figname, bbox_inches='tight', dpi=300)
plt.show()
print(f"Saved: {figname}")


# ============================================================================
# FIGURE 2: MULTIPLE LINES ON SAME PLOT
# ============================================================================
figname = 'multi_line.pdf'

# Create figure
fig, ax = plt.subplots(figsize=(6.5, 6.0), dpi=100)

# Generate or load multiple data series
# Replace with your actual data
y_data1 = np.sin(x_data)
y_data2 = np.cos(x_data)
y_data3 = np.sin(x_data) * 0.5

# Plot multiple lines with different colors
ax.plot(x_data, y_data1, 'r', linewidth=lwidth, label=r'Data 1')
ax.plot(x_data, y_data2, 'b', linewidth=lwidth, label=r'Data 2')
ax.plot(x_data, y_data3, 'g', linewidth=lwidth, label=r'Data 3')

# Set axis limits
ax.set_xlim(x_data.min(), x_data.max())

# Set axis labels
ax.set_xlabel(r'X variable (units)', color='k', fontsize=fs)
ax.set_ylabel(r'Y variable (units)', color='k', fontsize=fs)

# Enable minor ticks
ax.minorticks_on()

# Format tick labels
for tick in ax.get_xticklabels():
    tick.set_fontsize(r * fs)
for tick in ax.get_yticklabels():
    tick.set_fontsize(r * fs)

# Tick parameters
ax.tick_params(which='major', direction='in', length=10, width=1.5, colors='k')
ax.tick_params(which='minor', direction='in', length=5, width=1.5, colors='k')
ax.tick_params(which='both', top=False, right=False)

# Add legend
ax.legend(loc='upper right', shadow=False, fontsize=r*fs, frameon=False,
         ncol=1, columnspacing=0.8)

# Save figure
plt.savefig(figname, bbox_inches='tight', dpi=300)
plt.show()
print(f"Saved: {figname}")


# ============================================================================
# FIGURE 3: LINE PLOT WITH MARKERS
# ============================================================================
figname = 'xy_with_markers.pdf'

# Create figure
fig, ax = plt.subplots(figsize=(6.5, 6.0), dpi=100)

# Plot with markers at data points
# 'o' = circle, 's' = square, '^' = triangle, 'd' = diamond
ax.plot(x_data, y_data, 'bo-', linewidth=lwidth, markersize=6,
       markevery=5, label=r'Measured')  # Show marker every 5 points

# Set axis limits
ax.set_xlim(x_data.min(), x_data.max())
ax.set_ylim(y_data.min() * 1.1, y_data.max() * 1.1)

# Set axis labels
ax.set_xlabel(r'X variable (units)', color='k', fontsize=fs)
ax.set_ylabel(r'Y variable (units)', color='k', fontsize=fs)

# Enable minor ticks
ax.minorticks_on()

# Format tick labels
for tick in ax.get_xticklabels():
    tick.set_fontsize(r * fs)
for tick in ax.get_yticklabels():
    tick.set_fontsize(r * fs)

# Tick parameters
ax.tick_params(which='major', direction='in', length=10, width=1.5, colors='k')
ax.tick_params(which='minor', direction='in', length=5, width=1.5, colors='k')
ax.tick_params(which='both', top=False, right=False)

# Add legend
ax.legend(loc='best', shadow=False, fontsize=r*fs, frameon=False)

# Save figure
plt.savefig(figname, bbox_inches='tight', dpi=300)
plt.show()
print(f"Saved: {figname}")


# ============================================================================
# FIGURE 4: SCATTER PLOT WITH LINE FIT
# ============================================================================
figname = 'xy_scatter_fit.pdf'

# Create figure
fig, ax = plt.subplots(figsize=(6.5, 6.0), dpi=100)

# Scatter plot of raw data
ax.scatter(x_data, y_data, s=50, c='red', alpha=0.6, 
          edgecolors='black', linewidth=0.5, label=r'Data')

# Optional: Add polynomial fit line
# Fit a polynomial (degree 2 for quadratic)
coeffs = np.polyfit(x_data, y_data, 2)
fit_func = np.poly1d(coeffs)
y_fit = fit_func(x_data)

# Plot fit line
ax.plot(x_data, y_fit, 'b-', linewidth=lwidth, label=r'Fit')

# Set axis limits
ax.set_xlim(x_data.min(), x_data.max())

# Set axis labels
ax.set_xlabel(r'X variable (units)', color='k', fontsize=fs)
ax.set_ylabel(r'Y variable (units)', color='k', fontsize=fs)

# Enable minor ticks
ax.minorticks_on()

# Format tick labels
for tick in ax.get_xticklabels():
    tick.set_fontsize(r * fs)
for tick in ax.get_yticklabels():
    tick.set_fontsize(r * fs)

# Tick parameters
ax.tick_params(which='major', direction='in', length=10, width=1.5, colors='k')
ax.tick_params(which='minor', direction='in', length=5, width=1.5, colors='k')
ax.tick_params(which='both', top=False, right=False)

# Add legend
ax.legend(loc='best', shadow=False, fontsize=r*fs, frameon=False)

# Add grid for readability
ax.grid(alpha=0.3, linestyle='--')

# Save figure
plt.savefig(figname, bbox_inches='tight', dpi=300)
plt.show()
print(f"Saved: {figname}")


# ============================================================================
# FIGURE 5: CUSTOM TICKS AND LABELS
# ============================================================================
figname = 'xy_custom_ticks.pdf'

# Create figure
fig, ax = plt.subplots(figsize=(6.5, 6.0), dpi=100)

# Plot data
ax.plot(x_data, y_data, 'k', linewidth=lwidth)

# Custom tick positions
x_ticks = np.linspace(x_data.min(), x_data.max(), 6)
y_ticks = np.linspace(y_data.min(), y_data.max(), 6)

ax.set_xticks(x_ticks)
ax.set_yticks(y_ticks)

# Set specific axis ranges
ax.set_xlim(0, 10)
ax.set_ylim(-0.5, 1.0)

# Set axis labels
ax.set_xlabel(r'X variable (units)', color='k', fontsize=fs)
ax.set_ylabel(r'Y variable (units)', color='k', fontsize=fs)

# Enable minor ticks
ax.minorticks_on()

# Format tick labels
for tick in ax.get_xticklabels():
    tick.set_fontsize(r * fs)
for tick in ax.get_yticklabels():
    tick.set_fontsize(r * fs)

# Tick parameters
ax.tick_params(which='major', direction='in', length=10, width=1.5, colors='k')
ax.tick_params(which='minor', direction='in', length=5, width=1.5, colors='k')
ax.tick_params(which='both', top=False, right=False)

# Add reference lines (optional)
ax.axhline(y=0, color='gray', linestyle='--', linewidth=1, alpha=0.5)
ax.axvline(x=5, color='gray', linestyle='--', linewidth=1, alpha=0.5)

# Save figure
plt.savefig(figname, bbox_inches='tight', dpi=300)
plt.show()
print(f"Saved: {figname}")


# ============================================================================
# NOTES FOR CUSTOMIZATION
# ============================================================================
"""
TO CUSTOMIZE FOR YOUR DATA:

1. LOAD YOUR DATA:
   Option A - From file:
   fname = 'your_data.csv'
   A = np.genfromtxt(fname, delimiter=',')
   x_data = A[:, 0]
   y_data = A[:, 1]
   
   Option B - Create arrays:
   x_data = np.array([1, 2, 3, 4, 5])
   y_data = np.array([2, 4, 6, 8, 10])

2. CHANGE COLORS:
   'r' = red
   'b' = blue
   'g' = green
   'k' = black
   'c' = cyan
   'm' = magenta
   'y' = yellow
   Or use hex: '#FF5733'

3. LINE STYLES:
   '-'  = solid line
   '--' = dashed line
   ':'  = dotted line
   '-.' = dash-dot line

4. MARKER STYLES:
   'o' = circle
   's' = square
   '^' = triangle up
   'v' = triangle down
   'd' = diamond
   '*' = star
   '+' = plus
   'x' = x-mark

5. AXIS RANGES:
   ax.set_xlim(xmin, xmax)
   ax.set_ylim(ymin, ymax)

6. AXIS LABELS:
   Regular text: ax.set_xlabel('Time (s)', fontsize=fs)
   LaTeX math: ax.set_xlabel(r'$\alpha$ (degrees)', fontsize=fs)
   Units: ax.set_xlabel(r'Temperature (\SI{}{\degreeCelsius})', fontsize=fs)

7. LEGEND POSITION:
   loc='upper right', 'upper left', 'lower right', 'lower left'
   loc='center', 'best' (auto-position)

8. GRID:
   ax.grid(True)  # Show grid
   ax.grid(alpha=0.3, linestyle='--')  # Transparent dashed grid

9. SAVE FORMATS:
   .pdf - Vector graphics (recommended for papers)
   .png - Raster graphics (for presentations)
   .svg - Vector graphics (for web/editing)

10. MULTIPLE Y-AXES:
    ax2 = ax.twinx()
    ax2.plot(x_data, y_data2, 'r')
    ax2.set_ylabel(r'Second Y variable', color='r')

11. LOG SCALE:
    ax.set_xscale('log')
    ax.set_yscale('log')

12. ERROR BARS:
    ax.errorbar(x_data, y_data, yerr=errors, capsize=5)

13. FILL BETWEEN:
    ax.fill_between(x_data, y_lower, y_upper, alpha=0.3)

14. ANNOTATIONS:
    ax.annotate('Important point', xy=(x, y), 
               xytext=(x+1, y+1), arrowprops=dict(arrowstyle='->'))

15. DISABLE LaTeX (if not installed):
    Comment out:
    # plt.rc('text', usetex=True)
    # plt.rc('text.latex', preamble=preamble)
"""
