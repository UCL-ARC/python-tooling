---
title: Templates
layout: default
nav_order: 2
---

## Package templates

### Recommended ARC template

The [UCL-ARC/python-tooling](https://github.com/UCL-ARC/python-tooling)
repository contains our recommended package template for new ARC projects. It
pre-configures the recommended tools listed in the other pages of this site. If
you are working on a new project, our template should be a good starting point!
We have a [tutorial](https://github.com/UCL-ARC/python-tooling/blob/main/tutorial.md)
available with detailed instructions for creating a package using the template
and how to use the newly created package with some of the tools included.

If you're making a package for a community that already has a template in
general use (some examples are listed below) we recommend using their template
instead.

### Community-specific templates

If you're making a package within one of these communities, we recommend using
their package template.

| Community                                                          | Short description                                                                                                                               |
| ------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| [Napari](https://github.com/napari/cookiecutter-napari-plugin)     | Cookiecutter template for authoring (npe2-based) napari plugins.                                                                                |
| [SciKit-Surgery](https://github.com/SciKit-Surgery/PythonTemplate) | Cookiecutter template developed by the Wellcome EPSRC Centre for Interventional and Surgical Sciences.                                          |
| [Scientific Python](https://github.com/scientific-python/cookie)   | Cookiecutter template developed by [Scikit-HEP](https://github.com/scikit-hep) but now adopted by the more general Scientific Python community. |

### Template engines

Tools that can be used for creating your own package template.

| Name                                                                                                                          | Short description                                                                                                            |                      🚦                      |
| ----------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------: |
| [Cookiecutter](https://github.com/cookiecutter/cookiecutter)                                                                  | Widely-used tool for creating project templates                                                                              | <span class="label label-green">Best</span>  |
| [Copier](https://github.com/copier-org/copier)                                                                                | A tool to create project templates that are highly configurable. Project configuration can be kept in sync with the templae. | <span class="label label-yellow">Good</span> |
| [Cruft](https://github.com/cruft/cruft)                                                                                       | Can be used to create projects from a cookiecutter template and to keep the project configuration in sync with the template. | <span class="label label-yellow">Good</span> |
| [GitHub templates](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-template-repository) | GitHub repositories can be used as templates, but they are not configurable.                                                 | <span class="label label-yellow">Good</span> |
| [Cookieninja](https://github.com/cookieninja-generator/cookieninja)                                                           | A fork of Cookiecutter that is not actively maintained.                                                                      |  <span class="label label-red">Avoid</span>  |
