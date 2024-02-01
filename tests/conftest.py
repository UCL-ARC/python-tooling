"""Defines fixtures for tests."""

import pytest


@pytest.fixture()
def project_config() -> dict:
    """
    Pytest fixture for defining the project config.

    Returns
    -------
    dict
        dictionary with values for the cookiecutter template,
        as defined in the cookiecutter.json

    """
    return {
        "github_username": "test-user",
        "project_short_description": "description",
        "project_name": "Cookiecutter Test",
        "expected_repo_name": "cookiecutter-test",
        "expected_package_name": "cookiecutter_test",
    }
