---
title: Linting
layout: default
---

# Linting

See [here for example configuration](https://github.com/paddyroddy/python-template) for some of these.

## Code formatting

| Name     | Short description | 🚦 |
| -------- | ------------------| :-: |
| [pre-commit](https://pre-commit.com/) | Universal tool which performs a git hook on commit, allows you to run linters/formatters on any code. A tool to automatically run many of the tools listed below. | 🟢 |
| [black](https://black.readthedocs.io/en/stable/) | Opinionated formatter, defaults to 88 characters per line. | 🟢 |
| [isort](https://pycqa.github.io/isort/) | Sorts imports alphabetically, splits into first/third party, works on python & cython code. | 🟢 |
| [toml-sort](https://toml-sort.readthedocs.io/en/latest/) | Sorts TOML files which are now part of PEP 8. | 🟢 |
| [autopep8](https://github.com/hhatto/autopep8) | Formatter which conforms to PEP 8. | 🟠 |
| [pycodestyle](https://pycodestyle.pycqa.org/en/latest/) | Linter which checks for errors. | 🟠 |
| [pyflakes](https://github.com/PyCQA/pyflakes) | Linter which checks for errors. | 🟠 |
| [pylint](https://pylint.readthedocs.io/en/latest/) | Linter which checks for errors. | 🟠 |
| [ruff](https://github.com/charliermarsh/ruff) | A very fast linter which incorporates a range of other linters. | 🟢 |
| [sourcery](https://sourcery.ai/) | An AI code reviewer which simplifies code, has a free version but can pay for fancier features. | 🟠 |
| [yapf](https://github.com/google/yapf) | Google formatter. | 🟠 |
| [flake8](https://flake8.pycqa.org/en/latest/) | Linter which complains if code doesn't follow a rule. Does not support modern `pyproject.toml` configuration. | 🔴 |

## Type checking

| Name     | Short description | 🚦 |
| -------- | ------------------| :-: |
| [mypy](https://mypy.readthedocs.io/en/stable/) | Static type checker, won't fail if no typing but will if typing is incorrect. | 🟢 |
