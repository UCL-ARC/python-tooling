# Contributing Guide

This template and our [recommendation pages][website] were made by [research
software engineers] at [UCL's Centre for Advanced Research Computing][UCL ARC].
We made it with research software projects in mind, but whoever you are, we hope
you find this useful!

We are actively encouraging users to ask questions and start discussions in the
[discussions tab] of this repository. Does something seem like it's broken?
Please go ahead and [open an issue]!

The [website] pages are open to contributions but they will need to be reviewed
by a member or associate member of ARC. We might be slow to approve new tool
suggestions (since we'll probably want to discuss them first) but don't let that
put you off creating an issue.

## Development workflow

To contribute a change, please:

1. Create a new branch (or fork if you're not in [@UCL-ARC/collaborations]).
2. Modify an existing page, create a new one, or tweak the template. a. Run
   [pre-commit](https://pre-commit.com) which will lint your changes. b. Check
   the tests pass if you modified the template (`pytest -s`).
3. Open a _pull request_ (PR) with changes.
4. Ask someone who did not contribute to the PR from [@UCL-ARC/collaborations]
   to review it.
5. If approved with no comments, then the reviewer will merge the PR.
6. If changes are requested, the PR author should address the comments, and then
   ask for review again.

<!-- links here -->

<!-- prettier-ignore-start -->
[website]: https://github-pages.arc.ucl.ac.uk/python-tooling
[UCL ARC]: https://ucl.ac.uk/arc
[open an issue]: https://github.com/UCL-ARC/python-tooling/issues/new/choose
[Discussions tab]: https://github.com/UCL-ARC/python-tooling/discussions
[Research software engineers]: https://society-rse.org/about/history
[@UCL-ARC/collaborations]: https://github.com/orgs/UCL-ARC/teams/collaborations
<!-- prettier-ignore-end -->

## Notes for developers

<details><summary>Click to expand...</summary> <!-- markdownlint-disable-line MD033 -->

First, clone repository

- (Optional) Generate your SSH keys as suggested
  [here](https://docs.github.com/en/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)
- (Optional) GitHub CLI as suggested
  [here](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account?tool=cli)
- Clone the repository by typing (or copying) the following line in a terminal
  at your selected path in your machine:

```sh
git clone git@github.com:UCL-ARC/python-tooling.git
cd python-tooling
```

### Developing the cookiecutter template

- To create and remove your virtual environment

  ```sh
  uv venv
  source .venv/bin/activate
  # do your work
  deactivate
  ```

- To run template in the same path of this repo. We do a test cookiecut of a
  dummy package and install it to ensure the template setup works.

  ```sh
  cookiecutter .
  cd python-template
  git init
  uv pip install -e ".[dev]"
  ```

- To run cookiecutter using a specific branch of the template:

  ```sh
  cookiecutter https://github.com/UCL-ARC/python-tooling --checkout <branch-name>
  ```

- To run the tests locally:

  ```sh
  pytest -s
  ```

### Developing the recommended tooling pages

Pages all live in the
[docs/pages](https://github.com/UCL-ARC/python-tooling/tree/main/docs/pages)
sub-directory, and are written in markdown.

To build the webpage locally (for testing)

1. [Install jekyll](https://jekyllrb.com/docs/installation)
2. Run `bundle install` from the `docs/` directory of this repository to
   install dependencies.
3. Run `bundle exec jekyll serve` from the root directory of this repository.
   This should fire up a local web server and tell you its address. By default
   the server will automatically refresh the HTML pages if any changes are made
   to the markdown sources.

See the [jekyll docs](https://jekyllrb.com/docs) for more info.

</details>

If you have this repo locally (this may be the case if you are developing),
you can run the following:

```sh
cookiecutter /path/to/your/checkout/of/python-tooling --checkout latest
```
