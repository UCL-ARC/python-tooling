---
title: Jupyter Notebooks
layout: default
---

# Jupyter notebooks

We generally recommend packaging reusable code components into Python modules where possible.
However occasionally we support researchers who prefer a notebook environment or projects which want to provide examples and tutorials in notebook format.
Notebooks can also be a valid alternative to Python scripts for running and recording the results of numerical experiments for example.

## Live executable environments

| Name                                                                                                                                                                                                  | Short description                                                                                                                                             | 🚦  |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-: |
| [binder](https://mybinder.org/)                                                                                                                                                                       | Turns a Git repository into a collection of interactive notebooks                                                                                             | 🟢  |
| [Google Colab](https://colab.google/)                                                                                                                                                                 | Colab is a hosted Jupyter Notebook service that requires no setup to use and provides free access to computing resources, including GPUs and TPUs.            | 🟢  |
| [GitHub codespaces with JupyterLab](https://docs.github.com/en/codespaces/developing-in-a-codespace/getting-started-with-github-codespaces-for-machine-learning#opening-your-codespace-in-jupyterlab) | A codespace is a development environment that is hosted in the cloud and can run [Python and Jupyter notebooks](https://github.com/github/codespaces-jupyter) | 🟠  |

## Linting

Many of [our recommended linters](linting) don't work out-of-the box on Jupyter notebooks, however [nbQA] has been found to work well.
This is a translation tool that can be used to run our recommended linters over notebooks.

There is one exception: we've found that [black]'s own Jupyter extension works more reliably than [black] via [nbQA].

| Name             | Short description                                                                | 🚦  |
| ---------------- | -------------------------------------------------------------------------------- | :-: |
| `black[jupyter]` | (also `black-jupyter`) [black] with the optional Jupyter extension.              | 🟢  |
| [nbQA]           | Recommended for all other linters ([ruff], [isort]) and [mypy].                  | 🟢  |
| [pre-commit]     | Has cell output cleanup hooks (if desired). Also found to work well with [nbQA]. | 🟢  |
| `nbqa black`     | [black] via [nbQA].                                                              | 🟠  |

<!-- URLs for a more readable table & prose 👆 -->

[black]: https://nbqa.readthedocs.io/en/latest/index.html
[nbQA]: https://nbqa.readthedocs.io/en/latest/index.html
[isort]: https://pycqa.github.io/isort
[ruff]: https://github.com/charliermarsh/ruff
[mypy]: https://mypy.readthedocs.io/en/stable
[pre-commit]: https://github.com/kynan/nbstripout

<!-- TODO: more sections to consider>

## IDE plugins

## CI

<-->
