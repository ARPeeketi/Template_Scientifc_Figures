# Tutorial: Creating Publication-Quality Figures

A comprehensive guide to using the Scientific Plotting Templates, from beginner basics to advanced customization.

## Table of Contents
- [Introduction](#introduction)
- [Part 1: Getting Started](#part-1-getting-started)
- [Part 2: Understanding a Template](#part-2-understanding-a-template)
- [Part 3: Your First Plot](#part-3-your-first-plot)
- [Part 4: Customization Basics](#part-4-customization-basics)
- [Part 5: Working with Your Data](#part-5-working-with-your-data)
- [Part 6: Advanced Techniques](#part-6-advanced-techniques)
- [Common Workflows](#common-workflows)
- [Best Practices](#best-practices)

## Introduction

### Who Is This Tutorial For?

- **Complete beginners** to Python plotting
- **Researchers** who need publication-quality figures quickly
- **Students** learning scientific visualization
- **Anyone** who wants professional-looking plots

### What You'll Learn

- How to create professional scientific figures
- Understanding template structure and components
- Customizing plots for your specific needs
- Best practices for publication-quality figures

### Prerequisites

- Basic Python knowledge (variables, functions, importing modules)
- Python and required packages installed (see [INSTALL.md](INSTALL.md))
- A text editor or IDE (VS Code, PyCharm, Jupyter, etc.)

---

## Part 1: Getting Started

### Your First Run

1. **Open a terminal/command prompt**
2. **Navigate to the templates directory:**
   ```bash
   cd path/to/scientific-plotting-templates
   ```
3. **Run a simple template:**
   ```bash
   python template_line_plot.py
   ```
4. **Check the output:**
   - A window should appear showing the plot
   - A file named `line_plot.pdf` is created in the same directory

**🎉 Congratulations!** You've created your first publication-quality figure.

### What Just Happened?

The template:
1. Loaded necessary libraries (numpy, matplotlib)
2. Generated sample data
3. Created a figure with professional styling
4. Saved it as a high-resolution PDF
5. Displayed it on screen

---

## Part 2: Understanding a Template

Let's dissect `template_line_plot.py` to understand its structure.

### Template Structure Overview

```python
# ============================================================================
# SECTION 1: FONT AND TEXT CONFIGURATION
# ============================================================================
plt.rc('text', usetex=True)  # Enable LaTeX rendering
matplotlib.rcParams['font.family'] = "serif"  # Set font family
```

**What it does:** Configures fonts and text rendering for professional typography.

**When to modify:** If you don't have LaTeX installed or want different fonts.

---

```python
# ============================================================================
# SECTION 2: DATA GENERATION
# ============================================================================
x = np.linspace(0, 10, 100)
y = np.sin(x)
```

**What it does:** Creates or loads the data you want to plot.

**When to modify:** **Always!** Replace this with your actual data.

---

```python
# ============================================================================
# SECTION 3: PLOT STYLING PARAMETERS
# ============================================================================
fs = 24.0          # Font size
r = 0.9            # Tick label ratio
linewidth = 2.0    # Line width
```

**What it does:** Defines global styling parameters for consistency.

**When to modify:** To adjust the overall appearance of your plot.

---

```python
# ============================================================================
# SECTION 4: CREATE FIGURE AND AXES
# ============================================================================
fig, ax = plt.subplots(figsize=(6.2, 6.0), dpi=50)
```

**What it does:** Creates the figure canvas and axes object.

**Key parameters:**
- `figsize`: Figure size in inches (width, height)
- `dpi`: Resolution (50 for screen, 300 for publication)

---

```python
# ============================================================================
# SECTION 5: PLOT DATA
# ============================================================================
ax.plot(x, y, 'r-', linewidth=linewidth, label='Data')
```

**What it does:** Actually draws your data on the axes.

**Format string breakdown:**
- `'r'` = red color
- `'-'` = solid line style
- Together: `'r-'` = red solid line

---

```python
# ============================================================================
# SECTION 6: AXIS CONFIGURATION
# ============================================================================
ax.set_xlim(0, 10)
ax.set_ylim(-1, 1)
ax.set_xlabel(r'$x$ variable (units)', fontsize=fs)
ax.set_ylabel(r'$y$ variable (units)', fontsize=fs)
```

**What it does:** Sets axis ranges and labels.

**LaTeX in labels:** The `r'$...$'` syntax enables mathematical notation.

---

```python
# ============================================================================
# SECTION 7: SAVE AND DISPLAY
# ============================================================================
plt.savefig('line_plot.pdf', bbox_inches='tight', dpi=300)
plt.show()
```

**What it does:** Saves the figure to a file and displays it.

**Key parameters:**
- `bbox_inches='tight'`: Removes excess whitespace
- `dpi=300`: High resolution for publication

---

## Part 3: Your First Plot

Let's create a simple plot from scratch using a template.

### Exercise 1: Plot Your Own Function

**Goal:** Plot the function y = x² from 0 to 5

**Step 1:** Open `template_line_plot.py` and save it as `my_first_plot.py`

**Step 2:** Find the data generation section (around line 30):

```python
# ORIGINAL CODE:
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
```

**Replace with:**

```python
# MY DATA:
x = np.linspace(0, 5, 100)
y = x**2  # x squared
```

**Step 3:** Find the plotting section (around line 50):

```python
# ORIGINAL CODE:
ax.plot(x, y1, 'r-', linewidth=linewidth, label=r'sin($x$)')
# Remove or comment out the other lines
```

**Replace with:**

```python
# MY PLOT:
ax.plot(x, y, 'b-', linewidth=linewidth, label=r'$y = x^2$')
```

**Step 4:** Update the axis labels (around line 70):

```python
ax.set_xlabel(r'$x$', fontsize=fs)
ax.set_ylabel(r'$y = x^2$', fontsize=fs)
```

**Step 5:** Update the axis limits:

```python
ax.set_xlim(0, 5)
ax.set_ylim(0, 25)
```

**Step 6:** Change the output filename (near the end):

```python
plt.savefig('my_quadratic.pdf', bbox_inches='tight', dpi=300)
```

**Step 7:** Run your script:

```bash
python my_first_plot.py
```

**🎉 Success!** You've created a customized plot.

---

## Part 4: Customization Basics

### Colors

**Common color codes:**
```python
'r' - red       'b' - blue      'g' - green
'k' - black     'c' - cyan      'm' - magenta
'y' - yellow    'w' - white

# Hex codes for precise colors:
'#FF5733'  # Custom orange-red
'#3498DB'  # Custom blue
```

**Example:**
```python
ax.plot(x, y, '#2E86AB', linewidth=2.5)  # Custom blue
```

### Line Styles

```python
'-'   # Solid line
'--'  # Dashed line
'-.'  # Dash-dot line
':'   # Dotted line
''    # No line (markers only)
```

**Example:**
```python
ax.plot(x, y, 'r--', linewidth=2)  # Red dashed line
```

### Markers

```python
'o'  # Circle          's'  # Square
'^'  # Triangle up     'v'  # Triangle down
'D'  # Diamond         '*'  # Star
'+'  # Plus sign       'x'  # X mark
```

**Example:**
```python
ax.plot(x, y, 'bo-', markersize=8, markevery=5)
# Blue circles every 5 points with connecting line
```

### Combining Styles

Format: `[marker][color][line]`

```python
'ro-'   # Red circles with solid line
'bs--'  # Blue squares with dashed line
'g^:'   # Green triangles with dotted line
'ko'    # Black circles, no line
```

### Font Sizes

```python
# Method 1: Using the template's fs variable
ax.set_xlabel('Label', fontsize=fs)         # Main labels
ax.set_title('Title', fontsize=1.2*fs)      # Larger title
ax.legend(fontsize=0.8*fs)                  # Smaller legend

# Method 2: Direct specification
ax.set_xlabel('Label', fontsize=24)
ax.tick_params(labelsize=20)
```

### Figure Size

```python
# Small figure (3x3 inches)
fig, ax = plt.subplots(figsize=(3, 3))

# Standard figure (6x6 inches)
fig, ax = plt.subplots(figsize=(6, 6))

# Wide figure (10x5 inches) for multiple plots
fig, ax = plt.subplots(figsize=(10, 5))

# Publication column width (typical: 3.5 inches)
fig, ax = plt.subplots(figsize=(3.5, 3))
```

---

## Part 5: Working with Your Data

### Loading Data from Files

#### From CSV File

```python
import numpy as np

# Simple CSV (comma-separated)
data = np.genfromtxt('mydata.csv', delimiter=',', skip_header=1)
x = data[:, 0]  # First column
y = data[:, 1]  # Second column

# Using pandas (more flexible)
import pandas as pd
df = pd.read_csv('mydata.csv')
x = df['column1'].values
y = df['column2'].values
```

#### From Text File (Space-Separated)

```python
data = np.loadtxt('mydata.txt')
x = data[:, 0]
y = data[:, 1]
```

#### From Excel File

```python
import pandas as pd
df = pd.read_excel('mydata.xlsx', sheet_name='Sheet1')
x = df['column1'].values
y = df['column2'].values
```

### Creating Data Arrays Manually

```python
# Method 1: Direct definition
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])

# Method 2: Using linspace
x = np.linspace(0, 10, 100)  # 100 points from 0 to 10

# Method 3: Using arange
x = np.arange(0, 10, 0.1)  # From 0 to 10 with step 0.1
```

### Multiple Data Series

```python
# Load multiple columns
data = np.genfromtxt('data.csv', delimiter=',')
x = data[:, 0]
y1 = data[:, 1]
y2 = data[:, 2]
y3 = data[:, 3]

# Plot them all
ax.plot(x, y1, 'r-', label='Series 1')
ax.plot(x, y2, 'b-', label='Series 2')
ax.plot(x, y3, 'g-', label='Series 3')
ax.legend()
```

---

## Part 6: Advanced Techniques

### Adding Error Bars

```python
# Your data with uncertainties
x = np.array([1, 2, 3, 4, 5])
y = np.array([2.0, 3.5, 5.1, 7.2, 9.8])
y_err = np.array([0.2, 0.3, 0.4, 0.3, 0.5])

# Plot with error bars
ax.errorbar(x, y, yerr=y_err, fmt='o', 
           capsize=5, capthick=2, 
           label='Measured data')
```

### Filled Regions (Uncertainty Bands)

```python
# Mean and standard deviation
y_mean = np.sin(x)
y_std = 0.2

# Plot mean line
ax.plot(x, y_mean, 'b-', linewidth=2, label='Mean')

# Add uncertainty band
ax.fill_between(x, y_mean - y_std, y_mean + y_std,
               alpha=0.3, color='blue', label='±1σ')
```

### Annotations and Arrows

```python
# Add text at a specific location
ax.text(5, 1.2, 'Peak region', fontsize=20)

# Add arrow pointing to a feature
ax.annotate('Maximum', 
           xy=(3.14, 1.0),      # Point to annotate
           xytext=(5, 1.5),     # Text location
           arrowprops=dict(arrowstyle='->', lw=2),
           fontsize=20)
```

### Logarithmic Scales

```python
# Log scale on y-axis
ax.set_yscale('log')

# Log scale on both axes
ax.set_xscale('log')
ax.set_yscale('log')
```

### Subplots (Multiple Panels)

```python
# Create 2 rows, 2 columns of subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Access individual subplots
axes[0, 0].plot(x, y1)  # Top-left
axes[0, 1].plot(x, y2)  # Top-right
axes[1, 0].plot(x, y3)  # Bottom-left
axes[1, 1].plot(x, y4)  # Bottom-right

# Add labels to each
for ax in axes.flat:
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
```

---

## Common Workflows

### Workflow 1: Quick Data Exploration

**Goal:** Quickly visualize a dataset

```python
import numpy as np
import matplotlib.pyplot as plt

# Load your data
data = np.loadtxt('mydata.txt')
x = data[:, 0]
y = data[:, 1]

# Quick plot
plt.figure(figsize=(8, 6))
plt.plot(x, y, 'o-')
plt.xlabel('X variable')
plt.ylabel('Y variable')
plt.grid(True)
plt.show()
```

### Workflow 2: Publication Figure

**Goal:** Create a polished figure for a paper

```python
# Start from template_line_plot.py
# 1. Load your data (replace sample data)
# 2. Adjust styling parameters
# 3. Fine-tune axis limits
# 4. Add proper labels with units
# 5. Adjust legend position
# 6. Save as PDF at 300 DPI
```

### Workflow 3: Comparing Multiple Datasets

**Goal:** Plot several datasets on one figure

```python
# Use template_line_plot.py
# In the plotting section:

datasets = [
    (x1, y1, 'r-', 'Experiment 1'),
    (x2, y2, 'b-', 'Experiment 2'),
    (x3, y3, 'g-', 'Experiment 3'),
]

for x, y, style, label in datasets:
    ax.plot(x, y, style, linewidth=2, label=label)

ax.legend(loc='best')
```

### Workflow 4: Parameter Study

**Goal:** Show how a function changes with parameters

```python
x = np.linspace(0, 10, 100)

# Different parameter values
params = [0.5, 1.0, 1.5, 2.0]
colors = ['r', 'b', 'g', 'm']

for param, color in zip(params, colors):
    y = np.exp(-param * x)
    ax.plot(x, y, color=color, linewidth=2,
           label=f'λ = {param}')

ax.legend()
ax.set_xlabel('Time (s)')
ax.set_ylabel('Amplitude')
```

---

## Best Practices

### For Publication-Quality Figures

1. **Use vector graphics (PDF)** instead of raster (PNG) when possible
2. **Set DPI to 300** for final output: `dpi=300`
3. **Use consistent fonts** across all figures in your document
4. **Label everything**: axes, units, legend entries
5. **Use colorblind-friendly colors** when possible
6. **Keep figures simple**: avoid clutter and unnecessary elements

### Font Size Guidelines

For a standard single-column figure (3.5 inches wide):
- **Axis labels**: 10-12 pt
- **Tick labels**: 8-10 pt
- **Legend**: 8-10 pt
- **Title** (if used): 12-14 pt

For double-column figures (7 inches wide):
- **Axis labels**: 12-14 pt
- **Tick labels**: 10-12 pt
- **Legend**: 10-12 pt

### Color Selection

**Good color combinations:**
```python
# Qualitative (different categories)
colors = ['#E41A1C', '#377EB8', '#4DAF4A', '#984EA3']  # From ColorBrewer

# Sequential (ordered data)
colors = ['#FEE5D9', '#FCAE91', '#FB6A4A', '#CB181D']  # Light to dark red

# Diverging (data with meaningful center)
colors = ['#2166AC', '#92C5DE', '#F4A582', '#B2182B']  # Blue to red
```

### Common Mistakes to Avoid

❌ **Don't:**
- Use default colors without thought
- Make text too small to read
- Forget axis labels or units
- Use 3D plots when 2D would suffice
- Over-complicate with unnecessary features

✅ **Do:**
- Choose colors intentionally
- Make text readable (even when reduced in size)
- Always label axes with units
- Use the simplest plot type that conveys your message
- Keep it clean and professional

### File Formats

**For papers/journals:**
- **Primary choice**: PDF (vector, scalable)
- **Alternative**: EPS (vector, some journals prefer this)

**For presentations:**
- PNG at 300 DPI (good quality, manageable size)
- PDF works too

**For web:**
- PNG at 150 DPI (good balance of quality and size)
- SVG (vector, interactive possibilities)

### Testing Your Figure

Before submitting:
1. **Print it** at actual size to check readability
2. **View it in grayscale** to ensure clarity without color
3. **Reduce it to publication size** and check if text is still readable
4. **Show it to a colleague** for feedback

---

## Practice Exercises

### Exercise 1: Temperature Data

Plot daily temperature data showing mean, max, and min temperatures.

<details>
<summary>Click to see solution</summary>

```python
import numpy as np
import matplotlib.pyplot as plt

# Sample data (replace with your actual data)
days = np.arange(1, 31)
temp_mean = 20 + 5 * np.sin(days / 5)
temp_max = temp_mean + 3
temp_min = temp_mean - 3

fig, ax = plt.subplots(figsize=(8, 5))

ax.plot(days, temp_mean, 'r-', linewidth=2, label='Mean')
ax.fill_between(days, temp_min, temp_max, alpha=0.3, color='red')

ax.set_xlabel('Day of Month', fontsize=14)
ax.set_ylabel('Temperature (°C)', fontsize=14)
ax.legend(loc='upper right', fontsize=12)
ax.grid(True, alpha=0.3)

plt.savefig('temperature.pdf', dpi=300, bbox_inches='tight')
plt.show()
```
</details>

### Exercise 2: Comparison Plot

Create a figure comparing theoretical and experimental data.

<details>
<summary>Click to see solution</summary>

```python
x = np.linspace(0, 10, 100)
y_theory = x**2
y_exp = x**2 + np.random.normal(0, 2, 100)

fig, ax = plt.subplots(figsize=(6, 6))

ax.plot(x, y_theory, 'b-', linewidth=2.5, label='Theory')
ax.scatter(x[::5], y_exp[::5], s=50, c='red', 
          marker='o', label='Experiment', alpha=0.7)

ax.set_xlabel(r'$x$', fontsize=18)
ax.set_ylabel(r'$y$', fontsize=18)
ax.legend(fontsize=14)

plt.savefig('comparison.pdf', dpi=300, bbox_inches='tight')
plt.show()
```
</details>

---

## Getting Help

**If you're stuck:**

1. Check the template comments - they contain detailed explanations
2. Refer to [QUICK_REFERENCE.md](QUICK_REFERENCE.md) for common tasks
3. Look at [Matplotlib documentation](https://matplotlib.org/stable/gallery/index.html)
4. Search for your error message online
5. Open an issue on GitHub with your problem

**Remember:** Everyone starts as a beginner. With practice, creating publication-quality figures will become second nature!

---

**Happy plotting! 📊✨**
