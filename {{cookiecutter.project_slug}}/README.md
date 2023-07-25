# {{ cookiecutter.project_name }}

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Tests status][tests-badge]][tests-link]
[![Linting status][linting-badge]][linting-link]
[![Licence][licence-badge]](./LICENCE.md)

<!--
[![PyPI version][pypi-version]][pypi-link]
[![Conda-Forge][conda-badge]][conda-link]
[![PyPI platforms][pypi-platforms]][pypi-link]
-->

<!-- prettier-ignore-start -->
[tests-badge]:              https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/actions/workflows/tests.yml/badge.svg
[tests-link]:               https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/actions/workflows/tests.yml
[linting-badge]:            https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/actions/workflows/linting.yml/badge.svg
[linting-link]:             https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/actions/workflows/linting.yml
[conda-badge]:              https://img.shields.io/conda/vn/conda-forge/{{cookiecutter.project_slug}}
[conda-link]:               https://github.com/conda-forge/{{cookiecutter.project_slug}}-feedstock
[pypi-link]:                https://pypi.org/project/{{cookiecutter.project_slug}}/
[pypi-platforms]:           https://img.shields.io/pypi/pyversions/{{cookiecutter.project_slug}}
[pypi-version]:             https://img.shields.io/pypi/v/{{cookiecutter.project_slug}}
{% if cookiecutter.licence == "MIT" -%}
[licence-badge]:            https://img.shields.io/badge/License-MIT-yellow.svg
{%- elif cookiecutter.licence == "BSD-3" -%}
[licence-badge]:            https://img.shields.io/badge/License-BSD_3--Clause-blue.svg
{%- elif cookiecutter.licence == "GPL-3.0" -%}
[licence-badge]:            https://img.shields.io/badge/License-GPLv3-blue.svg
{% endif %}
<!-- prettier-ignore-end -->

{{cookiecutter.project_short_description}}

This project is developed in collaboration with the [Centre for Advanced Research Computing](https://ucl.ac.uk/arc), University College London.

## About

### Project Team

{{cookiecutter.author_name}} ([{{cookiecutter.author_email}}](mailto:{{cookiecutter.author_email}}))

<!-- TODO: how do we have an array of collaborators ? -->

### Research Software Engineering Contact

Centre for Advanced Research Computing, University College London
([arc-collab@ucl.ac.uk](mailto:arc-collab@ucl.ac.uk))

## Built With

<!-- TODO: can cookiecutter make a list of frameworks? -->

[Framework 1](https://something.com)
[Framework 2](https://something.com)
[Framework 3](https://something.com)

## Getting Started

### Prerequisites

<!-- Any tools or versions of languages needed to run code. For example specific Python or Node versions. Minimum hardware requirements also go here. -->

`{{cookiecutter.project_slug}}` requires Python {{cookiecutter.min_python_version}}{% if cookiecutter.min_python_version != cookiecutter.max_python_version %}&ndash;{{cookiecutter.max_python_version}}{% endif %}.

### Installation

<!-- How to build or install the application. -->

To install the latest development version of `{{cookiecutter.project_slug}}` using `pip` run

```sh
pip install git+https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}.git
```

Alternatively create a local clone of the repository with

```sh
git clone https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}.git
```

and then install in editable mode by running

```sh
pip install -e .
```

### Running Locally

How to run the application on your local system.

### Running Tests

<!-- How to run tests on your local system. -->

Tests can be run across all compatible Python versions in isolated environments using
[`tox`](https://tox.wiki/en/latest/) by running

```sh
tox
```

To run tests manually in a Python environment with `pytest` installed run

```sh
pytest tests
```

again from the root of the repository.

## Roadmap

- [x] Initial Research
- [ ] Minimum viable product <-- You are Here
- [ ] Alpha Release
- [ ] Feature-Complete Release
- [x] Initial Research
- [ ] Minimum viable product <-- You are Here
- [ ] Alpha Release
- [ ] Feature-Complete Release

## Citation

Please cite [xx.yyy/zenodo.zzzz](https://doi.org/xx.yyy/zenodo.zzzzz) for this work if you use this code.

<details>
<summary>BibTEX</summary>

```bibtex
@article{xxx2023paper,
  title={Title},
  author={Author},
  journal={arXiv},
  year={2023}
}
```

</details>

## Acknowledgements

This work was funded by a grant from the {{ cookiecutter.funder }}.
