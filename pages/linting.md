---
title: Linting
layout: default
---

# Linting

See [here for example configuration](https://github.com/paddyroddy/python-template) for some of these.

## Code formatting

| Name     | Short description | 🚦 |
| -------- | ------------------| :-: |
| [black](https://black.readthedocs.io/en/stable/) | Opinionated formatter, defaults to 88 characters per line. | 🟢 |
| [autopep8](https://github.com/hhatto/autopep8) | Formatter which conforms to PEP 8. | 🟠 |
| [isort](https://pycqa.github.io/isort/) | Sorts imports alphabetically, splits into first/third party, works on python & cython code. | 🟢 |
| [mypy](https://mypy.readthedocs.io/en/stable/) | Static type checker, won't fail if no typing but will if typing is incorrect. | 🟢 |
| [pre-commit](https://pre-commit.com/) | Universal tool which performs a git hook on commit, allows you to run linters/formatters on any code. | 🟢 |
| [pycodestyle](https://pycodestyle.pycqa.org/en/latest/) | Linter which checks for errors. | 🟠 |
| [pyflakes](https://github.com/PyCQA/pyflakes) | Linter which checks for errors. | 🟠 |
| [pylint](https://pylint.readthedocs.io/en/latest/) | Linter which checks for errors. | 🟠 |
| [ruff](https://github.com/charliermarsh/ruff) | A very fast linter which incorporates other linters. | 🟠 |
| [sourcery](https://sourcery.ai/) | An AI code reviewer which simplifies code, has a free version but can pay for fancier features. | 🟠 |
| [toml-sort](https://toml-sort.readthedocs.io/en/latest/) | Sorts TOML files which are now part of PEP 8. | 🟢 |
| [yapf](https://github.com/google/yapf) | Google formatter. | 🟠 |
| [flake8](https://flake8.pycqa.org/en/latest/) | Linter which complains if code doesn't follow a rule. Does not support modern `pyproject.toml` configuration. | 🔴 |
