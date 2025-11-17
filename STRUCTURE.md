# Repository Structure

This document explains the organization of the Scientific Plotting Templates repository.

## Directory Structure

```
scientific-plotting-templates/
│
├── README.md                          # Main documentation and overview
├── LICENSE                            # MIT License
├── requirements.txt                   # Python package dependencies
├── .gitignore                        # Git ignore patterns
├── CHANGELOG.md                      # Version history and changes
│
├── INSTALL.md                        # Installation instructions
├── TUTORIAL.md                       # Comprehensive beginner tutorial
├── QUICK_REFERENCE.md                # Quick lookup guide
├── CONTRIBUTING.md                   # Contribution guidelines
├── STRUCTURE.md                      # This file
│
├── templates/                        # Main template directory
│   ├── simple_xy_plots.py           # Basic X-Y plots with examples
│   ├── simple_xy_plots_custom1.py   # Enhanced version with more comments
│   ├── template_line_plot.py        # Line plot template
│   ├── template_scatter_plot.py     # Scatter plot with colormap
│   ├── template_bar_chart.py        # Bar chart variations
│   ├── template_histogram_errorbar.py # Histograms and error bars
│   ├── template_contour_plot.py     # Contour plots
│   ├── template_heatmap.py          # 2D heatmaps
│   ├── template_dual_axis_plot.py   # Dual Y-axis plots
│   ├── template_filled_area.py      # Filled regions and annotations
│   ├── template_subplots.py         # Multiple subplot layouts
│   └── template_log_plot.py         # Logarithmic scale plots
│
├── examples/                         # Example outputs and use cases
│   ├── README.md                    # Examples overview
│   ├── basic/                       # Basic examples
│   │   ├── line_plot_example.pdf
│   │   ├── scatter_example.pdf
│   │   └── bar_chart_example.pdf
│   ├── advanced/                    # Advanced examples
│   │   ├── multi_panel.pdf
│   │   ├── publication_figure.pdf
│   │   └── complex_annotation.pdf
│   └── data/                        # Sample data files
│       ├── sample_data_1.csv
│       ├── sample_data_2.txt
│       └── README.md                # Data description
│
├── docs/                            # Additional documentation
│   ├── latex_guide.md              # LaTeX setup and usage
│   ├── color_guide.md              # Comprehensive color reference
│   ├── journal_requirements.md     # Journal-specific guidelines
│   └── faq.md                      # Frequently asked questions
│
└── tests/                           # Test scripts (future)
    ├── test_templates.py           # Template validation tests
    └── test_installation.py        # Installation verification
```

## File Descriptions

### Root Level Files

#### Documentation Files
- **README.md** - Main entry point with overview, features, and quick start
- **INSTALL.md** - Detailed installation instructions for all platforms
- **TUTORIAL.md** - Step-by-step guide for beginners
- **QUICK_REFERENCE.md** - Fast lookup for common tasks and syntax
- **CONTRIBUTING.md** - Guidelines for contributing to the project
- **STRUCTURE.md** - This file, explaining repository organization
- **CHANGELOG.md** - Version history and change tracking

#### Project Files
- **LICENSE** - MIT License for the project
- **requirements.txt** - Python package dependencies
- **.gitignore** - Files and directories to ignore in git

### Templates Directory

Contains all plotting templates. Each template is a standalone Python file that can be:
- Run directly to see example output
- Copied and modified for your specific needs
- Used as a reference for matplotlib syntax

**Template Naming Convention:**
- `template_*.py` - Primary templates with consistent structure
- `simple_*.py` - Simplified versions with more examples

**Template Structure:** All templates follow a consistent format:
1. File-level docstring with description and use cases
2. Import statements
3. Font and LaTeX configuration
4. Data generation/loading section
5. Styling parameters
6. Figure creation and plotting
7. Axis configuration and formatting
8. Save and display
9. Additional tips and variations in comments

### Examples Directory

**Purpose:** Provide sample outputs and demonstrate various use cases

**Structure:**
- `basic/` - Simple, straightforward examples
- `advanced/` - Complex, multi-panel figures
- `data/` - Sample datasets for testing

**File Types:**
- PDF files: Example outputs from templates
- PNG files: Raster versions for quick viewing
- Data files: Sample datasets (CSV, TXT, Excel)

### Documentation Directory (docs/)

**Optional directory for extended documentation**

Potential contents:
- Detailed LaTeX setup guides
- Comprehensive color palette references
- Journal-specific formatting requirements
- Advanced customization guides
- FAQ compilation

### Tests Directory

**Future addition for quality assurance**

Will contain:
- Template validation scripts
- Installation verification tests
- Output quality checks
- Automated testing framework

## Usage Patterns

### For New Users

**Start here:**
1. `README.md` - Understand what the project offers
2. `INSTALL.md` - Set up your environment
3. `TUTORIAL.md` - Learn the basics step by step
4. Choose a template from `templates/`
5. Refer to `QUICK_REFERENCE.md` when needed

### For Experienced Users

**Quick workflow:**
1. `QUICK_REFERENCE.md` - Find the right template
2. Copy template from `templates/`
3. Replace sample data with your own
4. Customize and save

### For Contributors

**Contribution workflow:**
1. `CONTRIBUTING.md` - Understand contribution process
2. `STRUCTURE.md` - Know where files belong
3. Create/modify in appropriate directory
4. Update relevant documentation
5. Submit pull request

## File Organization Principles

### Templates
- **Self-contained**: Each template is a complete, runnable file
- **Well-documented**: Extensive inline comments
- **Consistent structure**: All follow the same organization
- **Example data**: Generate sample data if none provided

### Documentation
- **Layered complexity**: From quick start to deep dives
- **Cross-referenced**: Documents link to each other
- **Searchable**: Clear headings and table of contents
- **Maintained**: Kept in sync with code changes

### Examples
- **Diverse**: Cover various use cases and complexity levels
- **Documented**: README explains each example
- **Reproducible**: Include data and instructions
- **High quality**: 300 DPI, publication-ready

## Adding New Content

### Adding a New Template

1. **Create file** in `templates/` with descriptive name:
   ```
   templates/template_new_plot_type.py
   ```

2. **Follow structure** - Use existing templates as reference

3. **Update documentation**:
   - Add to README.md template table
   - Add to QUICK_REFERENCE.md decision tree
   - Add example if complex
   - Update CHANGELOG.md

### Adding New Examples

1. **Generate output** from template

2. **Save in appropriate directory**:
   - Simple example → `examples/basic/`
   - Complex example → `examples/advanced/`
   - Data file → `examples/data/`

3. **Update examples README** with description

### Adding Documentation

1. **Choose appropriate location**:
   - Core docs → Root level
   - Extended guides → `docs/`
   - Template-specific → Comments in template

2. **Follow markdown style**:
   - Clear headings
   - Code blocks with syntax highlighting
   - Cross-references to related docs

3. **Update README** with link if major documentation

## Maintenance

### Regular Updates
- Keep templates compatible with latest matplotlib
- Update examples with improved practices
- Refresh documentation based on user feedback
- Update dependencies in requirements.txt

### Version Control
- Follow semantic versioning
- Update CHANGELOG.md for all changes
- Tag releases appropriately
- Maintain backwards compatibility when possible

## Best Practices

### For Template Files
- ✅ Include comprehensive docstring
- ✅ Comment every major section
- ✅ Provide usage examples in comments
- ✅ Use consistent variable names
- ✅ Generate sample data if file not found
- ✅ Handle errors gracefully

### For Documentation
- ✅ Use clear, simple language
- ✅ Include code examples
- ✅ Provide step-by-step instructions
- ✅ Add troubleshooting sections
- ✅ Keep formatting consistent
- ✅ Update when code changes

### For Examples
- ✅ Name files descriptively
- ✅ Include README explaining contents
- ✅ Provide both PDF and PNG when possible
- ✅ Include source data or generation method
- ✅ Show both simple and complex use cases

## Navigation Tips

### Finding Information

**"I want to create a [plot type]"**
→ QUICK_REFERENCE.md → templates/template_*.py

**"How do I install?"**
→ INSTALL.md

**"I'm new to plotting"**
→ TUTORIAL.md

**"Quick syntax lookup"**
→ QUICK_REFERENCE.md

**"How do I contribute?"**
→ CONTRIBUTING.md

**"What's the file structure?"**
→ STRUCTURE.md (this file)

## Future Organization

As the project grows, we may add:
- `scripts/` - Helper scripts for common tasks
- `styles/` - Matplotlib style sheets for journals
- `notebooks/` - Jupyter notebook tutorials
- `gallery/` - Interactive web gallery of examples
- `utils/` - Utility functions for data handling

## Questions?

If anything about the repository structure is unclear:
1. Check this document
2. Look at existing files for examples
3. Open an issue on GitHub
4. Refer to CONTRIBUTING.md

---

**Maintained by:** Akhil Reddy Peeketi  
**Last Updated:** 2025  
**Version:** 1.0
