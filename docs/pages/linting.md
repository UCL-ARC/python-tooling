---
title: Linting
layout: default
---

## Linting

See
[here for an example configuration](https://github.com/UCL-ARC/python-tooling/blob/main/%7B%7Bcookiecutter.project_slug%7D%7D/.pre-commit-config.yaml)
for some of these.

### Code formatting

| Name                                                     | Short description                                                                                                                                                                                     | 🚦  |
| -------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-: |
| [pre-commit](https://pre-commit.com/)                    | Universal tool which performs a git hook on commit, allows you to run linters/formatters on any code. A tool to automatically run many of the tools listed below.                                     | 🟢  |
| [ruff-format](https://github.com/astral-sh/ruff)         | A drop-in replacement for `black` (and also super fast). A nice "no-need to think" code formatter. If you have your own opinions about code style, you might not like this.                           | 🟢  |
| [ruff](https://github.com/astral-sh/ruff)                | A fast linter which incorporates a range of other linters. Notably [isort](https://pycqa.github.io/isort/) can be included as a [ruff rule](https://docs.astral.sh/ruff/rules/) (which we recommend). | 🟢  |
| [toml-sort](https://github.com/pappasam/toml-sort) | Sorts TOML files which are now part of PEP 8.                                                                                                                                                         | 🟢  |
| [autopep8](https://github.com/hhatto/autopep8)           | Formatter which conforms to PEP 8.                                                                                                                                                                    | 🟠  |
| [black](https://black.readthedocs.io/en/stable/)         | Opinionated formatter, defaults to 88 characters per line. Widely used, but we now recommend `ruff-format` in its place.                                                                              | 🟠  |
| [isort](https://pycqa.github.io/isort/)                  | Sorts imports alphabetically, splits into first/third party, works on python & cython code. We recommend this, but it can be included in `ruff`, which is simpler.                                    | 🟠  |
| [pycodestyle](https://pycodestyle.pycqa.org/en/latest/)  | Linter which checks for errors.                                                                                                                                                                       | 🟠  |
| [pyflakes](https://github.com/PyCQA/pyflakes)            | Linter which checks for errors.                                                                                                                                                                       | 🟠  |
| [pylint](https://pylint.readthedocs.io/en/latest/)       | Linter which checks for errors.                                                                                                                                                                       | 🟠  |
| [sourcery](https://sourcery.ai/)                         | An AI code reviewer which simplifies code, has a free version but can pay for fancier features.                                                                                                       | 🟠  |
| [yapf](https://github.com/google/yapf)                   | Google formatter.                                                                                                                                                                                     | 🟠  |
| [flake8](https://flake8.pycqa.org/en/latest/)            | Linter which complains if code doesn't follow a rule. Does not support modern `pyproject.toml` configuration.                                                                                         | 🔴  |

### Type checking

| Name                                           | Short description                                                             | 🚦  |
| ---------------------------------------------- | ----------------------------------------------------------------------------- | :-: |
| [mypy](https://mypy.readthedocs.io/en/stable/) | Static type checker, won't fail if no typing but will if typing is incorrect. | 🟢  |
