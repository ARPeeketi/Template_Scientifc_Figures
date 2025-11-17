"""
MATPLOTLIB PLOTTING TEMPLATES - README
=======================================

This collection provides publication-quality plotting templates for scientific visualization.
All templates include comprehensive comments explaining options, parameters, and styling choices.

Author: Based on analysis of computational research notebooks
Date: November 2024

OVERVIEW
========

The templates are designed to be:
- Self-contained (no external dependencies beyond numpy and matplotlib)
- Well-commented for beginners
- Publication-ready with professional styling
- Easy to customize

Each template follows a consistent structure:
1. Font and text configuration
2. Data generation section (replace with your data)
3. Plot styling parameters
4. Main plotting code
5. Axis configuration
6. Tick formatting
7. Save and display
8. Additional tips and advanced options

TEMPLATE DESCRIPTIONS
=====================

1. template_line_plot.py
   -----------------------
   Purpose: Basic XY line plots with multiple curves
   Best for:
   - Time series data
   - Function plots
   - Comparing multiple datasets
   Features:
   - Multiple lines with different colors
   - Custom tick positioning
   - Legend customization
   - LaTeX text rendering
   - Aspect ratio control

2. template_dual_axis_plot.py
   ----------------------------
   Purpose: Plots with two different y-axes sharing same x-axis
   Best for:
   - Data with different scales
   - Comparing quantities with different units
   - Overlaying experimental and theoretical data
   Features:
   - Independent y-axis scaling
   - Color-coded axes
   - Markers and lines
   - Annotations with arrows

3. template_scatter_plot.py
   -------------------------
   Purpose: Scatter plots with colormap-based coloring
   Best for:
   - 3D data visualization (x, y, color)
   - Parameter studies
   - Correlation analysis
   Features:
   - Colormap customization
   - Colorbar with labels
   - Variable marker sizes and transparency
   - Categorical coloring options

4. template_heatmap.py
   --------------------
   Purpose: 2D heatmap visualization
   Best for:
   - Matrix data
   - Spatial data
   - Parameter sweeps
   - Correlation matrices
   Features:
   - pcolormesh and imshow methods
   - Custom colormaps
   - Contour line overlays
   - Logarithmic color scaling
   - Masked regions

5. template_contour_plot.py
   -------------------------
   Purpose: Filled contour plots with contour lines
   Best for:
   - Topographic data
   - Scalar fields
   - Level sets
   - Gradient visualization
   Features:
   - Filled contours with smooth gradients
   - Contour line overlays with labels
   - Custom level selection
   - Highlighted specific contours

6. template_bar_chart.py
   ----------------------
   Purpose: Vertical and horizontal bar charts
   Best for:
   - Categorical data
   - Comparisons between groups
   - Frequency distributions
   Features:
   - Single and grouped bars
   - Stacked bars
   - Error bars
   - Value labels on bars
   - Horizontal bar variant

7. template_subplots.py
   ---------------------
   Purpose: Multiple subplots in single figure
   Best for:
   - Comparing different datasets
   - Showing multiple aspects of data
   - Panel figures for publications
   Features:
   - Regular grid layouts
   - Custom grid with GridSpec
   - Shared axes
   - Subplot labels (a, b, c, ...)
   - Inset plots

8. template_log_plot.py
   ---------------------
   Purpose: Logarithmic scale plots
   Best for:
   - Data spanning multiple orders of magnitude
   - Power law relationships
   - Exponential decay/growth
   Features:
   - Log-log plots
   - Semi-log plots
   - Logarithmic heatmaps
   - Custom tick formatting
   - Grid for readability

9. template_histogram_errorbar.py
   -------------------------------
   Purpose: Histograms and error bar plots
   Best for:
   - Distribution analysis
   - Statistical data
   - Experimental measurements with uncertainties
   Features:
   - Various histogram types (bar, step, filled)
   - Overlapping histograms
   - 2D histograms
   - Error bars with caps
   - Asymmetric errors

10. template_filled_area.py
    -----------------------
    Purpose: Fill between curves and advanced annotations
    Best for:
    - Uncertainty visualization
    - Shaded regions
    - Highlighting areas of interest
    Features:
    - Fill between curves
    - Arrows and annotations
    - Geometric shapes (rectangles, circles, etc.)
    - Reference lines and spans
    - Mathematical notation examples

QUICK START GUIDE
=================

Step 1: Choose the Right Template
----------------------------------
- Line plots? → template_line_plot.py
- Two different scales? → template_dual_axis_plot.py
- 3D data (x, y, color)? → template_scatter_plot.py
- 2D field data? → template_heatmap.py or template_contour_plot.py
- Categories? → template_bar_chart.py
- Multiple plots? → template_subplots.py
- Wide data range? → template_log_plot.py
- Distributions? → template_histogram_errorbar.py
- Uncertainties? → template_filled_area.py

Step 2: Copy the Template
--------------------------
Copy the appropriate template file to your working directory

Step 3: Replace Data
--------------------
Find the "DATA GENERATION" section and replace with your actual data

Step 4: Customize
-----------------
Adjust parameters in "PLOT STYLING PARAMETERS" section:
- Font sizes
- Line widths
- Figure dimensions
- Colors

Step 5: Modify Labels
---------------------
Update axis labels, legend text, and title to match your data

Step 6: Run and Iterate
------------------------
Run the script, examine output, and refine as needed

COMMON STYLING PARAMETERS
==========================

Font Sizes
----------
- Main labels (xlabel, ylabel): 20-28 pt
- Tick labels: 16-24 pt (typically 0.8-0.9 × main font size)
- Legend: 16-22 pt
- Annotations: 14-20 pt

Line Properties
---------------
- Line width: 1.5-3.0 pt (thicker for presentations)
- Marker size: 6-12 pt for scatter plots
- Error bar width: 1.0-2.0 pt

Figure Dimensions
-----------------
- Single plot: 6-8 inches width
- Subplot panels: 10-15 inches width
- Aspect ratio: typically 1:1 or 3:2
- DPI: 50-100 for display, 300+ for publication

Colors
------
Scientific colormaps (perceptually uniform):
- Sequential: viridis, plasma, inferno, magma, cividis
- Diverging: coolwarm, RdBu, RdYlBu
- Qualitative: tab10, Set1, Set2

Avoid: jet, rainbow (not perceptually uniform)

LATEX RENDERING
===============

All templates support LaTeX for professional typography:

Requirements:
- LaTeX installation on your system
- Specific LaTeX packages (times, newtxmath, siunitx)

If LaTeX is not available:
1. Comment out the plt.rc('text', usetex=True) line
2. Remove or comment out preamble lines
3. Matplotlib will use its built-in math renderer

Common LaTeX syntax:
- Greek letters: $\alpha$, $\beta$, $\gamma$, etc.
- Subscripts: $x_i$, $y_{max}$
- Superscripts: $x^2$, $e^{-t}$
- Fractions: $\frac{a}{b}$
- Square roots: $\sqrt{x}$
- Integrals: $\int_0^x f(t) dt$
- Sums: $\sum_{i=1}^n x_i$

With siunitx package:
- Units: $\SI{300}{\kelvin}$
- Numbers: $\num{1.23e-4}$
- Ranges: $\SIrange{10}{20}{\meter}$

CUSTOMIZATION TIPS
==================

1. Color Schemes
   - Use colorblind-friendly palettes
   - Maintain sufficient contrast
   - Be consistent within a publication

2. Consistency
   - Use same font sizes across all figures
   - Maintain uniform line widths
   - Use consistent color coding

3. Clarity
   - Avoid overcrowding plots
   - Use appropriate tick spacing
   - Include units in all labels
   - Add legends when showing multiple datasets

4. Publication Requirements
   - Check journal's figure size requirements
   - Verify DPI requirements (usually 300+)
   - Confirm acceptable file formats (PDF, EPS, PNG)
   - Ensure figures are readable when printed in grayscale

TROUBLESHOOTING
===============

LaTeX Errors
------------
Problem: LaTeX rendering fails
Solution: Set usetex=False or install required LaTeX packages

Font Issues
-----------
Problem: Times New Roman not found
Solution: Use alternative fonts or system defaults
  matplotlib.rcParams['font.serif'] = ['DejaVu Serif']

Memory Issues
-------------
Problem: Large figures consume too much memory
Solution: 
- Reduce DPI for display (50-100)
- Reduce number of points in plots
- Use downsampling for very dense data

Slow Rendering
--------------
Problem: Figures take long time to render
Solution:
- Reduce number of contour levels
- Use 'gouraud' shading sparingly
- Consider rasterizing complex elements

ADVANCED FEATURES
=================

Most templates include commented-out examples of:
- Inset plots
- Multiple colormaps
- Custom tick formatting
- Annotations and arrows
- Statistical overlays
- 3D plotting basics
- Animation (time permitting)

See individual template files for detailed examples.

RESOURCES
=========

Official Documentation:
- Matplotlib: https://matplotlib.org/stable/
- NumPy: https://numpy.org/doc/

Useful Galleries:
- Matplotlib Gallery: https://matplotlib.org/stable/gallery/
- Python Graph Gallery: https://python-graph-gallery.com/

Color Advice:
- ColorBrewer: https://colorbrewer2.org/
- Colormaps reference: https://matplotlib.org/stable/tutorials/colors/colormaps.html

Scientific Plotting:
- Nature Figure Guidelines
- PLOS ONE Figure Requirements
- ACS Journal Guidelines

CONTRIBUTING
============

These templates are based on real research notebooks and represent
common visualization needs in computational research. Feel free to:
- Adapt for your specific needs
- Combine multiple templates
- Share improvements with colleagues

VERSION HISTORY
===============

v1.0 (November 2024)
- Initial release
- 10 comprehensive templates
- Based on analysis of 19 research notebooks
- Covers all major plot types used in scientific publications

ACKNOWLEDGMENTS
===============

Templates developed from patterns found in computational research
notebooks focusing on materials science and molecular dynamics simulations.

END OF README
=============
"""