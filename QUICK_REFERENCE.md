# Quick Reference Guide

A fast guide to choosing the right template and finding common solutions.

## 📋 Table of Contents
- [Template Selection](#template-selection)
- [Common Tasks](#common-tasks)
- [Quick Syntax](#quick-syntax)
- [Color Reference](#color-reference)
- [Troubleshooting](#troubleshooting)

---

## Template Selection

### Decision Tree: Which Template Do I Need?

```
What type of data do you have?

├─ One variable vs another (X vs Y)
│  ├─ Points only → template_scatter_plot.py
│  ├─ Line only → template_line_plot.py
│  ├─ Both line and points → template_line_plot.py (add markers)
│  └─ With uncertainty band → template_filled_area.py
│
├─ Categories vs values
│  ├─ Simple comparison → template_bar_chart.py
│  ├─ Multiple groups → template_bar_chart.py (grouped bars)
│  └─ Stacked composition → template_bar_chart.py (stacked bars)
│
├─ Distribution or frequency
│  ├─ Single variable → template_histogram_errorbar.py
│  ├─ With error bars → template_histogram_errorbar.py
│  └─ Two variables (2D) → template_heatmap.py
│
├─ 2D scalar field (X, Y, Z)
│  ├─ Filled regions → template_contour_plot.py
│  ├─ Grid pattern → template_heatmap.py
│  └─ Specific level highlighted → template_contour_plot.py
│
├─ Multiple plots in one figure
│  ├─ Same scale → template_subplots.py
│  ├─ Different scales → template_dual_axis_plot.py
│  └─ Various layouts → template_subplots.py
│
└─ Special cases
   ├─ Data spanning many orders → template_log_plot.py
   └─ Annotation-heavy figure → template_filled_area.py
```

---

## Template At-A-Glance

| I want to... | Use this template | Key features |
|--------------|------------------|--------------|
| Plot simple line graph | `template_line_plot.py` | Single/multiple lines, clean styling |
| Show relationship between two variables | `template_scatter_plot.py` | Color-coded points, colorbars |
| Compare categories | `template_bar_chart.py` | Single/grouped/stacked bars |
| Show distribution | `template_histogram_errorbar.py` | Frequency plots, bins |
| Visualize 2D data | `template_heatmap.py` | Color-mapped grid |
| Show contours/levels | `template_contour_plot.py` | Filled contours, level lines |
| Plot with uncertainty | `template_filled_area.py` | Shaded regions, error bands |
| Compare different scales | `template_dual_axis_plot.py` | Two Y-axes |
| Create multi-panel figure | `template_subplots.py` | Grid layouts |
| Handle large range data | `template_log_plot.py` | Logarithmic scales |
| Plot with error bars | `template_histogram_errorbar.py` | Vertical/horizontal errors |

---

## Common Tasks

### Quick Modifications

#### Change a Line Color
```python
# Find the line:
ax.plot(x, y, 'r-', ...)

# Change 'r' to:
'b'  # blue        '#FF5733'  # hex color
'g'  # green       '#3498DB'  # custom blue
'k'  # black       'C0'       # default color cycle
```

#### Make Line Thicker/Thinner
```python
ax.plot(x, y, linewidth=2.0)   # Default
ax.plot(x, y, linewidth=3.5)   # Thicker
ax.plot(x, y, linewidth=1.0)   # Thinner
```

#### Add Markers to Line
```python
# Without markers:
ax.plot(x, y, 'r-', linewidth=2)

# With markers:
ax.plot(x, y, 'ro-', linewidth=2, markersize=6)
#            ^^^ add marker symbol

# Show markers every N points:
ax.plot(x, y, 'ro-', linewidth=2, markersize=6, markevery=5)
```

#### Change Axis Limits
```python
# Find these lines and modify:
ax.set_xlim(0, 10)      # Change to your x-range
ax.set_ylim(-1, 1)      # Change to your y-range
```

#### Change Axis Labels
```python
# Regular text:
ax.set_xlabel('Time (seconds)', fontsize=24)

# With math symbols:
ax.set_xlabel(r'$\alpha$ (degrees)', fontsize=24)

# With units:
ax.set_xlabel(r'Temperature (\SI{}{\celsius})', fontsize=24)
```

#### Move Legend
```python
ax.legend(loc='upper right')   # Top-right corner
ax.legend(loc='upper left')    # Top-left corner
ax.legend(loc='lower right')   # Bottom-right corner
ax.legend(loc='lower left')    # Bottom-left corner
ax.legend(loc='center')        # Center
ax.legend(loc='best')          # Auto-position
```

#### Save in Different Format
```python
# Find the savefig line and change extension:
plt.savefig('figure.pdf', ...)   # PDF (recommended)
plt.savefig('figure.png', ...)   # PNG image
plt.savefig('figure.svg', ...)   # SVG vector
plt.savefig('figure.eps', ...)   # EPS (some journals)
```

---

## Quick Syntax

### Plot Types One-Liner

```python
# Line plot
ax.plot(x, y, 'r-', linewidth=2, label='Data')

# Scatter plot
ax.scatter(x, y, s=50, c='blue', marker='o', alpha=0.7)

# Bar chart
ax.bar(categories, values, width=0.6, color='steelblue')

# Histogram
ax.hist(data, bins=30, color='green', alpha=0.7)

# Error bars
ax.errorbar(x, y, yerr=errors, fmt='o', capsize=5)

# Filled region
ax.fill_between(x, y_lower, y_upper, alpha=0.3, color='blue')

# Heatmap
ax.pcolormesh(X, Y, Z, cmap='viridis', shading='auto')

# Contour
ax.contour(X, Y, Z, levels=10, colors='k', linewidths=1.5)
```

### Style Codes

#### Color Codes
```python
'r' = red       'g' = green     'b' = blue      'c' = cyan
'm' = magenta   'y' = yellow    'k' = black     'w' = white
```

#### Line Styles
```python
'-'   = solid       '--'  = dashed      ':'   = dotted
'-.'  = dash-dot    ''    = no line
```

#### Marker Styles
```python
'o'  = circle       's'  = square       '^'  = triangle up
'v'  = triangle dn  'D'  = diamond      '*'  = star
'+'  = plus         'x'  = x-mark       '.'  = point
```

### Format String Combinations
```python
'ro'    # Red circles, no line
'b-'    # Blue solid line, no markers
'g--'   # Green dashed line
'k^-'   # Black triangles with solid line
'ms:'   # Magenta squares with dotted line
```

---

## Color Reference

### Named Colors
```python
# Basic colors
'red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink', 'brown'

# Extended colors
'darkred', 'lightblue', 'darkgreen', 'gold', 'coral', 'violet'
```

### Color Cycles (C0-C9)
```python
'C0'  # Blue (default first color)
'C1'  # Orange
'C2'  # Green
'C3'  # Red
'C4'  # Purple
# ... continues to C9
```

### Hex Colors
```python
# Custom precise colors
'#FF5733'  # Red-orange
'#3498DB'  # Bright blue
'#2ECC71'  # Green
'#F39C12'  # Orange
'#8E44AD'  # Purple
```

### Colormaps for Heatmaps/Contours

**Sequential (light to dark):**
```python
'viridis', 'plasma', 'inferno', 'magma', 'cividis'
'Blues', 'Greens', 'Reds', 'Oranges', 'Purples'
'YlOrRd', 'YlOrBr', 'YlGnBu'
```

**Diverging (two extremes with neutral center):**
```python
'coolwarm', 'RdBu', 'RdYlBu', 'RdYlGn', 'Spectral', 'seismic'
```

**Qualitative (distinct categories):**
```python
'tab10', 'tab20', 'Set1', 'Set2', 'Set3', 'Paired'
```

**Reverse any colormap:** Add `_r` suffix, e.g., `'viridis_r'`, `'RdBu_r'`

---

## Font Sizes

### Recommended Sizes

For **single-column** figure (3.5 inches wide):
```python
fs = 10              # Axis labels
r = 0.8              # Tick labels (0.8 * fs = 8pt)
linewidth = 1.5      # Line width
```

For **double-column** figure (7 inches wide):
```python
fs = 14              # Axis labels
r = 0.85             # Tick labels (0.85 * fs ≈ 12pt)
linewidth = 2.0      # Line width
```

For **presentations**:
```python
fs = 24              # Axis labels
r = 0.9              # Tick labels (0.9 * fs ≈ 22pt)
linewidth = 3.0      # Line width
```

### Applying Consistently
```python
ax.set_xlabel('Label', fontsize=fs)
ax.set_ylabel('Label', fontsize=fs)
ax.legend(fontsize=r*fs)
ax.tick_params(labelsize=r*fs)
```

---

## LaTeX Math Symbols

### Common Greek Letters
```python
r'$\alpha$'    # α       r'$\beta$'     # β
r'$\gamma$'    # γ       r'$\delta$'    # δ
r'$\epsilon$'  # ε       r'$\theta$'    # θ
r'$\lambda$'   # λ       r'$\mu$'       # μ
r'$\pi$'       # π       r'$\sigma$'    # σ
r'$\phi$'      # φ       r'$\omega$'    # ω

# Capital letters
r'$\Gamma$'    # Γ       r'$\Delta$'    # Δ
r'$\Theta$'    # Θ       r'$\Lambda$'   # Λ
r'$\Sigma$'    # Σ       r'$\Omega$'    # Ω
```

### Common Operations
```python
r'$x^2$'               # x²  (superscript)
r'$x_i$'               # xᵢ  (subscript)
r'$\frac{a}{b}$'       # a/b (fraction)
r'$\sqrt{x}$'          # √x  (square root)
r'$\bar{x}$'           # x̄   (overbar/mean)
r'$\dot{x}$'           # ẋ   (time derivative)
```

### Example Labels
```python
ax.set_xlabel(r'$\kappa$ ($\mathrm{nm}^{-1}$)')
ax.set_ylabel(r'$E$ (eV)')
ax.set_title(r'$\alpha = 0.5$, $\beta = 2.0$')
```

---

## Data Loading Cheat Sheet

### From CSV
```python
import numpy as np
data = np.genfromtxt('file.csv', delimiter=',', skip_header=1)
x = data[:, 0]  # First column
y = data[:, 1]  # Second column
```

### From Text File (Space-Separated)
```python
data = np.loadtxt('file.txt')
x = data[:, 0]
y = data[:, 1]
```

### Using Pandas (More Flexible)
```python
import pandas as pd
df = pd.read_csv('file.csv')
x = df['columnname_x'].values
y = df['columnname_y'].values
```

### From Excel
```python
import pandas as pd
df = pd.read_excel('file.xlsx', sheet_name='Sheet1')
x = df['Column1'].values
y = df['Column2'].values
```

### Create Arrays Manually
```python
# Direct definition
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])

# Linspace (N evenly spaced points)
x = np.linspace(0, 10, 100)  # 100 points from 0 to 10

# Arange (like range() but for floats)
x = np.arange(0, 10, 0.1)  # From 0 to 10, step 0.1
```

---

## Troubleshooting

### Issue: Plot doesn't appear
**Solution:** Add `plt.show()` at the end of your script

### Issue: "No module named 'matplotlib'"
**Solution:** Install matplotlib: `pip install matplotlib`

### Issue: LaTeX errors
**Solution:** Comment out these lines:
```python
# plt.rc('text', usetex=True)
# plt.rc('text.latex', preamble=preamble)
```

### Issue: Font warnings
**Solution:** The plot will still work, warnings can be ignored. Or install fonts:
```bash
# Linux:
sudo apt-get install msttcorefonts
```

### Issue: Figure too small/large
**Solution:** Adjust `figsize` parameter:
```python
fig, ax = plt.subplots(figsize=(width, height))  # in inches
```

### Issue: Text overlapping
**Solution:**
```python
plt.tight_layout()  # Before savefig
# or
plt.savefig('file.pdf', bbox_inches='tight')
```

### Issue: Low resolution output
**Solution:** Increase DPI:
```python
plt.savefig('file.png', dpi=300)  # 300 for publication
```

---

## Quick Workflow

### Standard Publication Figure Workflow

1. **Choose template** based on data type (see Decision Tree)
2. **Copy template** to new file with descriptive name
3. **Load your data** (replace sample data section)
4. **Run once** to see default output
5. **Adjust colors** and styles
6. **Fine-tune limits** and ticks
7. **Update labels** with proper units
8. **Position legend** appropriately
9. **Save at 300 DPI** as PDF
10. **Check output** - is text readable? Colors clear?

### 5-Minute Quick Plot

```python
import numpy as np
import matplotlib.pyplot as plt

# Your data here
x = np.loadtxt('data.txt')[:, 0]
y = np.loadtxt('data.txt')[:, 1]

# Quick plot
fig, ax = plt.subplots(figsize=(6, 5))
ax.plot(x, y, 'b-', linewidth=2)
ax.set_xlabel('X (units)')
ax.set_ylabel('Y (units)')
plt.tight_layout()
plt.savefig('quick_plot.pdf', dpi=300)
plt.show()
```

---

## Keyboard Shortcuts (Common)

When viewing plots interactively:
- **`s`** - Save figure
- **`q`** - Close window
- **Pan mode** - Click and drag to move
- **Zoom mode** - Draw rectangle to zoom
- **Home** - Reset view

---

## Useful One-Liners

```python
# Add grid
ax.grid(True, alpha=0.3)

# Add title
ax.set_title('My Figure Title', fontsize=16)

# Remove top and right spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Make plot square
ax.set_aspect('equal')

# Set background color
ax.set_facecolor('#F0F0F0')

# Add horizontal/vertical line
ax.axhline(y=0, color='k', linestyle='--')
ax.axvline(x=0, color='k', linestyle='--')

# Add text anywhere
ax.text(x_pos, y_pos, 'Text here', fontsize=14)

# Tight layout (prevents label cutoff)
plt.tight_layout()
```

---

## Need More Help?

- **Detailed examples**: See [TUTORIAL.md](TUTORIAL.md)
- **Installation issues**: Check [INSTALL.md](INSTALL.md)
- **Matplotlib docs**: [matplotlib.org/stable/gallery](https://matplotlib.org/stable/gallery/index.html)
- **Report bugs**: Open an issue on GitHub

---

**Keep this reference handy while working with the templates! 🚀**
