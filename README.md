# Scientific Plotting Templates for Python

A comprehensive collection of production-ready matplotlib templates for creating publication-quality scientific figures. Designed for researchers, students, and anyone who needs professional visualizations with minimal setup.

[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Matplotlib](https://img.shields.io/badge/matplotlib-3.0+-orange.svg)](https://matplotlib.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 🎯 Features

- **11 Complete Templates** covering all common scientific plot types
- **Publication-Ready** with LaTeX support for professional typography
- **Extensively Commented** code with clear explanations for every section
- **Beginner-Friendly** with step-by-step instructions and customization tips
- **Professional Styling** following best practices for scientific visualization
- **Copy-Paste Ready** - just replace the sample data with your own

## 📊 Available Templates

| Template | Description | Use Case |
|----------|-------------|----------|
| `simple_xy_plots.py` | Basic X-Y line plots | Time series, function plots, comparisons |
| `template_line_plot.py` | Advanced line plots | Multiple datasets, styled legends |
| `template_scatter_plot.py` | Scatter plots with colormaps | 3D data visualization, correlations |
| `template_bar_chart.py` | Bar charts (single/grouped/stacked) | Categorical data, comparisons |
| `template_histogram_errorbar.py` | Histograms and error bars | Distributions, statistical data |
| `template_contour_plot.py` | Filled contour plots | Scalar fields, topographic data |
| `template_heatmap.py` | 2D heatmaps | Matrix data, spatial distributions |
| `template_dual_axis_plot.py` | Two Y-axes plots | Different scales/units |
| `template_filled_area.py` | Filled regions and annotations | Uncertainty bands, highlighted regions |
| `template_subplots.py` | Multiple subplot layouts | Complex multi-panel figures |
| `template_log_plot.py` | Logarithmic scales | Multiple orders of magnitude |

## 🚀 Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/ARPeeketi/Template_Scientifc_Figures.git
cd Template_Scientifc_Figures
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run a template
```bash
python template_line_plot.py
```

### 4. Customize for your data
Open any template, replace the sample data with yours, and adjust labels/colors as needed.

## 📚 Documentation

- **[Installation Guide](INSTALL.md)** - Detailed setup instructions including LaTeX configuration
- **[Tutorial](TUTORIAL.md)** - Comprehensive guide for beginners
- **[Quick Reference](QUICK_REFERENCE.md)** - Fast template selection guide
- **[Examples Gallery](templates/)** - Sample outputs from each template and the corresponding python file

## 💡 Example Usage

```python
import matplotlib.pyplot as plt
import numpy as np

# Load template settings
from template_line_plot import *

# Your data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create figure
fig, ax = plt.subplots(figsize=(6.2, 6.0))
ax.plot(x, y, 'r-', linewidth=2.0, label='sin(x)')

# Apply template styling
ax.set_xlabel(r'$x$ (units)', fontsize=24)
ax.set_ylabel(r'$y$ (units)', fontsize=24)
ax.legend(loc='upper right', fontsize=20)
ax.tick_params(which='major', direction='in', length=10, width=1.5)

plt.savefig('my_plot.pdf', bbox_inches='tight', dpi=300)
plt.show()
```

## 🎨 Features Highlights

### Publication-Quality Typography
- LaTeX rendering support with Times Roman font
- Professional mathematical notation
- Customizable font sizes and styles

### Flexible Customization
- Comprehensive commenting explains every parameter
- Easy color, marker, and style modifications
- Multiple layout options (single/multi-panel)

### Scientific Best Practices
- Inward-pointing ticks on all sides
- Proper axis limits and tick spacing
- High-resolution output (300 DPI)
- Vector graphics (PDF) support

## 🔧 Customization Examples

### Change Colors
```python
ax.plot(x, y, 'r-', ...)  # Red solid line
ax.plot(x, y, 'b--', ...) # Blue dashed line
ax.plot(x, y, '#FF5733', ...) # Hex color
```

### Modify Markers
```python
ax.plot(x, y, 'ro-', markersize=6, markevery=5)  # Red circles every 5 points
ax.plot(x, y, 'bs-', markersize=8)  # Blue squares
```

### Add Annotations
```python
ax.annotate('Peak', xy=(3.14, 1.0), xytext=(5, 1.3),
           arrowprops=dict(arrowstyle='->', lw=2))
```

## 📋 Requirements

- Python 3.7+
- NumPy >= 1.19.0
- Matplotlib >= 3.3.0
- SciPy >= 1.5.0 (optional, for some statistical functions)
- LaTeX (optional, for professional typography)

See [INSTALL.md](INSTALL.md) for detailed installation instructions.

## 🎓 Learning Path

1. **Beginners**: Start with [TUTORIAL.md](TUTORIAL.md) for step-by-step guidance
2. **Quick Users**: Check [QUICK_REFERENCE.md](QUICK_REFERENCE.md) to find the right template
3. **Advanced**: Explore template combinations and customizations in each file

## 📖 Template Structure

Each template follows a consistent structure:

```python
# 1. Font and text configuration
# 2. Data generation/loading
# 3. Plot styling parameters
# 4. Figure creation and plotting
# 5. Axis configuration
# 6. Tick formatting
# 7. Save and display
# 8. Additional tips and examples
```

## 🤝 Contributing

Contributions are welcome! Whether it's:
- Bug fixes
- New templates
- Documentation improvements
- Example figures

Please feel free to submit issues or pull requests.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Akhil Reddy Peeketi**
- Postdoctoral Research Associate, Los Alamos National Laboratory
- Research: Quantum-to-Continuum Scale Modeling for Advanced Energy and Actuation Materials
- Email: peeketiakhilreddy@gmail.com

## 🙏 Acknowledgments

- Built on the excellent [Matplotlib](https://matplotlib.org/) library
- Inspired by best practices from scientific journals and conferences
- Designed for the research community

## 📧 Support

If you have questions or need help:
- Open an issue on GitHub
- Check existing issues and documentation
- Reach out via email

## ⭐ Star This Repository

If you find these templates useful, please consider giving this repository a star! It helps others discover these tools.

---

**Happy Plotting! 📊✨**
