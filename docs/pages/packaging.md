---
title: Packaging
layout: default
---

# General packaging

A common question facing developers is "_How much code should go into a
package?_". Where code to solve a research problem might be large and perform
several tasks at once typically one should try to stick to a mantra of doing one
thing well. The following questions can be helpful when trying to abide by this
mantra:

- What do I want my package to provide?
- How will users interact with or use the code in my package?
- Is everything I'm including in the package relevant or useful in supporting
  it's main purpose?

In Python, a [package](https://docs.python.org/3/reference/import.html#packages)
is a collection of one or more
[modules](https://docs.python.org/3/glossary.html#term-module) to perform
software tasks. Typically there is a separate git repository per package, and we
recommend you stick to this. You can always add the packages as dependencies to
a higher-level package which is effectively the same, but much easier to reuse.

# Packaging tools

| Name                                                                  | Short description                                                                                                           | 🚦  |
| --------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --- |
| [setuptools](https://setuptools.pypa.io)                              | A widely used build backend, used to configure a Python package.                                                            | 🟢  |
| [setuptools-scm](https://github.com/pypa/setuptools_scm/)             | Provides automatic versioning Python packages. Also automatically adds all files under source control to the sdist / wheel. | 🟢  |
| [poetry](https://github.com/python-poetry/poetry)                     | A tool that lets you build and package your project as well as managing dependencies                                        | 🟠  |
| [twine](https://pypi.org/project/twine/)                              | Tool for publishing Python packages on PyPI.                                                                                | 🟠  |
| [bump2version](https://pypi.org/project/bump2version/)                | Tool for version-bumping your software. No longer maintained                                                                | 🔴  |
| [bump-my-version](https://github.com/callowayproject/bump-my-version) | Tool for version-bumping your software. Superseded by setuptools_scm                                                        | 🔴  |

# Building

| Name                                                  | Short description                                                                                         | 🚦  |
| ----------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --- |
| [build](https://pypa-build.readthedocs.io/en/stable/) | Straightforward tool to build a Python package.                                                           | 🟢  |
| [cibuildwheel](https://cibuildwheel.readthedocs.io)   | Builds python wheels for the main operating systems on continuous integration runs (e.g. GitHub actions). | 🟠  |

## Package configuration file

| Name                                                                                               | Short description                                                                                                                                                  | 🚦  |
| -------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --- |
| [pyproject.toml](https://pip.pypa.io/en/stable/reference/build-system/pyproject-toml/)             | Contains build system requirements and information, which are used by pip to build the package. It is becoming the accepted standard and we strongly recommend it. | 🟢  |
| [setup.py](https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/)  | Strongly coupled with setuptools and therefore not recommended.                                                                                                    | 🟠  |
| [setup.cfg](https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/) | An ini file that contains defaults for setup.py commands.                                                                                                          | 🟠  |

## Conda

These tools are helpful if you're looking to publish your package on
[conda-forge](https://conda-forge.org/), so users can install it through the
[Conda](https://docs.conda.io/projects/conda/en/stable/) package manager.

| Name                                                      | Short description                                                           | 🚦  |
| --------------------------------------------------------- | --------------------------------------------------------------------------- | :-: |
| [GraySkull](https://github.com/conda-incubator/grayskull) | A tool for automatic Conda recipe generation (aimed at conda-forge, above). | 🟢  |
