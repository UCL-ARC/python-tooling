# ARC Python Package Template

⚠️ This repository is still under construction! ⚠️

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

This is a Python package template for new ARC Python packages.
It automatically creates new Python packages with the recommended tooling set up and ready to go.
The recommended tooling is documented on the [UCL-ARC/python-tooling website](http://github-pages.arc.ucl.ac.uk/python-tooling/).

If you're making a package within a community that has an existing package template (e.g., [`scikit-hep`](https://github.com/scikit-hep/cookie)), we recommend using their template instead of this one.

## Using the template

This is a [cookieninja](https://cookieninja.readthedocs.io/en/latest/) template, so firstly you'll need to install that.

```bash
python -m pip install cookieninja
```

It should then be as simple as running cookieninja with this template as input:

```bash
cookieninja gh:ucl-arc/python-template
```

You'll be prompted to enter some details. If you don't enter anything you'll get cookieninja's best guess or recommended values which are in square braces.
