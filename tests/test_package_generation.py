"""Checks that the cookiecutter works."""

import os
import pathlib
import subprocess
import typing

import pytest


def get_all_files_folders(root_path: pathlib.Path) -> set[pathlib.Path]:
    """
    Get all files and folders under a directory.

    The paths are returned relative to the root path given.
    """
    file_set: set[pathlib.Path] = set()
    for dirpath, _, filenames in os.walk(root_path):
        dirpath_path = pathlib.Path(dirpath).relative_to(root_path)

        # Add this directory
        file_set.update((dirpath_path,))
        # Add any files in it
        for filename in filenames:
            file_set.update((dirpath_path / filename,))

    return file_set


def test_package_generation(
    tmp_path: pathlib.Path,
    generate_package: typing.Callable,
) -> None:
    """Test package generation."""
    test_config = {
        "github_username": "test-user",
        "project_short_description": "description",
        "project_name": "Cookiecutter Test",
    }
    generate_package(config=test_config, path=tmp_path)

    # Check project directory exists
    test_project_dir = tmp_path / "cookiecutter-test"
    assert test_project_dir.exists()

    # Check main files and directories inside
    expected_files: set[pathlib.Path] = {
        pathlib.Path(),
        pathlib.Path(".git"),
        pathlib.Path(".github"),
        pathlib.Path(".github/ISSUE_TEMPLATE"),
        pathlib.Path(".github/ISSUE_TEMPLATE/bug_report.yml"),
        pathlib.Path(".github/ISSUE_TEMPLATE/config.yml"),
        pathlib.Path(".github/ISSUE_TEMPLATE/documentation.yml"),
        pathlib.Path(".github/ISSUE_TEMPLATE/feature_request.yml"),
        pathlib.Path(".github/ISSUE_TEMPLATE/question.yml"),
        pathlib.Path(".github/workflows"),
        pathlib.Path(".github/workflows/docs.yml"),
        pathlib.Path(".github/workflows/linting.yml"),
        pathlib.Path(".github/workflows/tests.yml"),
        pathlib.Path(".gitignore"),
        pathlib.Path(".pre-commit-config.yaml"),
        pathlib.Path("CITATION.cff"),
        pathlib.Path("LICENSE.md"),
        pathlib.Path("README.md"),
        pathlib.Path("docs"),
        pathlib.Path("docs/LICENSE.md"),
        pathlib.Path("docs/api.md"),
        pathlib.Path("docs/index.md"),
        pathlib.Path("mkdocs.yml"),
        pathlib.Path("pyproject.toml"),
        pathlib.Path("schemas"),
        pathlib.Path("schemas/github-issue-forms.json"),
        pathlib.Path("src"),
        pathlib.Path("src/cookiecutter_test"),
        pathlib.Path("src/cookiecutter_test/__init__.py"),
        pathlib.Path("tests"),
        pathlib.Path("tests/test_dummy.py"),
        pathlib.Path("tests/__pycache__"),
        pathlib.PosixPath("tests/__pycache__/test_dummy.cpython-*-pytest-*.pyc"),
    }

    actual_files = get_all_files_folders(test_project_dir)
    # Filter out anything under .git/ to make comparison easier
    actual_files = actual_files - {
        a for a in actual_files if len(a.parts) > 1 and a.parts[0] == ".git"
    }

    assert actual_files == expected_files

    # Check it's pip-installable
    pipinstall = subprocess.run(  # noqa: S603
        [  # noqa: S607
            "python",
            "-m",
            "pip",
            "install",
            "-e",
            test_project_dir,
        ],
        capture_output=True,
        check=False,
    )
    assert (
        pipinstall.returncode == 0
    ), f"Something went wrong with installation: {pipinstall.stderr!r}"


@pytest.mark.parametrize("funder", ["", "STFC"])
def test_optional_funder(
    tmp_path: pathlib.Path, generate_package: typing.Callable, funder: str
) -> None:
    """Test package generation."""
    config = {
        "github_username": "test-user",
        "project_short_description": "description",
        "project_name": "Cookiecutter Test",
        "funder": funder,
    }

    generate_package(config, tmp_path)

    test_project_dir = tmp_path / "cookiecutter-test"
    with (test_project_dir / "README.md").open() as f:
        readme_text = "".join(f.readlines())

    if funder == "":
        assert "## Acknowledgements" not in readme_text
    else:
        assert (
            f"## Acknowledgements\n\nThis work was funded by {config['funder']}."
            in readme_text
        ), readme_text
