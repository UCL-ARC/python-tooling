---
title: Packaging
layout: default
---

# Packaging

| Name                                                                  | Short description                                                                                                           | 🚦  |                     Used by                     |
| --------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --- | :---------------------------------------------: |
| [setuptools](https://setuptools.pypa.io)                              | A widely used build backend, used to configure a Python package.                                                            | 🟢  | [autodE](https://github.com/duartegroup/autodE) |
| [setuptools-scm](https://github.com/pypa/setuptools_scm/)             | Provides automatic versioning Python packages. Also automatically adds all files under source control to the sdist / wheel. | 🟢  | [btrack](https://github.com/quantumjot/btrack)  |
| [poetry](https://github.com/python-poetry/poetry)                     | A tool that lets you build and package your project as well as managing dependencies                                        | 🟠  |                                                 |
| [twine](https://pypi.org/project/twine/)                              | Tool for publishing Python packages on PyPI.                                                                                | 🟠  |                                                 |
| [bump2version](https://pypi.org/project/bump2version/)                | Tool for version-bumping your software. No longer maintained                                                                | 🔴  |                                                 |
| [bump-my-version](https://github.com/callowayproject/bump-my-version) | Tool for version-bumping your software. Superseded by setuptools_scm                                                        | 🔴  |                                                 |

# Building

| Name                                                  | Short description                                                                                         | 🚦  |                         Used by                          |
| ----------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --- | :------------------------------------------------------: |
| [build](https://pypa-build.readthedocs.io/en/stable/) | Straightforward tool to build a Python package.                                                           | 🟢  |                                                          |
| [cibuildwheel](https://cibuildwheel.readthedocs.io)   | Builds python wheels for the main operating systems on continuous integration runs (e.g. GitHub actions). | 🟠  | [streamtracer](https://github.com/dstansby/streamtracer) |

## Package configuration file

| Name                                                                                               | Short description                                                                               | 🚦  | Used by |
| -------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | --- | :-----: |
| [pyproject.toml](https://pip.pypa.io/en/stable/reference/build-system/pyproject-toml/)             | Contains build system requirements and information, which are used by pip to build the package. | 🟢  |         |
| [setup.py](https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/)  | Strongly coupled with setuptools and therefore not recommended.                                         | 🟠  |         |
| [setup.cfg](https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/) | An ini file that contains option defaults for setup.py commands                                 | 🟠  |         |

## Conda

These tools are helpful if you're looking to publish your package on [conda-forge](https://conda-forge.org/), so users can install it through the [conda](https://docs.conda.io/en/latest/) or [mamba](https://mamba.readthedocs.io/en/latest/index.html) package managers.

| Name                                                      | Short description                                                           | 🚦  | Used by |
| --------------------------------------------------------- | --------------------------------------------------------------------------- | --- | :-----: |
| [GraySkull](https://github.com/conda-incubator/grayskull) | A tool for automatic conda recipe generation (aimed at conda-forge, above). | 🟢  |         |
