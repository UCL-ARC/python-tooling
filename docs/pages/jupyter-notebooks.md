---
title: Jupyter Notebooks
layout: default
---

# Jupyter notebooks

We generally recommend developing code for packaging into python modules if possible.
However occasionally we support researchers who prefer a notebook environment or projects which want to provide examples and tutorials in notebook format.

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
