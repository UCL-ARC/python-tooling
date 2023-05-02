"""Checks that the cookiecutter works."""

import pathlib as pl
import subprocess

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


def test_package_generation(
    tmp_path: pl.Path,
    project_config: dict,
):
    """
    Creates a project cookiecutter from the template.

    Once the project is made it verifies a series of actions work.

    tmp_path pytest fixture preferred over tmpdir
    see https://docs.pytest.org/en/7.3.x/how-to/tmp_path.html#the-tmpdir-and-tmpdir-factory-fixtures

    Args:
    ----
        tmpdir: A temporary directory path object which is unique.
    """
    # Run cookieninja with PROJECT_SLUG for project_slug
    subprocess.run(
        [  # noqa: S607
            "cookieninja",
            ".",
            "--no-input",
            "--output-dir",
            str(tmp_path),
            f"project_slug={project_config['project_slug']}",
        ],
        shell=False,  # noqa: S603
    )

    # Check parent directory exists
    assert (tmp_path / project_config["project_slug"]).exists()

    # Check files and directories inside
    expected_files = [
        "README.md",
        ".pre-commit-config.yaml",
        "LICENSE.md",
        "pyproject.toml",
        "src",
        pl.Path("src") / project_config["project_slug"],
        "tests",
        pl.Path(".github"),
        pl.Path(".github") / "workflows",
    ]
    for f in expected_files:
        assert (tmp_path / project_config["project_slug"] / f).exists()
