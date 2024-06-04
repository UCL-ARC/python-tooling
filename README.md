<div style="text-align: center;" align="center">
  <img src="https://raw.githubusercontent.com/UCL-ARC/python-tooling/main/images/logo.svg" alt="UCL ARC Python tooling logo" width="120"/>
  <h1> UCL ARC Python Recommendations</h1>
</div>

This repository collects the [UCL ARC] recommendations for a research software
project in Python. It contains a template for new Python packages and a
[website] documenting our recommendations. We've turned on
[discussions](https://github.com/UCL-ARC/python-tooling/discussions) for this
repo, and we welcome questions there or in the `#helpme` channel on the
[UCL research programming hub Slack](https://www.ucl.ac.uk/advanced-research-computing/community/ucl-research-programming-hub).

🍪 Our template is a [cookiecutter] template which automatically creates new
Python packages with our recommended tooling set up and ready to go.

> **Note** If you're making a package within a community that has an existing
> package template (e.g., [`scikit-hep`](https://github.com/scikit-hep/cookie)),
> we recommend using their template instead of this one.

<!-- links here -->

<!-- prettier-ignore-start -->
[website]: https://github-pages.arc.ucl.ac.uk/python-tooling
[UCL ARC]: https://ucl.ac.uk/arc
[cookiecutter]: https://libraries.io/pypi/cookiecutter
<!-- prettier-ignore-end -->

## Contributors

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://www.davidstansby.com"><img src="https://avatars.githubusercontent.com/u/6197628?v=4?s=100" width="100px;" alt="David Stansby"/><br /><sub><b>David Stansby</b></sub></a><br /><a href="#ideas-dstansby" title="Ideas, Planning, & Feedback">🤔</a> <a href="#bug-dstansby" title="Bug reports">🐛</a> <a href="#code-dstansby" title="Code">💻</a> <a href="#content-dstansby" title="Content">🖋</a> <a href="#doc-dstansby" title="Documentation">📖</a> <a href="#eventOrganizing-dstansby" title="Event Organizing">📋</a> <a href="#projectManagement-dstansby" title="Project Management">📆</a> <a href="#review-dstansby" title="Reviewed Pull Requests">👀</a> <a href="#test-dstansby" title="Tests">⚠️</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

## Using this template

1.  Install [cookiecutter] in a Conda or `venv` environment (commented lines for
    Conda example).

    ```
    # conda create --channel conda-forge --name new-env-name
    # conda activate new-env-name
    # conda install pip
    pip install cookiecutter
    ```

2.  Run cookiecutter in the desired directory
    ```
    cookiecutter gh:ucl-arc/python-tooling
    ```
    If you have this repo locally (this may be the case if you are developing),
    you can run the following:
    ```
    cookiecutter /path/to/your/checkout/of/python-tooling
    ```
3.  A series of questions will pop up to configure the project. Type the answer
    or hit return to use the default option (shown in square brackets).

    Note that these project variables are defined in the `cookiecutter.json`
    file.

4.  This will create a specific directory structure.

    For example, for a project with the following variables:

    ```
    project_name [Python Template]: PROJECT_NAME
    project_slug [python-template]: PROJECT_SLUG
    ```

    we will get a project folder named `PROJECT_SLUG`, structured like this:

    ```
    PROJECT_SLUG
    ├── ...
    ├── README.md
    ├── pyproject.toml
    ├── src
    │   └── PROJECT_SLUG
    │       └── PROJECT_SLUG.py
    └── tests
        └── test_dummy.py
    ```

    And the `PROJECT_NAME` will appear in the README.md as the human-readable
    name of the project.

    ```
    cat PROJECT_SLUG/README.md
    # PROJECT_NAME
    ...
    ```

5.  To work on your project, initialise a git repository and _install_ it in
    editable mode.
    ```
    cd PROJECT_SLUG
    git init
    python -m pip install -e ".[dev]"
    ```
6.  Build your package
    ```
    python -m build
    ```

## Notes for developers

<details>
<summary>Click to expand...</summary>

First, clone repository

- (Optional) Generate your SSH keys as suggested
  [here](https://docs.github.com/en/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)
- (Optional) GitHub CLI as suggested
  [here](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account?tool=cli)
- Clone the repository by typing (or copying) the following line in a terminal
  at your selected path in your machine:

```
git clone git@github.com:UCL-ARC/python-tooling.git
cd python-tooling
```

### Developing the cookiecutter template

- To create and remove your virtual environment

  ```
  conda create -n ptoolingVE pip -c conda-forge
  conda activate ptoolingVE
  conda deactivate ptoolingVE
  conda remove -n ptoolingVE --all
  ```

- To run template in the same path of this repo. We do a test cookiecut of a
  dummy package and install it to ensure the template setup works.

  ```
  cookiecutter .
  cd python-template
  git init
  python -m pip install -e ".[dev]"
  ```

- To run cookiecutter using a specific branch of the template:

  ```
  cookiecutter https://github.com/UCL-ARC/python-tooling --checkout <branch-name>
  ```

- To run the tests locally:

  ```
  pytest -s
  ```

### Developing the recommended tooling pages

Pages all live in the
[docs/pages](https://github.com/UCL-ARC/python-tooling/tree/main/docs/pages)
sub-directory, and are written in markdown.

To build the webpage locally (for testing)

1.  [Install jekyll](https://jekyllrb.com/docs/installation)
2.  Run `bundle install` from the `docs/` directory of this repository to
    install dependencies.
3.  Run `bundle exec jekyll serve` from the root directory of this repository.
    This should fire up a local web server and tell you its address. By default
    the server will automatically refresh the HTML pages if any changes are made
    to the markdown sources.

See the [jekyll docs](https://jekyllrb.com/docs) for more info.

</details>
