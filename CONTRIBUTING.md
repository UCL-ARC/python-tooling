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
