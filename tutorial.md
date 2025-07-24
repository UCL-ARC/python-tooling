# Tutorial: creating a package using our template

In this tutorial, we will go through the steps to set up a Python package using the `UCL-ARC/python-tooling` 🍪 cookiecutter template.
We'll also show you how to use your new package with some of the tools included.

> [!TIP]
> Some of the commands and URLs in this tutorial contain placeholders in curly braces like: `{project_slug}`.
> You'll need to replace these placeholders (including the curly braces) with the relevant values for your package or project.
> We'll always explain what should be substituted for each placeholder.

## ⚙️ Prerequisites for using the template

<details><summary>Click to expand… </summary> <!-- markdownlint-disable-line MD033 -->

To use the template you'll need the following software:

- A terminal;
- [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git);
- [`uv`](https://docs.astral.sh/uv/getting-started/installation/);
- and the official GitHub command line interface (CLI): [`gh`](https://github.com/cli/cli?tab=readme-ov-file#installation).

The instructions for installing these tools are at the individual links, above.

You'll also need [cookiecutter] to generate your package from the template.
If you don't have [cookiecutter], don't worry, we'll install it with `uv` in the next steps.
For the later part of the tutorial, you'll need an [account on GitHub](https://github.com/join), if you don't already have one.

[cookiecutter]: https://cookiecutter.readthedocs.io

An easy way to install and manage Python packages is using `uv`.
We'll use `uv` to install [cookiecutter] in the following steps, skip step 2 if you've already got [cookiecutter].

1. Open a terminal
   - On Windows: open the Start menu from the taskbar, type `cmd` in the search field, then click [command prompt](https://en.wikipedia.org/wiki/Command-line_interface#Command_prompt) from the results.
   - On MacOS: click the Launchpad icon in the Dock, type `terminal` in the search field, then click `Terminal` from the results.
   - On Linux: open the default terminal application installed in your distribution. You can usually do this with `<ctrl><alt>t`.

2. In the terminal, type

   ```sh
   uv tool install cookiecutter
   ```

   and press enter, to install [cookiecutter] as a [`uv` tool](https://docs.astral.sh/uv/concepts/tools/) on your computer.

3. To check that everything was installed correctly, run each of the following commands, one at a time

   ```sh
   cookiecutter --version
   gh --version
   git --version
   ```

   For each command you should see some text in the terminal giving each of the versions installed.
   The output itself isn't important, as long as you don't see any error messages.

4. If you have a GitHub account then run

   ```sh
   gh auth login
   ```

   to authenticate the GitHub CLI with your GitHub account.
   The tool will ask you some questions, for most these you can select the default options by just hitting the `Enter` key.

   Specifically, make sure you choose:
   - `GitHub.com` for account to log into,
   - `HTTPS` for preferred protocol,
   - `Y` to authenticate Git with your GitHub credentials,
   - `Login with a web browser` as the method to authenticate.

   Once you've done this, a one-time code will be printed to the terminal.
   Copy this code and then hit the `Enter` key to open a web browser and complete the authentication.
   Once you've finished in the browser window, you should see an `Authentication complete` message appear in the terminal window.

</details>

## 🍪 Creating a package using the template

We'll first go through creating a new package using the `UCL-ARC/python-tooling` template.

1. Open a new terminal and change the working directory to where you want to create the package.

   ```sh
   cd path/to/directory
   ```

2. To create the package, run

   ```sh
   cookiecutter gh:ucl-arc/python-tooling --checkout latest
   ```

   You will be shown a series of prompts asking for details of the project and package.
   You can choose to use the default value (shown in parentheses `()` in the prompt) for any question by hitting `Enter`.
   If you already have a specific project in mind, you can use this project's details; otherwise, use the placeholder values.
   You should choose `Y` (yes) to the questions on whether to initialise a Git repository and automatically deploy HTML documentation to GitHub Pages (this is used in a later section).
   When you're asked for the `GitHub user or organisation ...` type your GitHub username.

3. Once you have answered all of the questions, some additional instructions will be printed to the terminal (we will come back to these later).
   Your new package is in a directory named `{project_slug}` in the current working directory (where `{project_slug}` is the value entered for the `'Slugified' project name...`[^slug] prompt, this will be `python-template` if you used the default placeholder values). You can see the directory tree of files generated by running

   ```sh
   tree {project_slug}
   ```

   or on Windows

   ```sh
   tree /F {project_slug}
   ```

   in both cases, replacing `{project_slug}` with the name you used (`python-template` if you used the default).
   Some of the key files and directories are:
   - The `README.md` file is a Markdown file describing the project and acting as a landing page for first-time users.
   - The `LICENSE.md` file contains the terms of the open-source license the code is released under.
   - The `src` directory, which will contain the Python package source code.
   - The `docs` directory, which will contain the Markdown files used to generate the documentation pages for the package.
   - The `tests` directory, which will contain the Python modules defining tests to check for the correctness of the package code.

   Try viewing the content of some of the files generated by running

   ```sh
   cat {path_to_file}
   ```

   on macOS/Linux or

   ```sh
   type {path_to_file}
   ```

   on Windows, replacing `{path_to_file}` with the relevant path.

[^slug]: A ['slug'](https://en.wikipedia.org/wiki/Clean_URL#Slug) in this context is a human-readable identifier with words typically separated by hyphens that can be used as part of a URL.

## 📦 Creating a repository on GitHub for the new package

The package you created in the previous section will have been initialised locally as a Git repository (providing you answered 'Y' to the relevant prompt!) to allow keeping the package under version control, but some extra steps are required to have the local repository synchronised to a remote repository on [GitHub](https://github.com/). The advantages of doing this are that it makes it easy for other people to both download and use the package but also contribute to your project. The package has also been set up to take advantage of GitHub's continuous integration and deployment service [GitHub Actions](https://docs.github.com/en/actions) (which is free to use for public repositories) with workflows included for automatically running the package tests, performing [linting checks](<https://en.wikipedia.org/wiki/Lint_(software)>) and building the project documentation, on every [pull-request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests) and on updates to the default `main` [branch](https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell) for the repository.

When you've finished answering questions the you should see some additional instructions printed to screen.

If you have the [GitHub CLI](https://cli.github.com/) `gh` installed, you should see:

```sh
GitHub CLI detected, you can create a repo with the following:

gh repo create {github_owner}/{project_slug} -d "{project_description}" --public -r origin --source {project_slug}
```

where `{github_owner}`, `{project_slug}` and `{project_description}` are replaced with your username and your project name.
package.
You should copy-paste and run the `gh repo create ...` command,
If you closed your terminal or longer have access to the message for some reason, you can use the example above being careful to substitute the placeholders in braces `{}`.

If you get an error message at this point it may be because you have not installed `gh` or set up authorisation as [described in the setup instructions above](#️-prerequisites-for-using-the-template).

If the command worked you should see a message something like:

```sh
✓ Created repository {github_owner}/{project_slug} on GitHub
  https://github.com/{github_owner}/{project_slug}
✓ Added remote https://github.com/{github_owner}/{project_slug}.git
```

A repository will have been created at the URL (the one which doesn't end in `.git`).
You should be able to go there in your browser (either copy-paste into a browser or --depending on your terminal-- you may be able to hold `Ctrl` and click on URL directly).
Keep the browser window open for now, but return to the terminal.

> [!TIP]
> Your computer has a _*local*_ copy of this repository and GitHub has a _*remote*_ copy.

At the moment, both the remote and local repositories are empty as we have not made any commits.

To commit the package files generated by `cookiecutter`, and also push this commit to the repository on GitHub, run each of the commands below in turn.
You'll need to replace `{project_slug}` with your package name.

```sh
cd {project_slug}
git add .
git commit -m "Initial commit"
git push --set-upstream origin main
```

If you go back to your browser and refresh, you should see the package files appear.
You should also see the top-level `README.md` displayed as the repository landing page.

When you pushed to `main` you will have triggered runs of the [GitHub actions](https://docs.github.com/en/actions/about-github-actions/understanding-github-actions) workflows that are included in the template.
You can view the status of the workflow jobs by browsing the `Actions` button at the top bar of the repository homepage, which takes you to `https://github.com/{github_owner}/{project_slug}/actions`.

Depending on your account settings, you may find that the `Documentation` workflow shows as failed (❌).
If you see this it's probably because of the repository permissions settings for GitHub Actions.
We'll fix this in the next section.

For now, have a browse around the GitHub web interface.

## 📄 Configuring repository to host docs on GitHub Pages

Now that your repository is on GitHub, you need to do a few more steps to set up your project's documentation website.
The HTML documentation will be built using the `Documentation` workflow (that we're going to fix) and hosted on [GitHub Pages](https://pages.github.com/).

If you scroll back in your terminal to the end of the [cookiecutter] questions, you should be able to find a message like:

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

As before replace `{github_owner}` and `{project_slug}` with the relevant GitHub repository owner and project slug that you chose at the start.

The first part of the instructions explains how to set the permissions for GitHub Actions.
This lets the Actions bot push the built HTML documentation to a branch `gh-pages` when you update the default `main` branch.

- Go to the Actions settings page at the URL above (or via the repository `Settings` tab, then `Actions > General`).
- Set `Workflow permissions` to `Read and write permissions`.

Now that the permissions have changed, we need to re-run the `Documentation` workflow.

- Go back to the Actions page. Select the Actions button (in the top bar), or visit
  `https://github.com/{github_owner}/{project_slug}/actions`.
- Click on the failing entry for the `Documentation` workflow.
- Click on the `Re-run all jobs` button (top right of the page).

After the `Documentation` workflow finishes, a new `gh-pages` branch will be created containing only the HTML docs.

Following tha instructions printed to the terminal, go to `https://github.com/{github_owner}/{project_slug}/settings/pages` and set this branch as the source for GitHub Pages.

- Set `Source` to `Deploy from branch` and `Branch` to `gh-pages`.

This will start another new workflow called `pages-build-deployment` (in the Actions page).
When it finishes, you can view your HTML docs at:

```sh
https://{github_owner}.github.io/{project_slug}
```

🎉

You should see that the homepage of the documentation site is the same as the repository README file.
Importantly, the documentation website includes the [_application programming interface_ (API](https://en.wikipedia.org/wiki/API) reference documentation.
The API documentation is generated from [docstrings](https://peps.python.org/pep-0257/#what-is-a-docstring) in the source code.

## 🐍 Setting up a virtual environment for project

We recommend setting up a project-specific [virtual environment](https://docs.python.org/3/tutorial/venv.html) for each of your Python projects.
This means you can install the specific versions of third-party packages that each project requires without conflicting with the requirements of your other projects.

There are a lot of virtual environment management tools available for Python.
One option is [uv](https://docs.astral.sh/uv), which you will have installed if you followed our detailed set-up instructions above, or may already have installed previously.
`uv` is an extremely fast Python package and virtual environment manager that uses the familiar `pip` and [`venv`](https://docs.python.org/3/library/venv.html) commands (`venv` is the built-in virtual environment manager that comes with Python).

Back in the terminal, and from your `{project_slug}` directory, you can create a virtual environment by running:

```sh
uv venv
```

This will create a new environment in the hidden `.venv` directory.
`uv` tells you how to activate the environment:

```sh
source .venv/bin/activate
```

or on Windows:

```sh
.venv\Scripts\activate
```

Activate your environment, and you should see braces `( )` with your project slug on the left of your terminal window.
This might be slightly different depending on your terminal setup.

Once you have activated the environment you can use the following command to install any packages within the `.venv` environment

```sh
uv pip install numpy
```

(We're using `numpy` as an example.)

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
uv sync --all-groups
```

from the root of the project repository. Note that `uv>=0.6.7` is required to use the `--group` option.

<details><summary>Using venv as an alternative to uv </summary> <!-- markdownlint-disable-line MD033 -->

Alternatively, you can use the [`venv` module](https://docs.python.org/3/library/venv.html), which is slower and has fewer features, when compared to `uv`, but is built-in to the Python standard library. `venv` has the advantage of being available in any Python (3.3+) environment, but unlike `uv` will not by itself allow you to use a different Python version from the system level install. A common pattern is to store the virtual environment files in a directory `.venv` within the root directory of the project repository. This can be achieved by running

```sh
python -m venv
```

from the root of the project repository. To activate the new virtual environment, if on Linux or MacOS run from the root of the project repository

```sh
source .venv/bin/activate
```

or if on Windows

```sh
.venv\Scripts\activate
```

Once you've activated the environment you can make sure the version of the Python package manager `pip` installed in the environment is up to date:

```sh
python -m pip install --upgrade pip
```

Similar to `uv`, once the environment is active, you can install the package in editable mode as well as all dependencies:

```sh
python -m pip install --editable . --group dev --group docs --group test
```

</details>

## 🧪 Running package tests locally

The package template includes support for running tests using the [`pytest` testing framework](https://docs.pytest.org/).
Tests are defined in the `tests` directory.
By default a single test module `tests/test_dummy.py` is created with a placeholder test.
You can run the tests locally using `pytest` in your virtual environment:

```sh
pytest
```

from the root of the project repository.

The package template also sets up [`tox`](https://tox.wiki).
`tox` is a tool which allows you to easily run tests in isolated environments under different Python versions.
These tests don't interfere with the virtual environment that you use for developing the code.

You can run the tests across _all compatible Python versions currently installed_ using `tox` by running

```sh
tox
```

from the root of the project repository.

## 📖 Building documentation locally

It's sometimes useful to be able to render the HTML documentation pages locally.
For example if you're editing docstrings or adding additional pages, and you want to check everything worked.
The package is set up to use [MkDocs](https://www.mkdocs.org/) to build the documentation website.
The API documentation is generated using the [`mkdocstrings` plug-in](https://mkdocstrings.github.io/).
MkDocs and `mkdocstrings` will have been installed in your local development environment, because you installed the package with the `docs` dependencies.

To build and serve the documentation locally run:

```sh
mkdocs serve
```

from the root of the project repository and navigate to `http://127.0.0.1:8000/` in your browser.
The development server supports _auto-reloading_, meaning the content will be automatically refreshed in your browser if you make any edits to the docstrings or README.md.

There's also a `tox` environment called `docs`.
This is another way to build the documentation but in an isolated environment.
It is the command that is run in GitHub actions to build and publish the on the web (in the `Documentation` workflow).
This might be useful if debugging the Actions build, or if you didn't install the `docs` dependencies into your virtual environment.

Run:

```sh
tox -e docs
```

from the root of the project repository.
The built documentation will be output to a directory `site`.

## ✅ Using `pre-commit` to run checks when committing

The package is set-up to use [pre-commit](https://pre-commit.com/), a framework for running [Git hook scripts](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks) on each commit to the repository.

There is a `.pre-commit-config.yaml` configuration file which you can take a look at.
With this setup `pre-commit` will run a series of fast linters, checks and formatters on the repository on every commit.

The main tools we recommend are [ruff](https://docs.astral.sh/ruff/), [mypy](https://mypy.readthedocs.io/en/stable/) and [prettier](https://prettier.io/).
These Git hook scripts can installed locally by running

```sh
pre-commit install
```

from the root of the project repository.
You will only need to do this once per `git clone` of the code.

Once installed, the scripts will be called to inspect the changes each time `git commit` is run.
Any failures of the checks will need to be fixed before the changes can be committed.
Some of the `pre-commit` hooks include support for auto-fixing easy problems - in this case you will be alerted that a file has been changed by a hook and these changes need to be staged using `git add` before recommitting.

The hooks typically only run on the files _changed_ in a commit.
The `pre-commit` hooks can be run against _all files in the repository_ by running

```sh
pre-commit run --all-files
```

from the root of the project repository.
This is useful to check they will pass if the `pre-commit` configuration is updated, for example, when [adding a new plug-in](https://pre-commit.com/#plugins).
