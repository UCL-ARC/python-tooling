---
title: Packaging
layout: default
---

# General packaging

A common question facing developers is "_How much code should go into a
package?_". Where code to solve a research problem might be large and perform
several tasks at once typically one should try to stick to a mantra of doing one
thing well.

In Python, a [package](https://docs.python.org/3/reference/import.html#packages)
is a collection of one or more
[modules](https://docs.python.org/3/glossary.html#term-module) to perform
software tasks. Typically there is a separate git repository per package, and
we recommend you stick to this. You can always add the packages as dependencies
to a higher-level package which is effectively the same, but much easier to
reuse.

# Packaging tools

| Name                                                      | Short description                                                                                                           | 🚦  |
| --------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | :-: |
| [build](https://pypa-build.readthedocs.io/en/stable/)     | Straightforward tool to build a Python package.                                                                             | 🟢  |
| [cibuildwheel](https://cibuildwheel.readthedocs.io)       | Builds python wheels for the main operating systems on continuous integration runs (e.g. GitHub actions).                   | 🟢  |
| [setuptools](https://setuptools.pypa.io)                  | A widely used build backend, used to configure a Python package.                                                            | 🟢  |
| [setuptools-scm](https://github.com/pypa/setuptools_scm/) | Provides automatic versioning Python packages. Also automatically adds all files under source control to the sdist / wheel. | 🟢  |

## Conda

These tools are helpful if you're looking to publish your package on [conda-forge](https://conda-forge.org/), so users can install it through the [Conda](https://docs.conda.io/projects/conda/en/stable/) package manager.

| Name                                                      | Short description                                                           | 🚦  |
| --------------------------------------------------------- | --------------------------------------------------------------------------- | :-: |
| [GraySkull](https://github.com/conda-incubator/grayskull) | A tool for automatic Conda recipe generation (aimed at conda-forge, above). | 🟢  |
