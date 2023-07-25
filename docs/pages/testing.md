---
title: Testing
layout: default
---

# Testing

## Test runners

| Name                                                                          | Short description                                                              | 🚦  |
| ----------------------------------------------------------------------------- | ------------------------------------------------------------------------------ | :-: |
| [pytest](https://docs.pytest.org/en/stable/contents.html)                     | A framework for writing and running tests.                                     | 🟢  |
| [tox](https://tox.wiki/en/latest/index.html)                                  | A framework that allows running tests and packaging in different environments. | 🟢  |
| [unittest](https://docs.python.org/dev/library/unittest.html#module-unittest) | A framework built in to Python for writing and running tests.                  | 🟠  |

<details>
<summary>🟢 explanation</summary>
We recommend `pytest` over `unittest` because `pytest` tends to encourage a cleaner style, there are also extensive plugins and it's in widespread use.
</details>

## pytest plugins

| Name                                                                   | Short description                                                         | 🚦  |
| ---------------------------------------------------------------------- | ------------------------------------------------------------------------- | :-: |
| [pytest-cov](https://pytest-cov.readthedocs.io/en/latest/index.html)   | A framework to generate coverage reports that plays nicely with `pytest`. | 🟢  |
| [pytest-mock](https://pytest-mock.readthedocs.io/en/latest/index.html) | A framework to mock/patch objects that plays nicely with `pytest`.        | 🟢  |
