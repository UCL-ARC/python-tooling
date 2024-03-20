"""Configuration file for the Sphinx documentation builder."""

import datetime
from importlib.metadata import version as get_version

# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "{{cookiecutter.package_name}}"
author = "{{cookiecutter.author_given_names}} {{cookiecutter.author_family_names}}"
copyright = f"{datetime.datetime.now(tz=datetime.timezone.utc).year}, {author}"  # noqa: A001
release = get_version("{{cookiecutter.package_name}}")
version = ".".join(release.split(".")[:2])

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "autodoc2",
    "myst_parser",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
}

exclude_patterns = ["_build"]

autodoc2_packages = ["../src/{{cookiecutter.package_name}}"]
autodoc2_render_plugin = "myst"

myst_enable_extensions = ["fieldlist"]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "pydata_sphinx_theme"

html_theme_options = {
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/",
            "icon": "fa-brands fa-github",
            "type": "fontawesome",
        },
    ],
}
