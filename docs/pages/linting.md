---
title: Linting
layout: default
---

# Linting

See [here for example configuration](https://github.com/UCL-ARC/python-tooling/blob/main/%7B%7Bcookiecutter.project_slug%7D%7D/.pre-commit-config.yaml) for some of these.

## Code formatting

| Name                                                     | Short description                                                                                                                                                 | 🚦  |
| -------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- |
| [ruff-format](https://github.com/astral-sh/ruff)         | Like `black` but super fast.                                                                                                                                      | 🟢  |
| [isort](https://pycqa.github.io/isort/)                  | Sorts imports alphabetically, splits into first/third party, works on python & cython code.                                                                       | 🟢  |
| [pre-commit](https://pre-commit.com/)                    | Universal tool which performs a git hook on commit, allows you to run linters/formatters on any code. A tool to automatically run many of the tools listed below. | 🟢  |
| [ruff](https://github.com/astral-sh/ruff)                | A very fast linter which incorporates a range of other linters.                                                                                                   | 🟢  |
| [toml-sort](https://toml-sort.readthedocs.io/en/latest/) | Sorts TOML files which are now part of PEP 8.                                                                                                                     | 🟢  |
| [black](https://black.readthedocs.io/en/stable/)         | Opinionated formatter, defaults to 88 characters per line.                                                                                                        | 🟠  |
| [autopep8](https://github.com/hhatto/autopep8)           | Formatter which conforms to PEP 8.                                                                                                                                | 🟠  |
| [pycodestyle](https://pycodestyle.pycqa.org/en/latest/)  | Linter which checks for errors.                                                                                                                                   | 🟠  |
| [pyflakes](https://github.com/PyCQA/pyflakes)            | Linter which checks for errors.                                                                                                                                   | 🟠  |
| [pylint](https://pylint.readthedocs.io/en/latest/)       | Linter which checks for errors.                                                                                                                                   | 🟠  |
| [sourcery](https://sourcery.ai/)                         | An AI code reviewer which simplifies code, has a free version but can pay for fancier features.                                                                   | 🟠  |
| [yapf](https://github.com/google/yapf)                   | Google formatter.                                                                                                                                                 | 🟠  |
| [flake8](https://flake8.pycqa.org/en/latest/)            | Linter which complains if code doesn't follow a rule. Does not support modern `pyproject.toml` configuration.                                                     | 🔴  |

<details>
<summary> 🟢 explanation</summary>

We recommend a suite of 🟢 tools that we've used and work well together.

- Pre-commit is a useful framework tool to list several linters and run it automatically. It can be used to run all of our recommended linters.

- `black` is a nice _"no need to think"_ code formatter. If you have your own opinions about code style you might not like this. But it's widely used by almost all ARC python projects.

</details>

<details>
<summary> 🔴 explanation</summary>

Flake8 is not recommended because it doesn't support `pyproject.toml` and [seemingly won't](https://github.com/PyCQA/flake8/issues/234#issuecomment-1206730688). There are now better and more flexible tools available.

</details>

## Type checking

| Name                                           | Short description                                                             | 🚦  |
| ---------------------------------------------- | ----------------------------------------------------------------------------- | --- |
| [mypy](https://mypy.readthedocs.io/en/stable/) | Static type checker, won't fail if no typing but will if typing is incorrect. | 🟢  |
