# Contributing to Scientific Plotting Templates

Thank you for your interest in contributing! This project aims to help researchers and students create publication-quality figures easily.

## How to Contribute

### Ways to Contribute

1. **Report bugs** - Found an issue? Let us know!
2. **Suggest enhancements** - Have an idea for a new feature or template?
3. **Submit new templates** - Created a useful template? Share it!
4. **Improve documentation** - Help make the guides clearer
5. **Share examples** - Show how you've used the templates
6. **Fix typos** - Even small corrections help!

## Getting Started

### Reporting Bugs

When reporting bugs, please include:

- **Description**: What happened vs. what you expected
- **Code snippet**: Minimal example that reproduces the issue
- **Environment**: Python version, OS, matplotlib version
- **Error message**: Full traceback if applicable

**Template for bug reports:**

```markdown
## Bug Description
[Clear description of the bug]

## To Reproduce
Steps to reproduce the behavior:
1. Run template '...'
2. Modify line '...'
3. See error

## Expected Behavior
[What you expected to happen]

## Environment
- Python version: 3.x
- Matplotlib version: 3.x
- OS: [e.g., Windows 10, macOS 12, Ubuntu 22.04]

## Error Message
```python
[Paste full error traceback here]
```

## Suggesting Enhancements

Enhancement suggestions are welcome! Please include:

- **Use case**: Why is this enhancement needed?
- **Proposed solution**: How should it work?
- **Alternatives**: Other approaches you've considered
- **Examples**: If possible, show what the output should look like

## Submitting New Templates

We'd love to include more templates! A good template should:

### Template Requirements

1. **Follow existing structure**:
   - Font and text configuration section
   - Data generation/loading section
   - Plot styling parameters section
   - Figure creation section
   - Comprehensive comments

2. **Be well-documented**:
   - Clear docstring at the top explaining purpose
   - Comments explaining every section
   - Examples in comments showing variations
   - Tips section at the end

3. **Use consistent styling**:
   - Follow the LaTeX configuration pattern
   - Use similar variable names (fs, r, linewidth)
   - Include tick formatting
   - Set proper DPI for saving

4. **Include metadata**:
   - Template name and description
   - Use cases
   - Example output description
   - Data requirements

### Template Submission Process

1. **Create your template** following the structure above
2. **Test thoroughly** - ensure it runs without errors
3. **Add example** - Include sample output (PDF or PNG)
4. **Write documentation** - Add entry to QUICK_REFERENCE.md
5. **Submit pull request** - See process below

## Pull Request Process

### Before Submitting

1. **Test your changes**:
   ```bash
   python your_template.py
   ```
   Ensure it runs without errors

2. **Check code style**:
   - Clear, descriptive comments
   - Consistent variable naming
   - Proper indentation (4 spaces)

3. **Update documentation**:
   - Add your template to README.md template table
   - Add decision tree entry in QUICK_REFERENCE.md
   - Update TUTORIAL.md if adding new concepts

### Submitting a Pull Request

1. **Fork the repository**
   - Click "Fork" on GitHub
   - Clone your fork: `git clone https://github.com/ARPeeketi/Template_Scientifc_Figures.git`

2. **Create a branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```
   Or for bug fixes:
   ```bash
   git checkout -b fix/bug-description
   ```

3. **Make your changes**:
   - Add or modify files
   - Test thoroughly
   - Commit with clear messages:
   ```bash
   git add .
   git commit -m "Add template for violin plots"
   ```

4. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```

5. **Open a pull request**:
   - Go to the original repository on GitHub
   - Click "New Pull Request"
   - Select your branch
   - Fill in the PR template (see below)

### Pull Request Template

```markdown
## Description
[Brief description of changes]

## Type of Change
- [ ] Bug fix
- [ ] New template
- [ ] Documentation update
- [ ] Enhancement to existing template

## Checklist
- [ ] Code follows project style guidelines
- [ ] Comments are clear and comprehensive
- [ ] Documentation updated (README, QUICK_REFERENCE, etc.)
- [ ] Tested on my local machine
- [ ] No errors or warnings

## Testing
[Describe how you tested the changes]

## Screenshots (if applicable)
[Add screenshots of plot output]

## Related Issues
[Link to related issue, if any: #123]
```

## Code Style Guidelines

### Python Style

- **Follow PEP 8** where reasonable
- **Use descriptive names**:
  ```python
  # Good
  fs = 24.0  # Font size
  linewidth = 2.0
  
  # Avoid
  f = 24.0
  lw = 2.0
  ```

- **Comment generously**:
  ```python
  # Set axis limits to show full data range with 10% padding
  ax.set_xlim(x.min() * 0.9, x.max() * 1.1)
  ```

- **Group related code**:
  ```python
  # ============================================================================
  # AXIS CONFIGURATION
  # ============================================================================
  ax.set_xlim(0, 10)
  ax.set_ylim(-1, 1)
  ax.set_xlabel(...)
  ```

### Template Structure

All templates should follow this structure:

```python
"""
TEMPLATE: [Template Name]
========================
Description of what this template does.
Suitable for: [Use cases]
"""

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# Font configuration
# Data loading
# Styling parameters
# Figure creation
# Plotting
# Axis configuration
# Tick formatting
# Save and display
# Additional tips section
```

### Comments

- **Explain "why", not just "what"**:
  ```python
  # Good: Use log scale to handle data spanning 6 orders of magnitude
  ax.set_yscale('log')
  
  # Less helpful: Set y-axis to log scale
  ax.set_yscale('log')
  ```

- **Include examples in comments**:
  ```python
  # Alternative markers: 'o', 's', '^', 'v', 'D', '*'
  ax.plot(x, y, 'o')
  ```

## Documentation Guidelines

### README Updates

When adding a new template, update:

1. **Features section** - Add template to the list
2. **Table of templates** - Add row with description and use case
3. **Any relevant examples** - If your template introduces new concepts

### QUICK_REFERENCE Updates

Add your template to:

1. **Decision tree** - Where does it fit?
2. **Template at-a-glance table** - One-line description
3. **Common tasks** - If introducing new functionality

### TUTORIAL Updates

If your template introduces new concepts:

1. Add a section explaining the concept
2. Include a simple example
3. Add to practice exercises if appropriate

## Community Guidelines

### Code of Conduct

- **Be respectful** - Treat everyone with kindness
- **Be patient** - Remember everyone has different experience levels
- **Be constructive** - Offer helpful suggestions, not just criticism
- **Be collaborative** - We're all here to help each other

### Communication

- **Be clear** - Explain your ideas thoroughly
- **Be responsive** - Try to respond to comments on your PRs
- **Ask questions** - If something is unclear, ask!

## Recognition

Contributors will be:
- Listed in the project README
- Credited in release notes
- Acknowledged in any resulting publications (if substantial contribution)

## Questions?

If you have questions about contributing:

1. Check existing issues and pull requests
2. Open a discussion on GitHub
3. Reach out to the maintainer

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

**Thank you for helping make scientific visualization more accessible! 🙏**
