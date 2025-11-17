"""
TEMPLATE: Histograms and Error Bar Plots
=========================================
This template shows how to create histograms and plots with error bars.
Suitable for: Distributions, statistical data, experimental measurements
"""

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
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

# Sample data for histograms
np.random.seed(42)
data_normal = np.random.normal(loc=5, scale=2, size=1000)
data_uniform = np.random.uniform(low=0, high=10, size=500)
data_exponential = np.random.exponential(scale=2, size=1000)

# Data for error bar plots
x_err = np.linspace(0, 10, 20)
y_err = 2 * x_err + 5 + np.random.randn(20) * 2
y_error = np.abs(np.random.randn(20)) * 1.5  # Error magnitude
x_error = np.abs(np.random.randn(20)) * 0.3  # Optional x errors

# ============================================================================
# PLOT STYLING PARAMETERS
# ============================================================================

fs = 24.0           # Font size
r = 0.9             # Tick label font ratio
linewidth = 2.0     # Line width

# ============================================================================
# SIMPLE HISTOGRAM
# ============================================================================

fig, ax = plt.subplots(figsize=(7.0, 6.0), dpi=50)

# Create histogram
# bins: number of bins or array of bin edges
# density: if True, normalize to probability density
# cumulative: if True, create cumulative histogram
# histtype: 'bar', 'barstacked', 'step', 'stepfilled'

n, bins, patches = ax.hist(data_normal, bins=30, 
                           density=False, 
                           alpha=0.7, 
                           color='steelblue',
                           edgecolor='black',
                           linewidth=1.2)

# Add mean and standard deviation lines
mean_val = np.mean(data_normal)
std_val = np.std(data_normal)

ax.axvline(mean_val, color='red', linestyle='--', linewidth=2,
          label=f'Mean = {mean_val:.2f}')
ax.axvline(mean_val - std_val, color='orange', linestyle=':', linewidth=2)
ax.axvline(mean_val + std_val, color='orange', linestyle=':', linewidth=2,
          label=f'$\pm1\sigma$ = {std_val:.2f}')

# Labels
ax.set_xlabel(r'Value (units)', fontsize=fs)
ax.set_ylabel(r'Frequency', fontsize=fs)
ax.legend(loc='upper right', fontsize=r*fs, frameon=True)

# ============================================================================
# OVERLAPPING HISTOGRAMS (Multiple datasets)
# ============================================================================

# Uncomment to create overlapping histograms

# fig, ax = plt.subplots(figsize=(7.0, 6.0), dpi=50)
# 
# # Define common bins for fair comparison
# bins_common = np.linspace(0, 12, 25)
# 
# ax.hist(data_normal, bins=bins_common, alpha=0.6, 
#        label='Normal', color='blue', edgecolor='black', linewidth=1)
# ax.hist(data_exponential, bins=bins_common, alpha=0.6, 
#        label='Exponential', color='red', edgecolor='black', linewidth=1)
# 
# ax.set_xlabel(r'Value (units)', fontsize=fs)
# ax.set_ylabel(r'Frequency', fontsize=fs)
# ax.legend(loc='upper right', fontsize=r*fs)

# ============================================================================
# STEP HISTOGRAM (Good for comparisons)
# ============================================================================

# Uncomment to create step histogram

# fig, ax = plt.subplots(figsize=(7.0, 6.0), dpi=50)
# 
# ax.hist(data_normal, bins=30, histtype='step', 
#        linewidth=2.5, color='blue', label='Normal')
# ax.hist(data_exponential, bins=30, histtype='step',
#        linewidth=2.5, color='red', label='Exponential')
# 
# ax.set_xlabel(r'Value (units)', fontsize=fs)
# ax.set_ylabel(r'Frequency', fontsize=fs)
# ax.legend(loc='upper right', fontsize=r*fs)

# ============================================================================
# NORMALIZED HISTOGRAM (Probability density)
# ============================================================================

# Uncomment for probability density histogram

# fig, ax = plt.subplots(figsize=(7.0, 6.0), dpi=50)
# 
# n, bins, patches = ax.hist(data_normal, bins=30, density=True,
#                           alpha=0.7, color='steelblue',
#                           edgecolor='black')
# 
# # Overlay theoretical distribution
# from scipy import stats
# x_theory = np.linspace(data_normal.min(), data_normal.max(), 100)
# y_theory = stats.norm.pdf(x_theory, loc=mean_val, scale=std_val)
# ax.plot(x_theory, y_theory, 'r-', linewidth=2.5,
#        label='Normal PDF')
# 
# ax.set_xlabel(r'Value (units)', fontsize=fs)
# ax.set_ylabel(r'Probability density', fontsize=fs)
# ax.legend(loc='upper right', fontsize=r*fs)

# ============================================================================
# CUMULATIVE HISTOGRAM
# ============================================================================

# Uncomment for cumulative histogram

# fig, ax = plt.subplots(figsize=(7.0, 6.0), dpi=50)
# 
# ax.hist(data_normal, bins=30, cumulative=True,
#        alpha=0.7, color='steelblue', edgecolor='black',
#        label='Cumulative distribution')
# 
# ax.set_xlabel(r'Value (units)', fontsize=fs)
# ax.set_ylabel(r'Cumulative frequency', fontsize=fs)
# ax.legend(loc='upper left', fontsize=r*fs)

# ============================================================================
# 2D HISTOGRAM (HEATMAP)
# ============================================================================

# Uncomment for 2D histogram

# fig, ax = plt.subplots(figsize=(7.0, 6.0), dpi=50)
# 
# # Generate 2D data
# x_2d = np.random.normal(5, 2, 5000)
# y_2d = np.random.normal(5, 2, 5000)
# 
# # Create 2D histogram
# hist2d = ax.hist2d(x_2d, y_2d, bins=30, cmap='YlOrRd',
#                   cmin=1)  # Don't show bins with 0 counts
# 
# # Add colorbar
# cbar = plt.colorbar(hist2d[3], ax=ax, shrink=0.85)
# cbar.set_label(r'Count', fontsize=fs)
# cbar.ax.tick_params(labelsize=r*fs)
# 
# ax.set_xlabel(r'$x$ variable', fontsize=fs)
# ax.set_ylabel(r'$y$ variable', fontsize=fs)
# ax.set_aspect('equal')

# ============================================================================
# ERROR BAR PLOT
# ============================================================================

# Uncomment to create error bar plot instead of histogram

# fig, ax = plt.subplots(figsize=(7.0, 6.0), dpi=50)
# 
# # Plot with error bars
# # yerr: y-direction errors (scalar, array, or [lower, upper])
# # xerr: x-direction errors (optional)
# # fmt: format string for markers and lines
# # capsize: length of error bar caps
# # capthick: thickness of error bar caps
# # elinewidth: error bar line width
# 
# ax.errorbar(x_err, y_err, yerr=y_error, xerr=x_error,
#            fmt='o', color='blue', markersize=8,
#            ecolor='black', elinewidth=1.5,
#            capsize=5, capthick=1.5,
#            label='Data with errors')
# 
# # Add trend line
# z = np.polyfit(x_err, y_err, 1)
# p = np.poly1d(z)
# ax.plot(x_err, p(x_err), 'r--', linewidth=2,
#        label=f'Fit: $y = {z[0]:.2f}x + {z[1]:.2f}$')
# 
# ax.set_xlim(0, 10)
# ax.set_xlabel(r'$x$ variable (units)', fontsize=fs)
# ax.set_ylabel(r'$y$ variable (units)', fontsize=fs)
# ax.legend(loc='upper left', fontsize=r*fs)

# ============================================================================
# ASYMMETRIC ERROR BARS
# ============================================================================

# Uncomment for asymmetric error bars

# fig, ax = plt.subplots(figsize=(7.0, 6.0), dpi=50)
# 
# # Different upper and lower errors
# y_error_lower = np.abs(np.random.randn(20)) * 1.0
# y_error_upper = np.abs(np.random.randn(20)) * 2.0
# 
# # Format: [lower_errors, upper_errors]
# yerr_asym = [y_error_lower, y_error_upper]
# 
# ax.errorbar(x_err, y_err, yerr=yerr_asym,
#            fmt='s', color='red', markersize=8,
#            ecolor='black', elinewidth=1.5,
#            capsize=5, capthick=1.5)
# 
# ax.set_xlabel(r'$x$ variable', fontsize=fs)
# ax.set_ylabel(r'$y$ variable', fontsize=fs)

# ============================================================================
# TICK FORMATTING
# ============================================================================

# Format tick labels
for tick in ax.get_xticklabels():
    tick.set_fontsize(r * fs)
for tick in ax.get_yticklabels():
    tick.set_fontsize(r * fs)

# Enable minor ticks
ax.minorticks_on()

# Customize tick appearance
ax.tick_params(which='major', direction='in', length=10, width=1.5, colors='k')
ax.tick_params(which='minor', direction='in', length=5, width=1.5, colors='k')
ax.tick_params(which='both', top=True, right=True)

# Optional: Add grid
# ax.grid(True, which='major', alpha=0.3)

# ============================================================================
# SAVE AND DISPLAY
# ============================================================================

output_filename = 'histogram.pdf'
plt.savefig(output_filename, bbox_inches='tight', dpi=300)
plt.show()

# ============================================================================
# ADDITIONAL TIPS
# ============================================================================

# 1. Custom bin edges:
#    bins = [0, 2, 4, 6, 8, 10, 15, 20]  # Non-uniform bins
#    ax.hist(data, bins=bins)

# 2. Log-scale bins for wide-range data:
#    bins = np.logspace(np.log10(0.1), np.log10(100), 30)
#    ax.hist(data, bins=bins)
#    ax.set_xscale('log')

# 3. Stacked histograms:
#    ax.hist([data1, data2, data3], bins=30, stacked=True,
#           label=['A', 'B', 'C'], alpha=0.7)

# 4. Weighted histogram:
#    weights = np.ones_like(data) / len(data)  # Normalize
#    ax.hist(data, bins=30, weights=weights)

# 5. Bar histogram (manually):
#    counts, bin_edges = np.histogram(data, bins=30)
#    bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2
#    ax.bar(bin_centers, counts, width=np.diff(bin_edges),
#          edgecolor='black', alpha=0.7)

# 6. Statistical annotations:
#    median_val = np.median(data)
#    q25, q75 = np.percentile(data, [25, 75])
#    ax.axvline(median_val, color='green', linestyle='-', linewidth=2,
#              label=f'Median = {median_val:.2f}')
#    ax.axvspan(q25, q75, alpha=0.2, color='gray',
#              label='IQR')

# 7. Kernel Density Estimate overlay:
#    from scipy.stats import gaussian_kde
#    kde = gaussian_kde(data)
#    x_kde = np.linspace(data.min(), data.max(), 100)
#    # For density=True histogram
#    ax.hist(data, bins=30, density=True, alpha=0.5)
#    ax.plot(x_kde, kde(x_kde), 'r-', linewidth=2.5,
#           label='KDE')

# 8. Box plot alongside histogram:
#    from mpl_toolkits.axes_grid1 import make_axes_locatable
#    divider = make_axes_locatable(ax)
#    ax_box = divider.append_axes("top", size=1.2, pad=0.1, sharex=ax)
#    ax_box.boxplot(data, vert=False, widths=0.7)
#    ax_box.set_yticks([])

# 9. Fill between with errors:
#    ax.plot(x, y, 'b-', linewidth=2)
#    ax.fill_between(x, y - error, y + error, alpha=0.3, color='blue')

# 10. Error bars with different x/y errors for each point:
#     xerr = [[lower_x_errors], [upper_x_errors]]
#     yerr = [[lower_y_errors], [upper_y_errors]]
#     ax.errorbar(x, y, xerr=xerr, yerr=yerr, fmt='o')
