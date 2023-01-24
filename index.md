---
title: Home
layout: home
nav_order: 1
---

This site documents common tooling we use in Python projects at the [Advanced Research Computing center](https://www.ucl.ac.uk/arc/) (ARC) at [UCL](https://www.ucl.ac.uk).

It is not comprehensive, but intended as a forum to share knowledge across projects.
Each page contains a table of packages or services that are useful when building a Python package.
Each entry has a link to the package or service, and a short summary of what it does.

## Choosing tools
If you are working within a larger community, always start with the same tools they recommend - as an example, the [`napari`](https://napari.org/) community have  [`cookiecutter-napari-plugin`](https://github.com/napari/cookiecutter-napari-plugin) for setting up a new pacakge.
This makes it easier for others in the community to contribute to your package, and once you get used to the structure makes it easier for you to contribute back to other packages.

Otherwise, each page on this site highlights recommended packages or services for each area.
These shouldn't be taken as set in stone for every project, but are a good place to start.

### Traffic lights
Each item has an (opinionated) traffic light. The meaning of these is:
- 🟢 At least one person in ARC uses this. We actively recommend using it above other tools. It is the single recommended package for a given purpose.
- 🟠 We don't discourage using this, but it may duplicate functionality of a green tool.
- 🔴 We actively discourage using this. This could be because it's no longer maintained, not open source, or difficult to use. Consider moving to alternatives if you're currently using something that's red. A reason is given next to each red item.
