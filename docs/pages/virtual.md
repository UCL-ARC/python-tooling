---
title: Virtual environments
layout: default
---

## Virtual environments

| Name                    | Short description                                                                                                                                                                                                                                            | 🚦  |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :-: |
| conda-forge [miniforge] | Installs, runs, and updates packages and their dependencies. Uses `conda`, but with community maintained packages from `conda-forge` channel instead of commercially maintained packages.                                                                    | 🟢  |
| [uv]                    | Fast dependecy (and project) management tool. A drop-in replacement for `venv`. This will probably become our 🟢 tool, but for now we play cautious as there are some open bugs and features. If you're comfortable using `venv` syntax we'd recommend this. | 🟠  |
| [pipenv]                | Automatically creates and manages a virtualenv for your projects.                                                                                                                                                                                            | 🟠  |
| [pixi]                  | A fast drop-in replacement for `conda`.                                                                                                                                                                                                                      | 🟠  |
| [pyenv]                 | Lets you easily switch between multiple versions of Python.                                                                                                                                                                                                  | 🟠  |
| [virtualenv]            | Creates isolated Python environments, and offers more features than venv.                                                                                                                                                                                    | 🟠  |
| [venv]                  | Creates isolated Python environments. Fewer features than other tools, but very widely used and comes built into Python.                                                                                                                                     | 🟠  |
| [anaconda]              | Due to recent [licensing ambiguity][anaconda-problems], we recommend avoiding anaconda and many of the default channels. We recommend installing miniforge and sticking to the `conda-forge` channel.                                                        | 🔴  |

<!-- links here for a more readable table -->

[miniforge]: https://conda-forge.org/download/
[uv]: https://docs.astral.sh/uv/getting-started/installation/
[pixi]: https://pixi.sh/latest/#installation
[pipenv]: https://pipenv.pypa.io/en/latest/
[pyenv]: https://github.com/pyenv/pyenv
[virtualenv]: https://virtualenv.pypa.io/en/latest/
[anaconda]: https://www.anaconda.com/
[anaconda-problems]: https://www.theregister.com/2024/08/08/anaconda_puts_the_squeeze_on/
[venv]: https://docs.python.org/3/library/venv.html
