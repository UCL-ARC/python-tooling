---
title: Home
layout: home
nav_order: 1
---

This site documents common tooling we use in research software Python projects
at the [Centre for Advanced Research Computing](https://www.ucl.ac.uk/arc/)
(ARC) at [UCL](https://www.ucl.ac.uk).

These pages started as a forum to share knowledge across projects and have now
grown into a list of our default recommendations. Each page contains a table of
packages, tools, or services that are useful when working on a Python project.
Each entry has

- a link to the package, tool, or service,
- a short summary of what it does,
- and traffic light!

## Choosing tools

If you are working within a larger community, always start with the same tools
they recommend. For example, the [napari](https://napari.org/) community have a
[`cookiecutter-napari-plugin`](https://github.com/napari/cookiecutter-napari-plugin)
template and the
[SciKit-Surgery](https://scikit-surgery.github.io/scikit-surgery/) community
have [PythonTemplate](https://github.com/SciKit-Surgery/PythonTemplate), both
used to create new Python-based packages. Using common tooling and structure
makes it easier for others in the community to contribute to your package. Once
_you_ get used to the structure makes it easier for you to contribute back to
other packages.

If you just want to get started with our recommendations, we have
[our own Python package template](https://github.com/UCL-ARC/python-tooling#using-this-template)
that lives in the same repository as these pages.

Otherwise, each page on this site highlights recommended packages or services
for each area. These should not be taken as set in stone for every project, but
are a good place to start.

### Traffic lights

Each item has an (opinionated) traffic light. The meaning of these is:

- <span class="label label-green">Best</span> At least one person in ARC uses this. We actively recommend using it above
  other tools. It is the single recommended tool for a given purpose.
- <span class="label label-yellow">Good</span> We don't discourage using this, but it may duplicate functionality of a
  green tool.
- <span class="label label-red">Avoid</span> We actively discourage using this. This could be because it's no longer
  maintained, not open source, or difficult to use. Consider moving to
  alternatives if you're currently using something that's red. A reason for not
  using this is given.
