# Tutorial: creating a package using template

In this tutorial we will go through in detail the steps required to set-up a Python package using the `UCL-ARC/python-tooling` 🍪 cookiecutter template as well as some follow on steps illustrating how to use the newly created package with some of the included tools.

> [!TIP]
> Some of the commands and URLs in the instructions contain placeholders within curly braces such as `{project_slug}`. You will need to replace these placeholders (including the curly braces) with the relevant values for your particular package / project - the text should give details of what should be subsituted for each placeholder.

## ⚙️ Setting up dependencies for using template

<details><summary>Click to expand... </summary> <!-- markdownlint-disable-line MD033 -->

To use the template you will need to install the following software tools

- [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- [the GitHub command line interface (CLI)](https://github.com/cli/cli?tab=readme-ov-file#installation)

The instructions for installing these tools can be accessed by clicking the individual links above.

Additionally, [cookiecutter](https://cookiecutter.readthedocs.io) will be required to generate your package from the template, which can be installed using the instructions below. For the follow on exercises you will also need an [account set up on GitHub](https://github.com/join) if you don't already have one.

An easy way to install and manage Python packages is using `uv`, which can create a dedicated environment with the necessary packages installed using the step by step instructions below

1. Open a terminal window
   - On Windows: open the Start menu from the taskbar, type `cmd` in the search field, then click [command prompt](https://en.wikipedia.org/wiki/Command-line_interface#Command_prompt) from the results.
   - On MacOS: click the Launchpad icon in the Dock, type `Terminal` in the search field, then click `Terminal` from the results.
   - On Linux: open the default terminal application installed in your distribution.

2. In the terminal window, type

   ```sh
   uv tool install cookiecutter
   ```

   to install the "tools" necessary for creating and using a package using the `UCL-ARC/python-tooling` cookiecutter template.

3. To check that all the dependencies have installed correctly, run each of the following commands in turn, one at a time

   ```sh
   cookiecutter --version
   gh --version
   git --version
   ```

   For each command you should see some text outputted to the terminal giving details of the installed versions of the applications - the output itself is not important as long as you do not see any error messages.

4. If you also want to try out creating a GitHub repository for the package you will need to [sign-up for a free GitHub account](https://github.com/join) if you don't already have one. Once you have a GitHub account, open a terminal window - you can either use the same one as previously if you still have it open, or open a new terminal window as described in step 2 and then run

   ```sh
   gh auth login
   ```

   to authenticate the GitHub command line interface tool `gh` with your GitHub account credentials. The tool will ask you a series of question, for most of which you can select the default options by just hitting the `Enter` key. Specifically select:
   - `GitHub.com` for account to log into,
   - `HTTPS` for preferred protocol,
   - `Y` to authenticate Git with your GitHub credentials,
   - `Login with a web browser` as the method to authenticate.

   Once you have selected all these options, a one-time code will be printed to the terminal. You need to copy this code and then hit the `Enter` key to open a page to complete the authentication in your default browser. Once you have entered and submitted the code in the authenticatication page, you should see a `Authentication complete` message appear in the terminal window.

</details>

## 🍪 Creating a package using the template

We will first go through the steps for creating a new package using the `UCL-ARC/python-tooling` cookiecutter template.

1. Open a new terminal/command prompt window and change the working directory to the path you wish to create the package in using the `cd` (change directory) command

   ```sh
   cd path/to/directory
   ```

2. To begin creating the package run

   ```sh
   cookiecutter gh:ucl-arc/python-tooling --checkout latest
   ```

   You will then be shown a series of prompts at the command line asking for details of the project and package. You can choose to use the default placeholder value (shown in parenthesis `()` in prompt) for any question by hitting `Enter`. If you already have a specific project in mind you want to set up a package for using the template you can use this project's details, otherwise you can just use the placeholder values. You should choose `Y` (yes) to the questions on whether to initialise Git repository and automatically deploy HTML documentation to GitHub Pages to allow you to complete the follow on exercises which rely on these options being enabled. For the prompt asking for the GitHub user or organization name to be owner of repository you should supply your GitHub user name.

3. Once you have completed all the cookiecutter prompts some additional instructions will be printed to screen (which we will come back to in the next sections) and your new package will be generated in a directory named `{project_slug}` in the current working directory (where `{project_slug}` is the value entered for the `'Slugified' project name...`[^slug] prompt, this will be `python-template` if you used the default placeholder values). You can see the directory tree of files generated by running

   ```sh
   tree {project_slug}
   ```

   or on Windows

   ```sh
   tree /F {project_slug}
   ```

   in both cases replacing `{project_slug}` with the relevant value you used (`python-template` if you used the default values).
   Some of the key files and directories are
   - The `README.md` file which is a Markdown file describing the project and acting as a landing page for first-time users.
   - The `LICENSE.md` file which contains the terms of the open-source license the code is released under.
   - The `src` directory which will contain the Python package source code.
   - The `docs` directory which will contain the Markdown files used to generate the documentation pages for the package.
   - The `tests` directory which will contain the Python modules defining tests to check for the correctness of the package code.

   Try viewing the content of some of the files generated by running

   ```sh
   cat {path_to_file}
   ```

   on macOS/Linux or

   ```sh
   type {path_to_file}
   ```

   on Windows, replacing `{path_to_file}` with the relevant path.

[^slug]: A ['slug'](https://en.wikipedia.org/wiki/Clean_URL#Slug) in this context is a human readable identifier with words typically separated by hyphens that can be used as part of a URL.

## 📦 Creating a repository on GitHub for the new package

The package you created in the previous section will have been initialised locally as a Git repository (providing you answered 'Y' to the relevant prompt!) to allow keeping the package under version control, but some extra steps are required to have the local repository synchronised to a remote repository on [GitHub](https://github.com/). The advantages of doing this are that makes it easy for other people to both download and use the package but also contribute to your project. The package has also been set up to take advantage of GitHub's continuous integration and deployment service [GitHub Actions](https://docs.github.com/en/actions) (which is free to use for public repositories) with workflows included for automatically running the package tests, performing [linting checks](<https://en.wikipedia.org/wiki/Lint_(software)>) and building the project documentation, on every [pull-request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests) and on updates to the default `main` [branch](https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell) for the repository.

When you completed setting up the package using the `cookiecutter` command you should have seen some additional instructions printed to screen including, providing you have the [GitHub CLI](https://cli.github.com/) `gh` installed, a message of the form

```sh
GitHub CLI detected, you can create a repo with the following:

gh repo create {github_owner}/{project_slug} -d "{project_description}" --public -r origin --source {project_slug}
```

where `{github_owner}`, `{project_slug}` and `{project_description}` are replaced with the relevant GitHub repository owner (user name), project slug and description that you entered when setting up the package using `cookiecutter`. You should now copy-paste and run the `gh repo create ...` command that was printed out in the message - if you no longer have access to the message you can use the example above, being careful to subsitute the placeholders in braces `{}` with the relevant values.

If you get an error message at this point it may be because you have not installed the GitHub CLI or set up the authorisation for the GitHub CLI as [described in the setup instructions above](#%EF%B8%8F-setting-up-dependencies-for-using-template).

If the command runs successfully you should see a message of the form

```sh
✓ Created repository {github_owner}/{project_slug} on GitHub
  https://github.com/{github_owner}/{project_slug}
✓ Added remote https://github.com/{github_owner}/{project_slug}.git
```

A repository should have been created at the printed URL which you should be able to navigate to in your browser (either copy-paste in to browser or depending on terminal application you may be able to hold `Ctrl` and click on URL directly). Currently both the remote and local repositories are empty as we have not made any commits.

To commit the package files generated by `cookiecutter` locally on the default `main` branch and also push this commit to the repository on GitHub, run each of the commands below in turn, replacing the `{project_slug}` placeholder with the relevant value you used when creating package (`python-template` if you used default)

```sh
cd {project_slug}
git add .
git commit -m "Initial commit"
git push --set-upstream origin main
```

If you now navigate to the GitHub repository URL in your browser you should see the package files present, with the content of the top-level `README.md` being displayed as the repository landing page.

The push of the initial commit to the default `main` branch will have also triggered runs of the GitHub Actions workflows set up in the repository. You can view the status of the workflow job runs by opening the `Actions` pane from the top navigation bar on the repository landing page, or going to the URL `https://github.com/{github_owner}/{project_slug}/actions`.

Depending on your account settings, you may find that the `Documentation` workflow shows as failed (❌). If this is the case this is likely because the repository has been set by default to only allow GitHub Actions workflows read permissions on the repository, which prevents the step in the `Documentation` workflow which pushes the built HTML documentation to a branch `gh-pages` from completing. In the next section we will look at how to configure the repository to ensure the permissions are set correctly and have the HTML documentation deployed to a GitHub Pages website.

## 📄 Configuring repository to host docs on GitHub Pages

Now that the repository is synchronised to GitHub, a few additional steps are required to configure the repository for the HTML documentation to be automatically deployed to [GitHub Pages](https://pages.github.com/). On completion of the `cookiecutter` command to create the package, a message of the form below should have been displayed

```sh
The 'Documentation' GitHub Actions workflow has been set up to push the built
HTML documentation to a branch gh-pages on pushes to main for deploying as a
GitHub Pages website. To allow the GitHub Actions bot to push to the gh-pages
branch you need to enable 'Read and write permissions' under 'Workflow
permissions' at

https://github.com/{github_owner}/{project_slug}/settings/actions

After the 'Documentation' workflow has successfully completed at least once
you will also need to configure the repository to deploy a GitHub pages site
from the content on the gh-pages branch by going to

https://github.com/{github_owner}/{project_slug}/settings/pages

and under 'Built and deployment' selecting 'Deploy from a branch' for the
'Source' drop-down and 'gh-pages' for the 'Branch' drop-down, leaving the
branch path drop-down with its default value of '/ (root)'.
```

where as before `{github_owner}` and `{project_slug}` are replaced with the relevant GitHub repository owner and project slug that you entered when setting up the package.

The first part of the instructions gives details of how to set the permissions for GitHub Actions workflows in the repository to allow the GitHub Actions bot to push the built HTML documentation to a branch `gh-pages` on updates to the default `main` branch on the repository, so that the documentation is automatically updated whenever changes are merged in to `main`. After going to the Actions settings page at the URL indicated (which can also be reached by going to the `Settings` tab in the top navigation bar of the repository and then selecting `Action > General` in the left hand navigation menu) and ensuring `Workflow permissions` is set to allow `Read and write permissions`, if you have changed the permissions you will also need to re-run the documentation workflow with the updated permissions. This can be done by going to the Actions pane in the repository (accessible from top navigation bar or by going to `https://github.com/{github_owner}/{project_slug}/actions`), clicking on the (top / latest if there are multiple) entry for the _Documentation_ workflow, which should be showing as failing, and then from the resulting page click the `Re-run all jobs` button.

Once the _Documentation_ workflow has successfully completed, a new branch `gh-pages` should have been created in the repository containing the HTML documentation. The second part of the instructions printed in the message output by the `cookiecutter` command indicate to go to a URL `https://github.com/{github_owner}/{project_slug}/settings/pages` to set this branch as the source for a GitHub Pages website for the repository. If you now follow those instructions, setting the `Source` to `Deploy from branch` and `Branch` to `gh-pages`, the a new Actions workflow `pages-build-deployment` will be automatically triggered. Once this workflow has completed, you should be able to view the HTML documentation for the repository at a URL

```sh
https://{github_owner}.github.io/{project_slug}
```

The index page of the documentation reproduces the content from the repository README file. The documentation site also importantly includes _application programming interface_ (API) reference documentation built from the [docstrings](https://peps.python.org/pep-0257/#what-is-a-docstring) in the package source code; this API documentation is accessible from the `API reference` link in the navigation.

## 🐍 Setting up a virtual environment for project

It is recommended to set up a project-specific [virtual environment](https://docs.python.org/3/tutorial/venv.html) whenever working on Python project. This allows you to install the versions of third-party packages the project requires without conflicting with the requirements of other projects you are developing.

There are a variety of virtual environment management tools available for Python. One option is [uv](https://docs.astral.sh/uv), which you will have installed if you followed our detailed set-up instructions above, or may already have installed previously. `uv` is an extremely fast Python package and virtual environment manager that has API compatiblility with `pip` and the built-in virtual environment manager - [`venv`](https://docs.python.org/3/library/venv.html).

Once you are in your `{project_slug}` directory, a virtual environment can be created by running the following in a terminal/command prompt window

```sh
uv venv .venv
```

This will create a new environment with name `.venv`, which can be activated for installing packages using

```sh
source .venv/bin/activate
```

or if on Windows

```sh
.venv\Scripts\activate
```

You should see `(.venv)` on the left of your terminal window. Once you have activated the environment you can use the following command to install any packages within the `.venv` environment

```sh
uv pip install numpy
```

The environment can be deactivated using

```sh
deactivate
```

You can even use an arbitrary Python version to create `uv` environments, and `uv` will fetch that Python version if it is not available locally

```sh
uv venv --python 3.11.6
```

Once you have created and activated a virtual environment for the project, you can install the package in [editable mode](https://setuptools.pypa.io/en/latest/userguide/development_mode.html), along with both its required dependencies and optional sets of dependencies for development (`dev`), documentation (`docs`) and testing (`test`) by running

```sh
uv pip install --editable ".[dev,docs,test]"
```

from the root of the project repository.

<details><summary>Using venv as an alternative to uv </summary> <!-- markdownlint-disable-line MD033 -->

Alternatively, you can use the [`venv` module](https://docs.python.org/3/library/venv.html), which is slower and has fewer features, when compared to `uv`, but is built-in to the Python standard library. `venv` has the advantage of being available in any Python (3.3+) environment, but unlike `uv` will not by itself allow you to use a different Python version from the system level install. A common pattern is to store the virtual environment files in a directory `.venv` within the root directory of the project repository. This can be achieved by running

```sh
python -m venv .venv
```

from the root of the project repository. To activate the new virtual environment, if on Linux or MacOS run from the root of the project repository

```sh
source .venv/bin/activate
```

or if on Windows

```sh
.venv\Scripts\activate
```

Once you have activated the environment you should make sure the version of the Python package manager `pip` installed in the environment is up to date by running

```sh
python -m pip install --upgrade pip
```

Similar to `uv`, once the environment is active, you can install the package in editable mode, along with both its required dependencies and optional sets of dependencies by running

```sh
python -m pip install --editable ".[dev,docs,test]"
```

</details>

## 🧪 Running package tests locally

The package template includes support for running tests using the [`pytest` testing framework](https://docs.pytest.org/). Tests are defined in modules in the `tests` directory. By default a single test module `tests/test_dummy.py` is created with a placeholder test. You can run the test locally using `pytest` directly (you will need to have the virtual environment active in which you installed the package and its dependencies) by running

```sh
pytest
```

from the root of the project repository.

The package template also sets up [`tox`](https://tox.wiki), an automation tool which allows easily running tests in isolated environments and under multiple Python versions. You can run the tests across all compatible Python versions currently installed using `tox` by running

```sh
tox
```

from the root of the project repository.

## 📖 Building documentation locally

It can sometimes be useful when editing docstrings or adding additional pages in the `docs` directory to be able to render the HTML documentation locally. The package is set up to use [MkDocs](https://www.mkdocs.org/) to build the documentation with the package API documentation generated using the [`mkdocstrings` plug-in](https://mkdocstrings.github.io/). These packages will have been installed in to you local development environment providing you installed the package with optional `docs` dependencies as recommended above. To build and serve the documentation locally run

```sh
mkdocs serve
```

from the root of the project repository and navigate to `http://127.0.0.1:8000/` in your browser. The development server used here supports auto-reloading, meaning the content will be automatically refreshed in your browser if you make any edits to source.

A `tox` environment `docs` to build the documentation is also available. This will be build the documentation in an isolated environment and is also used for building the documentation in the GitHub Actions _Documentation_ workflow so can be useful to run locally when debugging issues with the workflow - it can be executed by running

```sh
tox -e docs
```

from the root of the project repository. The built documentation will be output to a directory `site`.

## ✅ Using `pre-commit` to run checks when committing

The package is set-up to use [pre-commit](https://pre-commit.com/), a framework for running [Git hook scripts](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks) on each commit to the repository. In particular the a `.pre-commit-config.yaml` configuration file is provided which will run a series of linters, checks and formatters on the repository such as [ruff](https://docs.astral.sh/ruff/), [mypy](https://mypy.readthedocs.io/en/stable/) and [prettier](https://prettier.io/) on every commit. These Git hook scripts can installed locally by running

```sh
pre-commit install
```

from the root of the project repository. Once installed the hook scripts will be called to inspect the changes each time `git commit` is run, with any failures of the checks needing to be resolved before the changes can be commited. Some of the `pre-commit` hooks include support for auto-fixing some problems - in this case you will be alerted that a file has been changed by a hook and these changes need to be staged using `git add` before recommitting.

The `pre-commit` hooks can be run against all files in the repository by running

```sh
pre-commit run --all-files
```

from the root of the project repository. As the hooks are typically only run on the files changed in a commit, this can be useful to check the hooks will pass on all files when the `pre-commit` configuration is updated by, for example, [adding a new plug-in](https://pre-commit.com/#plugins).
