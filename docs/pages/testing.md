---
title: Testing
layout: default
---

# Testing

## Test runners

| Name                                                                          | Short description                                                                                                                                                                                  | 🚦  |
| ----------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-: |
| [pytest](https://docs.pytest.org/en/stable/contents.html)                     | A framework for writing and running tests. We recommend `pytest` over `unittest` because `pytest` tends to encourage a cleaner style, there are also extensive plugins and it's in widespread use. | 🟢  |
| [tox](https://tox.wiki/en/latest/index.html)                                  | A framework that allows running tests and packaging in different environments.                                                                                                                     | 🟢  |
| [unittest](https://docs.python.org/dev/library/unittest.html#module-unittest) | Python's built in framework for writing and running tests. Encourages use of classes as test fixtures.                                                                                             | 🟠  |

## pytest plugins

| Name                                                                   | Short description                                                                                                                                                                                                                                        | 🚦  |
| ---------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-: |
| [pytest-cov](https://pytest-cov.readthedocs.io/en/latest/index.html)   | A framework to generate coverage reports that plays nicely with `pytest`.                                                                                                                                                                                | 🟢  |
| [pytest-mock](https://pytest-mock.readthedocs.io/en/latest/index.html) | A framework to mock/patch objects that plays nicely with `pytest`.                                                                                                                                                                                       | 🟢  |
| [pyfakefs](https://pytest-pyfakefs.readthedocs.io/en/latest/)          | A plugin to create a full fake file system, for situations where you need something more complicated than the built in [`tmp_path` fixture](https://docs.pytest.org/en/stable/how-to/tmp_path.html#how-to-use-temporary-directories-and-files-in-tests). | 🟢  |
