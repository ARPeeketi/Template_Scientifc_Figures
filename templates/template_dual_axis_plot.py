"""
TEMPLATE: Dual-Axis Line Plot (Two Y-Axes)
===========================================
This template shows how to create plots with two different y-axes sharing the same x-axis.
Suitable for: Comparing data with different scales or units
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

# Shared x-axis data
x = np.linspace(0, 10, 100)

# Left y-axis data (first dataset)
y1_line1 = x**2
y1_line2 = 0.5 * x**2
y1_line3 = 1.5 * x**2

# Right y-axis data (second dataset with different scale)
y2_data = 100 * np.exp(-0.3 * x)

# ============================================================================
# PLOT STYLING PARAMETERS
# ============================================================================

fs = 24.0           # Font size
r = 0.9             # Tick label font ratio
linewidth = 2.0     # Line width
marker_size = 6.0   # Marker size

# ============================================================================
# CREATE FIGURE AND FIRST AXIS
# ============================================================================

fig, ax1 = plt.subplots(figsize=(6.2, 6.0), dpi=50)

# ============================================================================
# PLOT DATA ON LEFT Y-AXIS (ax1)
# ============================================================================

# Plot multiple lines on the left y-axis
ax1.plot(x, y1_line1, 'r-', linewidth=linewidth, label=r'Data A')
ax1.plot(x, y1_line2, 'g-', linewidth=linewidth, label=r'Data B')
ax1.plot(x, y1_line3, 'c-', linewidth=linewidth, label=r'Data C')

# ============================================================================
# CONFIGURE LEFT Y-AXIS (ax1)
# ============================================================================

# Set axis limits
ax1.set_xlim(0.0, 10.0)
ax1.set_ylim(0, 150)

# Set tick positions
ax1.xaxis.set_ticks(np.arange(0, 10.1, 2.0))
ax1.yaxis.set_ticks(np.arange(0, 151, 30))

# Enable minor ticks
ax1.minorticks_on()

# Set labels (left y-axis is typically in black)
ax1.set_xlabel(r'$x$ variable (units)', color='k', fontsize=fs)
ax1.set_ylabel(r'Left $y$ variable (units)', color='k', fontsize=fs)

# Format tick labels
for tick in ax1.get_xticklabels():
    tick.set_fontsize(r * fs)
for tick in ax1.get_yticklabels():
    tick.set_fontsize(r * fs)

# Customize tick appearance
ax1.tick_params(which='major', direction='in', length=10, width=1.5, colors='k')
ax1.tick_params(which='minor', direction='in', length=5, width=1.5, colors='k')
ax1.tick_params(which='both', top=True, right=True)

# ============================================================================
# CREATE SECOND Y-AXIS (RIGHT SIDE)
# ============================================================================

# Create second y-axis that shares the same x-axis
ax2 = ax1.twinx()

# ============================================================================
# PLOT DATA ON RIGHT Y-AXIS (ax2)
# ============================================================================

# Color for right axis (typically blue to differentiate from left)
color = 'tab:blue'

# Plot data with markers
ax2.plot(x, y2_data, 'bs', markersize=marker_size, markevery=10, 
         linewidth=0, label=r'Experimental')

# Alternative: Plot with both line and markers
# ax2.plot(x, y2_data, 'bs-', markersize=marker_size, markevery=10, 
#          linewidth=1.5, label=r'Experimental')

# ============================================================================
# CONFIGURE RIGHT Y-AXIS (ax2)
# ============================================================================

# Set y-axis limits for right axis
ax2.set_ylim(0, 120)

# Set tick positions
ax2.yaxis.set_ticks(np.arange(0, 121, 20))

# Set label (note: color matches the data color for clarity)
ax2.set_ylabel(r'Right $y$ variable (different units)', color='b', fontsize=fs)

# Enable minor ticks
ax2.minorticks_on()

# Format tick labels
for tick in ax2.get_yticklabels():
    tick.set_fontsize(r * fs)

# Customize tick appearance (note: colors match the data)
ax2.tick_params(which='major', direction='in', length=10, width=1.5, colors='b')
ax2.tick_params(which='minor', direction='in', length=5, width=1.5, colors='b')
ax2.tick_params(which='both', top=True, right=True)

# ============================================================================
# ANNOTATIONS (Optional)
# ============================================================================

# Add text annotation on the right axis
ax2.text(7.0, 35, r'Exp. Data', color='b', fontsize=r*fs)

# Add arrow annotation
# ax2.annotate('', xy=(9.8, 10), xytext=(8.2, 10),
#              arrowprops=dict(arrowstyle='->, head_length=0.7, head_width=0.5',
#                            lw=1.5, color='blue'))

# ============================================================================
# ASPECT RATIO
# ============================================================================

ratio = 1.0
ax1.set_aspect(1.0/ax1.get_data_ratio() * ratio)

# ============================================================================
# SAVE AND DISPLAY
# ============================================================================

output_filename = 'dual_axis_plot.pdf'
plt.savefig(output_filename, bbox_inches='tight', dpi=300)
plt.show()

# ============================================================================
# ADDITIONAL TIPS FOR DUAL-AXIS PLOTS
# ============================================================================

# 1. Legend for dual-axis plots:
#    To combine legends from both axes:
#    lines1, labels1 = ax1.get_legend_handles_labels()
#    lines2, labels2 = ax2.get_legend_handles_labels()
#    ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left', fontsize=r*fs)

# 2. Color coordination:
#    - Keep left axis in black/neutral colors
#    - Use distinctive color (like blue) for right axis
#    - Match line/marker colors with axis label colors

# 3. Common mistakes to avoid:
#    - Don't use too many different scales (confusing)
#    - Ensure both datasets actually need different scales
#    - Label axes clearly with units

# 4. Alignment tips:
#    - Both y-axes should start and end at clean values
#    - Consider if zero should be included on both axes
#    - Use set_ylim() to control the ranges independently

# 5. For more than two y-axes:
#    ax3 = ax1.twinx()
#    ax3.spines['right'].set_position(('outward', 60))
#    # Then configure ax3 as above
