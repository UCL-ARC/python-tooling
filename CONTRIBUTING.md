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
   [pre-commit] which will lint your changes. b. Check
   the tests pass if you modified the template (`pytest -s`).
3. Open a _pull request_ (PR) with changes.
4. Ask someone who did not contribute to the PR from [@UCL-ARC/collaborations]
   to review it.
5. If approved with no comments, then the reviewer will merge the PR.
6. If changes are requested, the PR author should address the comments, and then
   ask for review again.

### Developing the cookiecutter template

We quite like installing cookiecutter as a [uv tool], so it's available globally:

```sh
uv tool install cookiecutter
```

To run cookiecutter using a specific branch of the template:

```sh
cookiecutter gh:UCL-ARC/python-tooling --checkout <branch-name>
```

If you have this repo locally (presumably the case if you're developing), you
can instead run the following:

```sh
cookiecutter /path/to/your/checkout/of/python-tooling --checkout <branch-name>
```

You can omit the `--checkout` option if you're already on the
branch you want to test.

#### Python version support

[![SPEC 0 — Minimum Supported Dependencies](https://img.shields.io/badge/SPEC-0-green?labelColor=%23004811&color=%235CA038)](https://scientific-python.org/specs/spec-0000/)

We follow Scientific Python's [SPEC 0](https://scientific-python.org/specs/spec-0000/) policy.
Notably this means our template will support [Python versions for three years after their release](https://scientific-python.org/specs/spec-0000/#support-window), and changes to the template are required to pass tests in all such python versions.
(See [the CI checks](./.github/workflows/test.yml) for precise details.)

### Developing the recommended tooling pages

Pages all live in the `docs/pages` sub-directory, and are written in markdown.

To build the webpage locally (for testing)

1. [Install jekyll]
2. Run `bundle install` from the `docs/` directory of this repository to
   install dependencies.
3. Run `bundle exec jekyll serve` from the root directory of this repository.
   This should fire up a local web server and tell you its address. By default
   the server will automatically refresh the HTML pages if any changes are made
   to the markdown sources.

See the [jekyll docs] for more info.

<!-- links here -->

<!-- prettier-ignore-start -->
[website]: https://github-pages.arc.ucl.ac.uk/python-tooling
[UCL ARC]: https://ucl.ac.uk/arc
[open an issue]: https://github.com/UCL-ARC/python-tooling/issues/new/choose
[Discussions tab]: https://github.com/UCL-ARC/python-tooling/discussions
[Research software engineers]: https://society-rse.org/about/history
[pre-commit]: https://pre-commit.com
[@UCL-ARC/collaborations]: https://github.com/orgs/UCL-ARC/teams/collaborations
[uv tool]: https://docs.astral.sh/uv/guides/tools
[Install jekyll]: https://jekyllrb.com/docs/installation
[jekyll docs]: https://jekyllrb.com/docs
<!-- prettier-ignore-end -->
