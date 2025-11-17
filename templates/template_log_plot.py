"""
TEMPLATE: Logarithmic Plots
============================
This template shows how to create plots with logarithmic axes.
Suitable for: Data spanning multiple orders of magnitude, power laws, exponential decay
"""

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import LogLocator, LogFormatterMathtext
import matplotlib.cm as cm
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

# Data spanning several orders of magnitude
x_log = np.logspace(-2, 2, 100)  # 10^-2 to 10^2

# Different functional forms
y_power_law = 10 * x_log**(-1.5)      # Power law: y ~ x^(-1.5)
y_exponential = 100 * np.exp(-0.5 * x_log)  # Exponential decay
y_linear = 5 * x_log + 2              # Linear in log-log

# For log-normal distribution
x_lin = np.linspace(0.01, 100, 1000)
y_lognormal = (1/(x_lin * 0.5 * np.sqrt(2*np.pi))) * \
              np.exp(-((np.log(x_lin) - 1)**2) / (2 * 0.5**2))

# ============================================================================
# PLOT STYLING PARAMETERS
# ============================================================================

fs = 24.0           # Font size
r = 0.9             # Tick label font ratio
linewidth = 2.0     # Line width

# ============================================================================
# LOG-LOG PLOT (Both axes logarithmic)
# ============================================================================

fig, ax = plt.subplots(figsize=(7.0, 6.0), dpi=50)

# Plot data
ax.plot(x_log, y_power_law, 'r-', linewidth=linewidth, 
       label=r'$y \sim x^{-1.5}$')
ax.plot(x_log, y_linear, 'b-', linewidth=linewidth,
       label=r'$y = 5x + 2$')

# Set both axes to logarithmic scale
ax.set_xscale('log')
ax.set_yscale('log')

# Set axis limits
ax.set_xlim(0.01, 100)
ax.set_ylim(0.1, 1000)

# Labels
ax.set_xlabel(r'$x$ variable (units)', fontsize=fs)
ax.set_ylabel(r'$y$ variable (units)', fontsize=fs)

# Legend
ax.legend(loc='upper right', fontsize=r*fs, frameon=True)

# Enable minor ticks (important for log scales)
ax.minorticks_on()

# Format tick labels
for tick in ax.get_xticklabels():
    tick.set_fontsize(r * fs)
for tick in ax.get_yticklabels():
    tick.set_fontsize(r * fs)

# Customize tick appearance
ax.tick_params(which='major', direction='in', length=10, width=1.5, colors='k')
ax.tick_params(which='minor', direction='in', length=5, width=1.5, colors='k')
ax.tick_params(which='both', top=True, right=True)

# Add grid (useful for log plots)
ax.grid(True, which='major', linestyle='-', linewidth=0.8, alpha=0.3)
ax.grid(True, which='minor', linestyle=':', linewidth=0.5, alpha=0.2)

# ============================================================================
# SEMI-LOG PLOT (Only Y-axis logarithmic) - Alternative
# ============================================================================

# Uncomment to create semi-log plot instead

# fig, ax = plt.subplots(figsize=(7.0, 6.0), dpi=50)
# 
# x_semilog = np.linspace(0, 10, 100)
# y_exp1 = 100 * np.exp(-0.5 * x_semilog)
# y_exp2 = 50 * np.exp(-0.3 * x_semilog)
# 
# ax.plot(x_semilog, y_exp1, 'r-', linewidth=linewidth, 
#        label=r'$y = 100e^{-0.5x}$')
# ax.plot(x_semilog, y_exp2, 'b-', linewidth=linewidth,
#        label=r'$y = 50e^{-0.3x}$')
# 
# # Only Y-axis is logarithmic
# ax.set_yscale('log')
# 
# ax.set_xlim(0, 10)
# ax.set_ylim(0.1, 200)
# 
# ax.set_xlabel(r'$x$ variable (units)', fontsize=fs)
# ax.set_ylabel(r'$y$ variable (units)', fontsize=fs)
# ax.legend(loc='upper right', fontsize=r*fs)

# ============================================================================
# LOGARITHMIC HEATMAP
# ============================================================================

# Uncomment to create log-scale heatmap

# fig, ax = plt.subplots(figsize=(7.0, 6.0), dpi=50)
# 
# # Create 2D data with log scales
# M, N = 250, 250
# x_2d = np.logspace(-2, 2, N)
# y_2d = np.logspace(-2, 2, M)
# X, Y = np.meshgrid(x_2d, y_2d)
# 
# # Calculate some function
# Z = (1 + X**3 * Y)  # Spans many orders of magnitude
# 
# # Create colormap
# cmap = copy.copy(cm.get_cmap("autumn_r"))
# 
# # Plot with logarithmic color scale
# import matplotlib.colors as colors
# 
# heatmap = ax.pcolormesh(X, Y, Z, 
#                        norm=colors.LogNorm(vmin=1, vmax=1e8),
#                        cmap=cmap, shading='gouraud')
# 
# # Set logarithmic axes
# ax.set_xscale('log')
# ax.set_yscale('log')
# 
# # Add colorbar with log scale
# cbar = fig.colorbar(heatmap, shrink=0.85)
# cbar.ax.tick_params(labelsize=r*fs)
# cbar.set_ticks(np.logspace(0, 8, 5))
# 
# # Add contour lines at specific levels
# contour_levels = [1, 10, 100, 1e4, 1e6, 1e8]
# contours = ax.contour(X, Y, Z, levels=contour_levels, 
#                      colors='k', linewidths=1.5)
# 
# ax.set_xlabel(r'$x$ variable', fontsize=fs)
# ax.set_ylabel(r'$y$ variable', fontsize=fs)

# ============================================================================
# CUSTOM TICK FORMATTING FOR LOG SCALES
# ============================================================================

# For custom major tick locations on log scale
# from matplotlib.ticker import FixedLocator
# ax.xaxis.set_major_locator(FixedLocator([0.01, 0.1, 1, 10, 100]))
# ax.yaxis.set_major_locator(FixedLocator([0.1, 1, 10, 100, 1000]))

# For scientific notation on log axes
# from matplotlib.ticker import LogFormatterSciNotation
# ax.xaxis.set_major_formatter(LogFormatterSciNotation())
# ax.yaxis.set_major_formatter(LogFormatterSciNotation())

# ============================================================================
# ASPECT RATIO
# ============================================================================

ratio = 1.0
ax.set_aspect(1.0/ax.get_data_ratio() * ratio)

# ============================================================================
# SAVE AND DISPLAY
# ============================================================================

output_filename = 'log_plot.pdf'
plt.savefig(output_filename, bbox_inches='tight', dpi=300)
plt.show()

# ============================================================================
# ADDITIONAL TIPS FOR LOGARITHMIC PLOTS
# ============================================================================

# 1. Symmetric log scale (includes negative values):
#    from matplotlib.scale import SymmetricalLogScale
#    ax.set_yscale('symlog', linthresh=0.1)  # Linear near zero
#    # Useful for data crossing zero

# 2. Log bins for histograms:
#    bins = np.logspace(np.log10(0.1), np.log10(100), 30)
#    ax.hist(data, bins=bins)
#    ax.set_xscale('log')

# 3. Minor tick formatting:
#    from matplotlib.ticker import NullFormatter
#    ax.xaxis.set_minor_formatter(NullFormatter())  # Hide minor tick labels
#    ax.yaxis.set_minor_formatter(NullFormatter())

# 4. Power law fit visualization:
#    # If you have power law data: y = A * x^alpha
#    # In log-log plot, this appears as straight line
#    # Slope = alpha, intercept = log(A)
#    
#    # Fit power law
#    log_x = np.log10(x_log)
#    log_y = np.log10(y_power_law)
#    coeffs = np.polyfit(log_x, log_y, 1)
#    alpha = coeffs[0]
#    A = 10**coeffs[1]
#    
#    # Plot fit
#    y_fit = A * x_log**alpha
#    ax.plot(x_log, y_fit, 'k--', linewidth=2,
#           label=f'Fit: $y = {A:.2f}x^{{{alpha:.2f}}}$')

# 5. Setting log scale base:
#    ax.set_xscale('log', base=2)  # Log base 2
#    ax.set_yscale('log', base=np.e)  # Natural log

# 6. Broken axis for log plots:
#    # When you need to skip a range
#    from matplotlib.patches import Rectangle
#    # Create two subplots with different y-ranges
#    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
#    ax1.set_yscale('log')
#    ax2.set_yscale('log')
#    ax1.set_ylim(100, 1000)
#    ax2.set_ylim(0.1, 10)

# 7. Reference lines on log plots:
#    # Power law reference
#    x_ref = np.array([0.1, 10])
#    y_ref = 10 * x_ref**(-2)
#    ax.plot(x_ref, y_ref, 'k--', linewidth=1.5, alpha=0.5,
#           label=r'$\sim x^{-2}$')

# 8. Annotations on log plots:
#    # Text at specific location
#    ax.text(1, 100, 'Important\nregion', fontsize=r*fs,
#           bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
#    
#    # Arrow in log space
#    ax.annotate('Transition', xy=(5, 10), xytext=(20, 50),
#               arrowprops=dict(arrowstyle='->', lw=2),
#               fontsize=r*fs)

# 9. Multiple log scales on same plot:
#    # Log-log plot with different bases
#    ax2 = ax.twiny()  # Create second x-axis
#    ax2.set_xscale('log', base=2)
#    ax2.set_xlabel('$x$ (log base 2)', fontsize=fs)

# 10. Verify log scale properties:
#     print(f"X-axis scale type: {ax.get_xscale()}")
#     print(f"Y-axis scale type: {ax.get_yscale()}")
