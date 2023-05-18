# ARC Python Package Template

⚠️ This repository is still under construction! ⚠️

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

This is a Python package template for new ARC Python packages.
It automatically creates new Python packages with the recommended tooling set up and ready to go.
The recommended tooling is documented on the [UCL-ARC/python-tooling website](http://github-pages.arc.ucl.ac.uk/python-tooling/).

If you're making a package within a community that has an existing package template (e.g., [`scikit-hep`](https://github.com/scikit-hep/cookie)), we recommend using their template instead of this one.

## Using the template

1. Install [cookieninja](https://libraries.io/pypi/cookieninja)
   ```
   pip install cookieninja
   ```
2. Run cookieninja in the desired directory
   ```
   cookieninja gh:ucl-arc/python-template
   ```
   If you have this repo locally (this may be the case if you are developing), you can alternatively run the following:
   ```
   cookieninja /path/to/your/checkout/of/python-template
   ```
3. A series of questions will pop up to configure the project. Type the answer or hit return to use the default option (shown in square brackets).

   ```
   full_name [UCL ARC]:
   email [temp@gmail.com]:
   github_username [UCL-ARC]:
   project_name [Python Template]:
   project_slug [python-template-cookiecutter]:
   project_short_description [A cookieninja template with ARC recommendations.]:
   version [0.1.0]:
   Select min_python_version:
   Choose from 1, 2, 3, 4 [1]: 3.10
   Select max_python_version:
   Choose from 1, 2, 3, 4 [1]: 1
   ...
   ```

   Note that these project variables are defined in the `cookiecutter.json` file.

4. This will create a specific directory structure.

   For example, for a project with the following variables:

   ```
   project_slug [python-template-cookiecutter]: PROJECT_SLUG
   project_name [Python Template]: PROJECT_NAME
   ```

   we will get a project folder named after `project_slug`, structured like this:

   ```
   PROJECT_SLUG
   ├── README.md
   ├── pyproject.toml
   ├── src
   │   └── PROJECT_SLUG
   │       └── PROJECT_SLUG.py
   └── tests
       ├── conftest.py
       └── test_dummy.py
   ```

   And the `project_name` will appear in the README.md as the human-readable name of the project.

   ```
   cat PROJECT_SLUG/README.md
   # PROJECT_NAME
   ...
   ```

5. To work on your project, initialise a git repository and _install_ it in editable mode.
   (If you want to develop in a `venv` or `conda` environment, now is a good time to set that up)
   ```
   cd PROJECT_SLUG
   git init
   # conda create -n PROJECT_SLUG-dev python=3.11
   # conda activate PROJECT_SLUG-dev
   python -m pip install -e .
   ```

## Notes for developers

- To run cookieninja using a specific branch of the template:
  ```
  cookieninja https://github.com/UCL-ARC/python-template --checkout <branch-name>
  ```
