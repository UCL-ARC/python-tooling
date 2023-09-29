# UCL ARC Python Recommendations

This is repository collects the [UCL ARC] recommendations for a Research Software project in Python.
It contains a template for new Python packages and a [website] documenting our recommendations.
We've turned on [discussions](https://github.com/UCL-ARC/python-tooling/discussions) for this repo, and we welcome questions there or in the `#programming-help` channel on the [UCL research software hub slack](https://www.ucl.ac.uk/advanced-research-computing/community/ucl-research-programming-hub).

🍪🥷 Our template is a [cookieninja] template which automatically creates new Python packages with our recommended tooling set up and ready to go.

> **Note**
> If you're making a package within a community that has an existing package template (e.g., [`scikit-hep`](https://github.com/scikit-hep/cookie)), we recommend using their template instead of this one.

<!-- links here -->

<!-- prettier-ignore-start -->
[website]: https://github-pages.arc.ucl.ac.uk/python-tooling
[UCL ARC]: https://ucl.ac.uk/arc
[cookieninja]: https://libraries.io/pypi/cookieninja
<!-- prettier-ignore-end -->

## Using this template

1.  Install [cookieninja](https://libraries.io/pypi/cookieninja) in a `conda`, `mamba` or `venv` environment (commented lines for conda example).

```
# conda create --channel conda-forge --name new-env-name 
# conda activate new-env-name
# conda install pip
pip install cookieninja
```

2. Run cookieninja in the desired directory
   ```
   cookieninja gh:ucl-arc/python-tooling
   ```
   If you have this repo locally (this may be the case if you are developing), you can run the following:
   ```
   cookieninja /path/to/your/checkout/of/python-tooling
   ```
3. A series of questions will pop up to configure the project. Type the answer or hit return to use the default option (shown in square brackets).

   ```
   full_name [UCL ARC]:
   email [temp@gmail.com]:
   github_username [UCL-ARC]:
   project_name [Python Template]:
   project_slug [python-tooling-cookiecutter]:
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
   project_slug [python-tooling-cookiecutter]: PROJECT_SLUG
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
   ```
   cd PROJECT_SLUG
   git init
   python -m pip install -e ".[dev]"
   ```
6. Build your package
   ```
   python -m build
   ```

## Notes for developers

### Contributing

The [website] and source pages are open to contributions but must be reviewed by a member or associate member of ARC.
We might be slow to approve new tool suggestions (since we'll probably want to discuss them first), but bug reports (and fixes) are very welcome from anyone!

Pages all live in the [docs/pages](https://github.com/UCL-ARC/python-tooling/tree/main/docs/pages) sub-directory, and are written in markdown.

To contribute:

1. Create a new branch (or fork if you're not in ARC-collaborations).
2. Modify an existing page, create a new one, or tweak the template.
   a. Run [pre-commit](https://pre-commit.com) which will lint your changes.
   b. Check the tests pass if you modified the template (`pytest -s`).
3. Open a pull request with changes.
4. Someone who did not contribute to the PR should review it.
5. If approved, the reviewer should merge the PR.
6. If changes requested, the PR author should address the comments, then ask for review again.

### Development

- Clone repository

  - (Optional) Generate your SSH keys as suggested [here](https://docs.github.com/en/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)
  - (Optional) GitHub CLI as suggested [here](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account?tool=cli)
  - Clone the repository by typing (or copying) the following line in a terminal at your selected path in your machine:

  ```
  git clone git@github.com:UCL-ARC/python-tooling.git
  cd python-tooling
  ```

- To create and remove your virtual environment

  ```
  conda create -n ptoolingVE pip -c conda-forge
  conda activate ptoolingVE
  conda deactivate ptoolingVE
  conda remove -n ptoolingVE --all
  ```

- To run template in the same path of this repo.
  We do a test cookiecut of a dummy package and install it to ensure the template setup works.

  ```
  cookieninja .
  cd python-template
  git init
  python -m pip install -e ".[dev]"
  ```

- To run cookieninja using a specific branch of the template:

  ```
  cookieninja https://github.com/UCL-ARC/python-tooling --checkout <branch-name>
  ```

- To run the tests locally:

  ```
  pytest -s
  ```

- To commit changes

  ```
  pre-commit run -a
  git add .
  git commmit -m 'message issue number (#NN)'
  git push origin NN-future-branch
  ```

- To build the docs locally

  1.  [Install jekyll](https://jekyllrb.com/docs/installation)
  2.  Run `bundle install` from the root of this repository to install dependencies
  3.  Run `bundle exec jekyll serve` from the root directory of this repository. This should fire up a local web server and tell you its address. By default the server will automatically refresh the HTML pages if any changes are made to the markdown sources.

  See the [jekyll docs](https://jekyllrb.com/docs) for more info.
