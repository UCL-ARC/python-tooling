---
title: Documentation
layout: default
---

## Documentation

With Python, as with many other languages, it's very common to automatically
create a web page with documentation. This can include reference for the API
taken from your package's [docstrings], tutorials, examples, and more in depth
explanation about how the package works. For an in-depth discussion of the
different components of good documentation, see the
[Diátaxis framework](https://diataxis.fr/). For your package to be easily
reusable we recommend you build documentation pages and host them somewhere.

If you're using GitHub, one option is to host your docs on [GitHub pages].
[Here's how we've set this up][template-docs-dot-yaml] for [our template].

<!-- URL used above in the blurb-->

[docstrings]: https://peps.python.org/pep-0257/#what-is-a-docstring
[GitHub pages]: https://docs.github.com/en/pages
[our template]: https://github.com/UCL-ARC/python-tooling?tab=readme-ov-file#using-this-template
[template-docs-dot-yaml]: https://github.com/UCL-ARC/python-tooling/blob/main/%7B%7Bcookiecutter.project_slug%7D%7D/.github/workflows/docs.yml

### Documentation build tools

| Name      | Short description                                                                                                                                               |                      🚦                      |
| --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------: |
| [MkDocs]  | Generates documentation from Markdown files, with a plugin to generate API documentation. A good plugin ecosystem and balance of usability and customisability. | <span class="label label-green">Best</span>  |
| [Sphinx]  | Generates documentation from reStructuredText or Markdown files, long been the de-facto standard and very widely used. Mature plugin ecosystem.                 | <span class="label label-yellow">Good</span> |
| [gitbook] | General documentation builder; integrates with GitHub.                                                                                                          | <span class="label label-yellow">Good</span> |
| [pdoc]    | Auto-generates API documentation from docstrings, beginner friendly but with less of a plugin ecosystem than others.                                            | <span class="label label-yellow">Good</span> |

<details markdown="block"><summary>More details about Sphinx</summary><!-- markdownlint-disable-line MD033 -->

We marginally recommend [MkDocs] over [Sphinx] due to it's ease of use,
preference for Markdown, and more support for a variety of docstring styles.

However the [Sphinx] tool has long been the de-facto standard in the scientific
Python ecosystem. It is widely used, customisable, and well tested. If you need
a [Sphinx extension](#sphinx-extensions) that does not have an equivalent
[MkDocs plugin](https://github.com/mkdocs/catalog), or if you are part of a
community that heavily uses [Sphinx] then we recommend you use that instead.

#### See also

- Our internal discussions about which to recommend
  ([#16](https://github.com/UCL-ARC/python-tooling/issues/16) and
  [#187](https://github.com/UCL-ARC/python-tooling/issues/187)).
- [An interesting related discussion](https://github.com/encode/httpx/discussions/1220).

</details>

<!-- URLS used above -->

[MkDocs]: https://www.mkdocs.org/
[Sphinx]: https://www.sphinx-doc.org/en/master/
[gitbook]: https://www.gitbook.com/
[pdoc]: https://pdoc.dev/

### MkDocs plugins

| Name                                                          | Short description                            |                     🚦                      |
| ------------------------------------------------------------- | -------------------------------------------- | :-----------------------------------------: |
| [mkdocstrings-python](https://mkdocstrings.github.io/python/) | Automatically generates API reference pages. | <span class="label label-green">Best</span> |

### Sphinx extensions

| Name                                                                 | Short description                                                |                     🚦                      |
| -------------------------------------------------------------------- | ---------------------------------------------------------------- | :-----------------------------------------: |
| [sphinx-gallery](https://sphinx-gallery.github.io/stable/index.html) | Builds an HTML gallery of examples from a set of Python scripts. | <span class="label label-green">Best</span> |
| [sphinx-autoapi](https://sphinx-autoapi.readthedocs.io/en/stable/)   | Automatically generates API reference pages.                     | <span class="label label-green">Best</span> |
