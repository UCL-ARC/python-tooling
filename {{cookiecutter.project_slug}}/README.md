# {{ cookiecutter.project_name }}

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Actions Status][actions-badge]][actions-link]
[![Licence][licence-badge]](./LICENCE.md)

<!--
[![PyPI version][pypi-version]][pypi-link]
[![Conda-Forge][conda-badge]][conda-link]
[![PyPI platforms][pypi-platforms]][pypi-link]
-->

<!-- prettier-ignore-start -->
[actions-badge]:            https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/workflows/CI/badge.svg
[actions-link]:             https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/actions
[conda-badge]:              https://img.shields.io/conda/vn/conda-forge/{{cookiecutter.project_slug}}
[conda-link]:               https://github.com/conda-forge/{{cookiecutter.project_slug}}-feedstock
[pypi-link]:                https://pypi.org/project/{{cookiecutter.project_slug}}/
[pypi-platforms]:           https://img.shields.io/pypi/pyversions/{{cookiecutter.project_slug}}
[pypi-version]:             https://img.shields.io/pypi/v/{{cookiecutter.project_slug}}
{%- if cookiecutter.licence == "MIT" -%}
[licence-badge]             https://img.shields.io/badge/License-MIT-yellow.svg
{%- elif cookiecutter.licence == "BSD-3" -%}
[licence-badge]             https://img.shields.io/badge/License-BSD_3--Clause-blue.svg
{%- elif cookiecutter.licence == "GPL-3.0" -%}
[licence-badge]             https://img.shields.io/badge/License-GPLv3-blue.svg
{%- endif -%}

<!-- prettier-ignore-end -->

{{cookiecutter.project_short_description}}

This project is developed in collaboration with the [Centre for Advanced Research Computing](https://ucl.ac.uk/arc), University College London.

## About

### Project Team

{{cookiecutter.full_name}} ([{{cookiecutter.email}}](mailto:{{cookiecutter.email}}))

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

Any tools or versions of languages needed to run code. For example specific Python or Node versions. Minimum hardware requirements also go here.

### Installation

How to build or install the application.

### Running Locally

How to run the application on your local system.

### Running Tests

How to run tests on your local system.

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
