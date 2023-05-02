# {{ cookiecutter.project_name }}

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Actions Status][actions-badge]][actions-link]
[![Documentation Status][rtd-badge]][rtd-link]

[![PyPI version][pypi-version]][pypi-link]
[![Conda-Forge][conda-badge]][conda-link]
[![PyPI platforms][pypi-platforms]][pypi-link]

[![GitHub Discussion][github-discussions-badge]][github-discussions-link]
[![Gitter][gitter-badge]][gitter-link]

<!-- prettier-ignore-start -->
[actions-badge]:            https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/workflows/CI/badge.svg
[actions-link]:             https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/actions
[conda-badge]:              https://img.shields.io/conda/vn/conda-forge/{{cookiecutter.project_slug}}
[conda-link]:               https://github.com/conda-forge/{{cookiecutter.project_slug}}-feedstock
[github-discussions-badge]: https://img.shields.io/static/v1?label=Discussions&message=Ask&color=blue&logo=github
[github-discussions-link]:  https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/discussions
[gitter-badge]:             https://badges.gitter.im/{{cookiecutter.project_slug}}/community.svg
[gitter-link]:              https://gitter.im/{{cookiecutter.project_slug}}/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge
[pypi-link]:                https://pypi.org/project/{{cookiecutter.project_slug}}/
[pypi-platforms]:           https://img.shields.io/pypi/pyversions/{{cookiecutter.project_slug}}
[pypi-version]:             https://img.shields.io/pypi/v/{{cookiecutter.project_slug}}
[rtd-badge]:                https://readthedocs.org/projects/{{cookiecutter.project_name}}/badge/?version=latest
[rtd-link]:                 https://{{cookiecutter.project_slug}}.readthedocs.io/en/latest/?badge=latest

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

## License

Distributed under the terms of the `{{cookiecutter.license}}`\_ license.

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
