"""Defines fixtures for tests."""

import pytest


@pytest.fixture()
def project_config():
    """
    Pytest fixture for defining the project config.

    Returns
    -------
    dict
        dictionary with values for the cookiecutter template,
        as defined in the cookiecutter.json
    """
    return {
        "project_slug": "cookiecutter_test",
    }
