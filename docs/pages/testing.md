---
title: Testing
layout: default
---

## Testing

### Test runners

| Name                                                                          | Short description                                                                                                                                                                                  |                      🚦                      |
| ----------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------: |
| [pytest](https://docs.pytest.org/en/stable/contents.html)                     | A framework for writing and running tests. We recommend `pytest` over `unittest` because `pytest` tends to encourage a cleaner style, there are also extensive plugins and it's in widespread use. | <span class="label label-green">Best</span>  |
| [tox](https://tox.wiki/en/latest/index.html)                                  | A framework that allows running tests and packaging in different environments.                                                                                                                     | <span class="label label-green">Best</span>  |
| [unittest](https://docs.python.org/dev/library/unittest.html#module-unittest) | Python's built in framework for writing and running tests. Encourages use of classes as test fixtures.                                                                                             | <span class="label label-yellow">Good</span> |

### pytest plugins

| Name                                                                   | Short description                                                                                                                                                                                                                                        |                     🚦                      |
| ---------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-----------------------------------------: |
| [pytest-cov](https://pytest-cov.readthedocs.io/en/latest/index.html)   | A framework to generate coverage reports that plays nicely with `pytest`.                                                                                                                                                                                | <span class="label label-green">Best</span> |
| [pytest-mock](https://pytest-mock.readthedocs.io/en/latest/index.html) | A framework to mock/patch objects that plays nicely with `pytest`.                                                                                                                                                                                       | <span class="label label-green">Best</span> |
| [pyfakefs](https://pytest-pyfakefs.readthedocs.io/latest/)             | A plugin to create a full fake file system, for situations where you need something more complicated than the built in [`tmp_path` fixture](https://docs.pytest.org/en/stable/how-to/tmp_path.html#how-to-use-temporary-directories-and-files-in-tests). | <span class="label label-green">Best</span> |

## Property based testing

| Name                                                                      | Short description                                                        |                     🚦                      |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------ | :-----------------------------------------: |
| [Hypothesis](https://hypothesis.readthedocs.io/en/latest/quickstart.html) | Allows one to easily test multiple inputs for a given function with ease | <span class="label label-green">Best</span> |
