---
title: Dev tools
layout: default
---

# Integrated Development Environments (IDEs)

| Name                                                     | Short description                   | 🚦  | Used by |
| -------------------------------------------------------- | ----------------------------------- | --- | :-----: |
| [Visual Studio Code](https://code.visualstudio.com/docs) | A light-weight general-purpose IDE. | 🟠  |         |
| [PyCharm](https://www.jetbrains.com/pycharm/)            | A Python IDE by JetBrains.          | 🟠  |         |

# Virtual environments

| Name                                                                  | Short description                                                                   | 🚦  | Used by |
| --------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | --- | :-----: |
| [mamba](https://mamba.readthedocs.io/en/latest/user_guide/mamba.html) | A tool to manage conda environments. Faster than conda for installing dependencies. | 🟢  |         |
| [conda](https://conda.io/projects/conda/en/latest/)                   | Conda quickly installs, runs, and updates packages and their dependencies.          | 🟠  |         |
| [pipenv](https://pipenv.pypa.io/en/latest/)                           | A tool that automatically creates and manages a virtualenv for your projects.       | 🟠  |         |
| [venv](https://docs.python.org/3/library/venv.html)                   | A tool to create isolated Python environments.                                      | 🔴  |         |
| [virtualenv](https://virtualenv.pypa.io/en/latest/)                   | A tool to create isolated Python environments which offers more features than venv. | 🟠  |         |
| [pyenv](https://github.com/pyenv/pyenv)                               | A tool that lets you easily switch between multiple versions of Python.             | 🟠  |         |

# Other

| Name                                                        | Short description                                                                                 | 🚦  |                                                                                        Used by                                                                                        |
| ----------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | --- | :-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [jedi](https://jedi.readthedocs.io/en/latest/)              | Refactoring and autocompletion used in IDEs.                                                      | 🟢  |                                                            [Conjurer](https://github.com/UCL-ARC/Conjurer/tree/main/MLDE)                                                             |
| [rope](https://rope.readthedocs.io/en/latest/overview.html) | Refactoring library.                                                                              |     |                                                                                                                                                                                       |
| [tqdm](https://pypi.org/project/tqdm/2.2.3/)                | Progress bar for loops.                                                                           | 🟢  |                                    [RRED,](https://github.com/UCL-ARC/rred-reports) [Conjurer](https://github.com/UCL-ARC/Conjurer/tree/main/MLDE)                                    |
| [psutil](https://psutil.readthedocs.io/en/latest/)          | System monitoring, profiling, limiting process resources and the management of running processes. | 🟢  | [Conjurer,](https://github.com/UCL-ARC/Conjurer/tree/main/MLDE) [Puppet Submitty,](https://github.com/UCL-ARC/puppet-submitty) [Quality Workflow tool](https://github.com/UCL-ARC/qw) |
