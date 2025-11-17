# Installation Guide

This guide provides detailed instructions for setting up the Scientific Plotting Templates on your system.

## Table of Contents
- [Quick Installation](#quick-installation)
- [Detailed Installation](#detailed-installation)
- [LaTeX Setup (Optional)](#latex-setup-optional)
- [Verification](#verification)
- [Troubleshooting](#troubleshooting)

## Quick Installation

For most users, this is all you need:

```bash
# Clone the repository
git clone https://github.com/your-username/scientific-plotting-templates.git
cd scientific-plotting-templates

# Install Python dependencies
pip install -r requirements.txt

# Test installation
python template_line_plot.py
```

## Detailed Installation

### Step 1: Python Installation

Ensure you have Python 3.7 or higher installed:

```bash
python --version
# Should show: Python 3.7.x or higher
```

If Python is not installed:
- **Windows**: Download from [python.org](https://www.python.org/downloads/)
- **macOS**: `brew install python3` (requires Homebrew)
- **Linux**: `sudo apt-get install python3 python3-pip` (Ubuntu/Debian)

### Step 2: Virtual Environment (Recommended)

Create an isolated environment for the project:

```bash
# Create virtual environment
python -m venv plotting_env

# Activate it
# On Windows:
plotting_env\Scripts\activate
# On macOS/Linux:
source plotting_env/bin/activate
```

### Step 3: Install Dependencies

#### Option A: Using requirements.txt (Recommended)

```bash
pip install -r requirements.txt
```

#### Option B: Manual Installation

```bash
pip install numpy>=1.19.0
pip install matplotlib>=3.3.0
pip install scipy>=1.5.0
```

### Step 4: Verify Installation

Run this Python command to check if everything is installed:

```python
python -c "import numpy; import matplotlib; import scipy; print('All packages installed successfully!')"
```

## LaTeX Setup (Optional)

LaTeX rendering provides professional typography and is **highly recommended** for publication-quality figures.

### Why Use LaTeX?

- Professional mathematical typesetting
- Consistent fonts across figures and documents
- Support for scientific notation and symbols
- Required by many journals

### Installing LaTeX

#### Windows

1. **Download MiKTeX**: [miktex.org/download](https://miktex.org/download)
2. **Install** using the downloaded installer
3. **Add to PATH**: MiKTeX installer usually does this automatically

#### macOS

```bash
# Install MacTeX (recommended)
brew install --cask mactex

# Lightweight alternative: BasicTeX
brew install --cask basictex
```

#### Linux

```bash
# Ubuntu/Debian
sudo apt-get install texlive-latex-base texlive-latex-extra texlive-fonts-recommended

# Fedora/CentOS
sudo dnf install texlive-scheme-basic texlive-collection-latexextra

# Arch Linux
sudo pacman -S texlive-core texlive-latexextra
```

### Verify LaTeX Installation

```bash
# Check if LaTeX is installed
pdflatex --version

# Should show version information
```

### Using Templates Without LaTeX

If LaTeX is not installed or you prefer not to use it, modify the templates:

**Comment out these lines at the top of any template:**

```python
# Comment out these lines:
# plt.rc('text', usetex=True)
# preamble = '\\usepackage{times}\n\\usepackage{newtxmath}\n\\usepackage{siunitx}\n'
# plt.rc('text.latex', preamble=preamble)
```

The templates will use Matplotlib's default fonts instead.

## Package Details

### Required Packages

| Package | Version | Purpose |
|---------|---------|---------|
| numpy | ≥ 1.19.0 | Numerical arrays and operations |
| matplotlib | ≥ 3.3.0 | Plotting and visualization |

### Optional Packages

| Package | Version | Purpose |
|---------|---------|---------|
| scipy | ≥ 1.5.0 | Statistical distributions, curve fitting |
| pandas | ≥ 1.1.0 | Data manipulation (if loading CSV/Excel files) |
| seaborn | ≥ 0.11.0 | Additional color palettes |

### Installing Optional Packages

```bash
# For statistical functions
pip install scipy

# For data handling
pip install pandas

# For enhanced color schemes
pip install seaborn
```

## Verification

### Test Script

Create a file named `test_installation.py`:

```python
"""
Test script to verify installation
"""
import sys

print("Testing Python installation...")
print(f"Python version: {sys.version}")

try:
    import numpy as np
    print(f"✓ NumPy version: {np.__version__}")
except ImportError:
    print("✗ NumPy not found")

try:
    import matplotlib
    print(f"✓ Matplotlib version: {matplotlib.__version__}")
except ImportError:
    print("✗ Matplotlib not found")

try:
    import scipy
    print(f"✓ SciPy version: {scipy.__version__}")
except ImportError:
    print("✗ SciPy not found (optional)")

# Test LaTeX
import matplotlib.pyplot as plt
try:
    plt.rc('text', usetex=True)
    print("✓ LaTeX rendering available")
except:
    print("✗ LaTeX not available (optional)")
    plt.rc('text', usetex=False)

# Test basic plotting
print("\nTesting basic plot generation...")
try:
    import numpy as np
    import matplotlib.pyplot as plt
    
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(x, y, 'r-', linewidth=2)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    plt.savefig('test_plot.png', dpi=150, bbox_inches='tight')
    plt.close()
    
    print("✓ Test plot saved as 'test_plot.png'")
    print("\n✓✓✓ All tests passed! ✓✓✓")
except Exception as e:
    print(f"✗ Error during plotting: {e}")
```

Run the test:

```bash
python test_installation.py
```

### Expected Output

```
Testing Python installation...
Python version: 3.9.x
✓ NumPy version: 1.21.x
✓ Matplotlib version: 3.5.x
✓ SciPy version: 1.7.x
✓ LaTeX rendering available

Testing basic plot generation...
✓ Test plot saved as 'test_plot.png'

✓✓✓ All tests passed! ✓✓✓
```

## Troubleshooting

### Common Issues and Solutions

#### Issue 1: "ModuleNotFoundError: No module named 'matplotlib'"

**Solution:**
```bash
pip install matplotlib
# or if using Python 3 specifically:
pip3 install matplotlib
```

#### Issue 2: LaTeX rendering errors

**Error message:**
```
RuntimeError: Failed to process string with tex because latex could not be found
```

**Solution:**
- **Option A**: Install LaTeX (see [LaTeX Setup](#latex-setup-optional))
- **Option B**: Disable LaTeX rendering by commenting out usetex lines

#### Issue 3: Permission denied during pip install

**Solution:**
```bash
# Use --user flag
pip install --user -r requirements.txt

# Or use virtual environment (recommended)
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
pip install -r requirements.txt
```

#### Issue 4: Matplotlib backend issues (no display)

**Error message:**
```
UserWarning: Matplotlib is currently using agg, which is a non-GUI backend
```

**Solution:**

Add this at the beginning of your script:
```python
import matplotlib
matplotlib.use('TkAgg')  # or 'Qt5Agg', 'Qt4Agg'
import matplotlib.pyplot as plt
```

Or set the backend in your matplotlibrc file.

#### Issue 5: Font not found warnings

**Warning message:**
```
findfont: Font family 'Times New Roman' not found
```

**Solution:**

**On Linux:**
```bash
sudo apt-get install msttcorefonts -qq
rm ~/.cache/matplotlib -rf
```

**On macOS:**
Times New Roman should be installed by default.

**On Windows:**
Times New Roman should be installed by default.

#### Issue 6: numpy/scipy version conflicts

**Solution:**
```bash
# Upgrade to latest compatible versions
pip install --upgrade numpy scipy matplotlib
```

### Getting Help

If you encounter issues not covered here:

1. **Check Python version**: Ensure you're using Python 3.7+
2. **Update pip**: `pip install --upgrade pip`
3. **Check dependencies**: `pip list` to see installed packages
4. **Search GitHub Issues**: Someone may have had the same problem
5. **Create an issue**: Provide error messages and system information

## System-Specific Notes

### Windows

- Use PowerShell or Command Prompt
- May need to add Python to PATH during installation
- LaTeX installation takes ~4 GB of disk space (MiKTeX)

### macOS

- Homebrew recommended for package management
- May need to install Xcode Command Line Tools: `xcode-select --install`
- MacTeX is large (~4 GB); BasicTeX is a lighter alternative

### Linux

- Most distributions come with Python pre-installed
- May need development headers: `sudo apt-get install python3-dev`
- TeXLive full installation is large; texlive-latex-base is sufficient

## Updating

To update to the latest version:

```bash
cd scientific-plotting-templates
git pull origin main
pip install --upgrade -r requirements.txt
```

## Uninstallation

To remove the packages:

```bash
# If using virtual environment
deactivate
rm -rf plotting_env

# If installed globally
pip uninstall numpy matplotlib scipy
```

---

**For additional help, please open an issue on GitHub or consult the [README](README.md).**
