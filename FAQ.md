# Frequently Asked Questions (FAQ)

Quick answers to common questions about the Scientific Plotting Templates.

## Table of Contents
- [General Questions](#general-questions)
- [Installation Issues](#installation-issues)
- [LaTeX Questions](#latex-questions)
- [Template Usage](#template-usage)
- [Customization](#customization)
- [Output and Saving](#output-and-saving)
- [Troubleshooting](#troubleshooting)

---

## General Questions

### Q: What are these templates for?

**A:** These templates help you create publication-quality scientific figures quickly. Instead of remembering matplotlib syntax, you can start with a working template and modify it for your needs.

### Q: Do I need to know Python well to use these?

**A:** Basic Python knowledge is helpful, but not required. If you can:
- Open and edit a text file
- Run a Python script
- Replace sample data with your own

Then you can use these templates!

### Q: Can I use these for my thesis/paper/presentation?

**A:** Yes! The templates are released under the MIT License, which means you can use them freely for academic, commercial, or personal projects. Attribution is appreciated but not required.

### Q: Which template should I use for my data?

**A:** Check the [QUICK_REFERENCE.md](QUICK_REFERENCE.md) decision tree. It guides you based on your data type.

### Q: Are there example outputs I can see?

**A:** Yes, run any template to generate example output. Future versions will include an `examples/` directory with various use cases.

---

## Installation Issues

### Q: I get "ModuleNotFoundError: No module named 'matplotlib'"

**A:** Matplotlib is not installed. Install it with:
```bash
pip install matplotlib
```
Or install all dependencies:
```bash
pip install -r requirements.txt
```

### Q: pip install fails with permission error

**A:** Try one of these solutions:

**Option 1: Use --user flag**
```bash
pip install --user matplotlib
```

**Option 2: Use a virtual environment (recommended)**
```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
pip install -r requirements.txt
```

**Option 3: Use sudo (not recommended)**
```bash
sudo pip install matplotlib
```

### Q: Which Python version do I need?

**A:** Python 3.7 or higher. Check your version:
```bash
python --version
```

### Q: Can I use Python 2?

**A:** No, Python 2 reached end-of-life in 2020. Please upgrade to Python 3.

---

## LaTeX Questions

### Q: Do I need LaTeX to use these templates?

**A:** No! LaTeX is optional but recommended for professional typography. Without LaTeX:
1. Comment out these lines in any template:
```python
# plt.rc('text', usetex=True)
# plt.rc('text.latex', preamble=preamble)
```
2. The plots will use matplotlib's default fonts instead

### Q: How do I know if LaTeX is installed?

**A:** Run this in your terminal:
```bash
pdflatex --version
```
If you see version information, LaTeX is installed.

### Q: Where can I get LaTeX?

**A:** See [INSTALL.md](INSTALL.md) for detailed instructions. Quick links:
- **Windows**: [MiKTeX](https://miktex.org/)
- **macOS**: [MacTeX](https://www.tug.org/mactex/)
- **Linux**: `sudo apt-get install texlive`

### Q: I get "LaTeX Error: File `...sty' not found"

**A:** You're missing a LaTeX package. 

**On MiKTeX (Windows):**
- MiKTeX usually installs packages automatically
- If not, open MiKTeX Console → Packages → Install missing

**On Linux:**
```bash
sudo apt-get install texlive-latex-extra
```

**On macOS:**
```bash
sudo tlmgr update --all
sudo tlmgr install <package-name>
```

### Q: LaTeX makes my plots slow to generate

**A:** Yes, LaTeX rendering is slower. For quick prototyping, disable LaTeX. Re-enable it for final output:
```python
# Quick draft
plt.rc('text', usetex=False)

# Final version
plt.rc('text', usetex=True)
```

---

## Template Usage

### Q: How do I run a template?

**A:** 
```bash
python template_line_plot.py
```
A window will show the plot, and a PDF file will be saved in the same directory.

### Q: Where is my output file saved?

**A:** In the same directory where you ran the script. Look for:
```
line_plot.pdf
bar_chart.pdf
# etc.
```

### Q: Can I run templates in Jupyter Notebook?

**A:** Yes! Copy the template code into a notebook cell. You may want to:
1. Remove `plt.show()` to display inline
2. Add `%matplotlib inline` at the top

### Q: How do I load my own data?

**A:** Replace the data generation section. Examples:

**From CSV:**
```python
import numpy as np
data = np.genfromtxt('mydata.csv', delimiter=',', skip_header=1)
x = data[:, 0]
y = data[:, 1]
```

**From TXT:**
```python
data = np.loadtxt('mydata.txt')
x = data[:, 0]
y = data[:, 1]
```

**With Pandas:**
```python
import pandas as pd
df = pd.read_csv('mydata.csv')
x = df['x_column'].values
y = df['y_column'].values
```

### Q: Can I combine multiple templates?

**A:** Yes! For example, you might want a line plot with a bar chart inset. Study `template_subplots.py` for multi-panel layouts, then copy relevant sections from other templates.

---

## Customization

### Q: How do I change colors?

**A:** Find the plot line and change the color code:
```python
# Color letter codes
ax.plot(x, y, 'r-')  # red
ax.plot(x, y, 'b-')  # blue
ax.plot(x, y, 'g-')  # green
ax.plot(x, y, 'k-')  # black

# Hex codes for exact colors
ax.plot(x, y, color='#FF5733')

# Named colors
ax.plot(x, y, color='steelblue')
```

### Q: How do I make text bigger/smaller?

**A:** Modify the `fs` variable near the top:
```python
fs = 24.0  # Main font size
r = 0.9    # Tick labels are r*fs

# For specific elements:
ax.set_xlabel('X', fontsize=30)  # Larger
ax.legend(fontsize=18)           # Smaller
```

### Q: How do I change line thickness?

**A:** Modify the `linewidth` parameter:
```python
linewidth = 2.0   # Default
linewidth = 3.5   # Thicker
linewidth = 1.0   # Thinner

# In plot command:
ax.plot(x, y, linewidth=3.5)
```

### Q: How do I add markers to my line?

**A:**
```python
ax.plot(x, y, 'ro-')  # Red circles with line
#            ^^-- add marker symbol

# Show every Nth marker:
ax.plot(x, y, 'ro-', markevery=5)  # Every 5th point
```

### Q: How do I change figure size?

**A:** Modify the `figsize` parameter:
```python
fig, ax = plt.subplots(figsize=(6, 6))    # Square
fig, ax = plt.subplots(figsize=(10, 5))   # Wide
fig, ax = plt.subplots(figsize=(5, 8))    # Tall
```

### Q: How do I use different fonts?

**A:** Without LaTeX:
```python
matplotlib.rcParams['font.family'] = 'Arial'
# Or: 'Times New Roman', 'Helvetica', 'DejaVu Sans', etc.
```

With LaTeX, fonts are controlled by LaTeX packages in the preamble.

---

## Output and Saving

### Q: What's the best format for papers?

**A:** PDF (vector format). It's scalable and most journals accept it:
```python
plt.savefig('figure.pdf', bbox_inches='tight', dpi=300)
```

### Q: What's the best format for presentations?

**A:** PNG at 300 DPI for good quality:
```python
plt.savefig('figure.png', bbox_inches='tight', dpi=300)
```

### Q: My saved figure has too much white space

**A:** Use `bbox_inches='tight'`:
```python
plt.savefig('figure.pdf', bbox_inches='tight')
```

### Q: My saved figure is low resolution

**A:** Increase DPI:
```python
plt.savefig('figure.png', dpi=300)  # High resolution
plt.savefig('figure.png', dpi=150)  # Medium (faster)
```

### Q: How large should my figure be?

**A:** Common journal sizes:

**Single column:** ~3.5 inches wide
```python
fig, ax = plt.subplots(figsize=(3.5, 3))
```

**Double column:** ~7 inches wide
```python
fig, ax = plt.subplots(figsize=(7, 5))
```

**Check your journal's guidelines for exact requirements!**

### Q: Can I save multiple formats at once?

**A:** Yes!
```python
for fmt in ['pdf', 'png', 'svg']:
    plt.savefig(f'figure.{fmt}', bbox_inches='tight', dpi=300)
```

---

## Troubleshooting

### Q: The plot window doesn't appear

**A:** Add this at the end of your script:
```python
plt.show()
```

If still not working, try:
```python
import matplotlib
matplotlib.use('TkAgg')  # Or 'Qt5Agg'
import matplotlib.pyplot as plt
```

### Q: I get "RuntimeError: main thread is not in main loop"

**A:** This is a backend issue. Try:
```python
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt

# Then at the end, only save, don't show:
plt.savefig('figure.pdf')
# plt.show()  # Comment this out
```

### Q: My axis labels are cut off

**A:** Use `bbox_inches='tight'` or `plt.tight_layout()`:
```python
plt.tight_layout()  # Before savefig
plt.savefig('figure.pdf', bbox_inches='tight')
```

### Q: Colors look wrong in my saved figure

**A:** Ensure consistent DPI:
```python
fig, ax = plt.subplots(dpi=100)  # For display
plt.savefig('figure.pdf', dpi=300)  # For saving
```

### Q: My plot looks different after saving vs on screen

**A:** This can happen with DPI differences. Make sure:
```python
# Use same DPI for both
fig, ax = plt.subplots(figsize=(6, 5), dpi=100)
plt.savefig('figure.pdf', dpi=300)  # Higher DPI for printing
```

### Q: Scientific notation appears when I don't want it

**A:**
```python
from matplotlib.ticker import ScalarFormatter
formatter = ScalarFormatter(useOffset=False)
ax.yaxis.set_major_formatter(formatter)
```

### Q: I want to remove the top/right spines

**A:**
```python
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
```

### Q: How do I add a grid?

**A:**
```python
ax.grid(True)  # Basic grid
ax.grid(True, alpha=0.3, linestyle='--')  # Styled grid
```

---

## Data Questions

### Q: My data is in Excel, can I use it?

**A:** Yes! Install pandas and openpyxl:
```bash
pip install pandas openpyxl
```

Then:
```python
import pandas as pd
df = pd.read_excel('data.xlsx', sheet_name='Sheet1')
x = df['ColumnA'].values
y = df['ColumnB'].values
```

### Q: My data has missing values (NaN)

**A:** Remove or interpolate them:
```python
# Remove NaN
mask = ~np.isnan(x) & ~np.isnan(y)
x_clean = x[mask]
y_clean = y[mask]

# Or use pandas
df = df.dropna()
```

### Q: How do I plot only every Nth point?

**A:**
```python
ax.plot(x[::5], y[::5], 'o')  # Every 5th point
```

### Q: Can I plot multiple Y columns against one X?

**A:** Yes!
```python
data = np.loadtxt('data.txt')
x = data[:, 0]
y1 = data[:, 1]
y2 = data[:, 2]
y3 = data[:, 3]

ax.plot(x, y1, label='Series 1')
ax.plot(x, y2, label='Series 2')
ax.plot(x, y3, label='Series 3')
ax.legend()
```

---

## Performance Questions

### Q: My plots are slow to generate

**A:** Try these:
1. **Disable LaTeX** for drafts (major speedup)
2. **Reduce data points** - plot every Nth point
3. **Use simpler styles** - fewer effects and transparency
4. **Close figures** after saving: `plt.close()`

### Q: Python crashes with large datasets

**A:** 
1. **Downsample** your data
2. **Use `pcolormesh`** instead of `contourf` for large 2D data
3. **Increase memory** allocated to Python
4. **Process in batches**

---

## Advanced Questions

### Q: Can I use these templates in a script loop?

**A:** Yes! Example:
```python
for i, dataset in enumerate(datasets):
    fig, ax = plt.subplots()
    ax.plot(dataset['x'], dataset['y'])
    # ... styling ...
    plt.savefig(f'figure_{i}.pdf')
    plt.close()  # Important! Close to free memory
```

### Q: How do I make animations?

**A:** Matplotlib has animation capabilities, but it's not covered in these templates. See [matplotlib animation docs](https://matplotlib.org/stable/api/animation_api.html).

### Q: Can I make interactive plots?

**A:** For interactive plots, consider:
- Plotly
- Bokeh  
- Matplotlib with `%matplotlib notebook` in Jupyter

These templates focus on static publication figures.

### Q: How do I match my figures to my journal's style?

**A:** Check journal guidelines for:
- Figure dimensions
- Font sizes (typically 8-10 pt for labels)
- DPI requirements (usually 300 or 600)
- File format (PDF, EPS, or TIFF)
- Color vs grayscale

Adjust template parameters accordingly.

---

## Getting More Help

### Q: My question isn't answered here

**A:** Try these resources:

1. **Template comments** - Extensive tips in each template file
2. **TUTORIAL.md** - Step-by-step guide
3. **QUICK_REFERENCE.md** - Common tasks lookup
4. **Matplotlib docs** - [matplotlib.org](https://matplotlib.org/stable/contents.html)
5. **GitHub issues** - Search existing issues or open a new one
6. **Stack Overflow** - Tag your question with `matplotlib` and `python`

### Q: I found a bug, what should I do?

**A:** Please report it! Open an issue on GitHub with:
- Description of the problem
- Code to reproduce it
- Error message (if any)
- Your Python and matplotlib versions

### Q: I have a feature request

**A:** Great! Open an issue on GitHub describing:
- What feature you'd like
- Why it would be useful
- Example of how it would work

See [CONTRIBUTING.md](CONTRIBUTING.md) for more details.

---

## Tips and Tricks

### Tip 1: Start Simple
Begin with the simplest template that fits your needs. Add complexity only when necessary.

### Tip 2: Test on Sample Data First
Before using your real data, test the template with its sample data to understand how it works.

### Tip 3: Save Often
Save intermediate versions with different names:
```python
plt.savefig('figure_draft.pdf')
# Make changes
plt.savefig('figure_v2.pdf')
```

### Tip 4: Use Version Control
If making many changes, use git to track your modifications:
```bash
git init
git add my_plot.py
git commit -m "Initial version"
```

### Tip 5: Comment Your Changes
When modifying templates, add comments explaining your changes:
```python
# Modified 2025-01-15: Changed color scheme for colorblind accessibility
ax.plot(x, y, color='#E69F00')  # Orange instead of red
```

---

**Still have questions? Check out [TUTORIAL.md](TUTORIAL.md) or open an issue on GitHub!**
