---
title: Packaging
layout: default
---

# Packaging

| Name                                                      | Short description                                                                                                           | 🚦  |
| --------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | :-: |
| [build](https://pypa-build.readthedocs.io/en/stable/)     | Straightforward tool to build a Python package.                                                                             | 🟢  |
| [cibuildwheel](https://cibuildwheel.readthedocs.io)       | Builds python wheels for the main operating systems on continuous integration runs (e.g. GitHub actions).                   | 🟢  |
| [setuptools](https://setuptools.pypa.io)                  | A widely used build backend, used to configure a Python package.                                                            | 🟢  |
| [setuptools-scm](https://github.com/pypa/setuptools_scm/) | Provides automatic versioning Python packages. Also automatically adds all files under source control to the sdist / wheel. | 🟢  |

## Conda

These tools are helpful if you're looking to publish your package on [conda-forge](https://conda-forge.org/), so users can install it through the [conda](https://docs.conda.io/en/latest/) or [mamba](https://mamba.readthedocs.io/en/latest/index.html) package managers.

| Name                                                      | Short description                                                           | 🚦  |
| --------------------------------------------------------- | --------------------------------------------------------------------------- | :-: |
| [GraySkull](https://github.com/conda-incubator/grayskull) | A tool for automatic conda recipe generation (aimed at conda-forge, above). | 🟢  |
