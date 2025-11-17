"""
TEMPLATE: Bar Chart
===================
This template shows how to create publication-quality bar charts.
Suitable for: Categorical data, comparisons, grouped data
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
# DATA PREPARATION (Replace with your actual data)
# ============================================================================

# Category labels
categories = ['A', 'B', 'C', 'D', 'E']
n_categories = len(categories)

# Single dataset
values_single = [25, 32, 28, 41, 35]
errors_single = [3, 4, 2, 5, 3]  # Error bars (optional)

# Multiple datasets for grouped bars
values_group1 = [25, 32, 28, 41, 35]
values_group2 = [30, 28, 35, 38, 40]
values_group3 = [22, 35, 30, 43, 32]

errors_group1 = [3, 4, 2, 5, 3]
errors_group2 = [2, 3, 4, 3, 4]
errors_group3 = [4, 2, 3, 4, 2]

# ============================================================================
# PLOT STYLING PARAMETERS
# ============================================================================

fs = 24.0           # Font size
r = 0.9             # Tick label font ratio
bar_width = 0.6     # Width of bars (0.4-0.8 typical)

# ============================================================================
# SIMPLE BAR CHART (Single Dataset)
# ============================================================================

fig, ax = plt.subplots(figsize=(7.0, 6.0), dpi=50)

# X positions for bars
x_pos = np.arange(n_categories)

# Create bars
# color options: single color or list of colors for each bar
bars = ax.bar(x_pos, values_single, width=bar_width, 
              color='steelblue', edgecolor='black', linewidth=1.5,
              alpha=0.8)

# Add error bars (optional)
ax.errorbar(x_pos, values_single, yerr=errors_single, 
           fmt='none', ecolor='black', capsize=5, capthick=1.5,
           linewidth=1.5)

# Alternative: Different color for each bar
# colors = ['red', 'green', 'blue', 'orange', 'purple']
# bars = ax.bar(x_pos, values_single, width=bar_width, color=colors,
#              edgecolor='black', linewidth=1.5)

# ============================================================================
# GROUPED BAR CHART (Multiple Datasets) - Comment out simple chart above
# ============================================================================

# fig, ax = plt.subplots(figsize=(8.0, 6.0), dpi=50)
# 
# # Calculate positions for grouped bars
# n_groups = 3
# bar_width = 0.25
# 
# x_pos = np.arange(n_categories)
# offset = bar_width
# 
# # Create bars for each group
# bars1 = ax.bar(x_pos - offset, values_group1, width=bar_width,
#               label=r'Group 1', color='steelblue', edgecolor='black',
#               linewidth=1.2)
# bars2 = ax.bar(x_pos, values_group2, width=bar_width,
#               label=r'Group 2', color='coral', edgecolor='black',
#               linewidth=1.2)
# bars3 = ax.bar(x_pos + offset, values_group3, width=bar_width,
#               label=r'Group 3', color='lightgreen', edgecolor='black',
#               linewidth=1.2)
# 
# # Add error bars for each group
# ax.errorbar(x_pos - offset, values_group1, yerr=errors_group1,
#            fmt='none', ecolor='black', capsize=4, linewidth=1.2)
# ax.errorbar(x_pos, values_group2, yerr=errors_group2,
#            fmt='none', ecolor='black', capsize=4, linewidth=1.2)
# ax.errorbar(x_pos + offset, values_group3, yerr=errors_group3,
#            fmt='none', ecolor='black', capsize=4, linewidth=1.2)

# ============================================================================
# STACKED BAR CHART - Alternative
# ============================================================================

# fig, ax = plt.subplots(figsize=(7.0, 6.0), dpi=50)
# 
# x_pos = np.arange(n_categories)
# 
# bars1 = ax.bar(x_pos, values_group1, width=bar_width,
#               label=r'Group 1', color='steelblue', edgecolor='black')
# bars2 = ax.bar(x_pos, values_group2, width=bar_width,
#               bottom=values_group1, label=r'Group 2', 
#               color='coral', edgecolor='black')
# bars3 = ax.bar(x_pos, values_group3, width=bar_width,
#               bottom=np.array(values_group1) + np.array(values_group2),
#               label=r'Group 3', color='lightgreen', edgecolor='black')

# ============================================================================
# HORIZONTAL BAR CHART - Alternative
# ============================================================================

# fig, ax = plt.subplots(figsize=(6.0, 7.0), dpi=50)
# 
# y_pos = np.arange(n_categories)
# 
# bars = ax.barh(y_pos, values_single, height=bar_width,
#               color='steelblue', edgecolor='black', linewidth=1.5)
# 
# ax.set_yticks(y_pos)
# ax.set_yticklabels(categories)
# ax.set_xlabel(r'Value (units)', fontsize=fs)
# ax.set_ylabel(r'Category', fontsize=fs)

# ============================================================================
# AXIS CONFIGURATION
# ============================================================================

# Set x-axis
ax.set_xticks(x_pos)
ax.set_xticklabels(categories)
ax.set_xlabel(r'Category', color='k', fontsize=fs)

# Set y-axis
ax.set_ylabel(r'Value (units)', color='k', fontsize=fs)
ax.set_ylim(0, 50)  # Start from 0 for bar charts
ax.yaxis.set_ticks(np.arange(0, 51, 10))

# Enable minor ticks
ax.minorticks_on()

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

# For horizontal bars, adjust:
# ax.tick_params(axis='x', which='both', top=True, bottom=True)
# ax.tick_params(axis='y', which='both', left=True, right=True)

# ============================================================================
# VALUE LABELS ON BARS (Optional)
# ============================================================================

# Add value labels on top of bars
# for i, (bar, value) in enumerate(zip(bars, values_single)):
#     height = bar.get_height()
#     ax.text(bar.get_x() + bar.get_width()/2., height + 1,
#            f'{value}', ha='center', va='bottom', fontsize=0.7*fs)

# For percentage labels:
# total = sum(values_single)
# for i, (bar, value) in enumerate(zip(bars, values_single)):
#     height = bar.get_height()
#     percentage = 100 * value / total
#     ax.text(bar.get_x() + bar.get_width()/2., height/2,
#            f'{percentage:.1f}\%', ha='center', va='center', 
#            fontsize=0.7*fs, color='white', fontweight='bold')

# ============================================================================
# REFERENCE LINES (Optional)
# ============================================================================

# Add horizontal reference line (e.g., threshold or target)
# ax.axhline(y=30, color='red', linestyle='--', linewidth=2, 
#           label='Target', alpha=0.7)

# ============================================================================
# LEGEND (For grouped bars)
# ============================================================================

# ax.legend(loc='upper right', fontsize=r*fs, frameon=True, 
#          shadow=False, ncol=1)

# For legend outside:
# ax.legend(loc='upper left', bbox_to_anchor=(1.02, 1.0), 
#          fontsize=r*fs, frameon=True)

# ============================================================================
# GRID (Optional)
# ============================================================================

# Add horizontal grid lines for readability
# ax.grid(axis='y', linestyle='--', alpha=0.3, linewidth=1)
# ax.set_axisbelow(True)  # Place grid below bars

# ============================================================================
# SAVE AND DISPLAY
# ============================================================================

output_filename = 'bar_chart.pdf'
plt.savefig(output_filename, bbox_inches='tight', dpi=300)
plt.show()

# ============================================================================
# ADDITIONAL TIPS FOR BAR CHARTS
# ============================================================================

# 1. Color gradients in bars:
#    colors = plt.cm.viridis(np.linspace(0.3, 0.9, n_categories))
#    bars = ax.bar(x_pos, values_single, color=colors, edgecolor='black')

# 2. Hatching patterns:
#    patterns = ['/', '\\', '|', '-', '+', 'x', 'o', 'O', '.', '*']
#    for bar, pattern in zip(bars, patterns):
#        bar.set_hatch(pattern)

# 3. Diverging bars (positive and negative):
#    values = [10, -5, 15, -8, 12]
#    colors = ['green' if v > 0 else 'red' for v in values]
#    bars = ax.bar(x_pos, values, color=colors, edgecolor='black')
#    ax.axhline(y=0, color='black', linewidth=2)

# 4. Log scale for large value ranges:
#    ax.set_yscale('log')

# 5. Custom bar colors based on value:
#    colors = ['red' if v < 30 else 'green' for v in values_single]
#    bars = ax.bar(x_pos, values_single, color=colors, edgecolor='black')

# 6. Annotate specific bars:
#    # Highlight maximum value
#    max_idx = np.argmax(values_single)
#    bars[max_idx].set_color('gold')
#    bars[max_idx].set_edgecolor('darkgoldenrod')
#    bars[max_idx].set_linewidth(3)

# 7. Break axis for outliers:
#    # Use brokenaxes package for discontinuous axes
#    # from brokenaxes import brokenaxes
#    # bax = brokenaxes(ylims=((0, 40), (90, 110)))
#    # bax.bar(x_pos, values_with_outlier, width=bar_width)

# 8. Percentage stacked bars:
#    # Normalize to percentages
#    data = np.array([values_group1, values_group2, values_group3])
#    data_percent = data / data.sum(axis=0) * 100
#    # Then create stacked bars with data_percent
