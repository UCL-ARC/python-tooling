"""Checks that the cookiecutter works."""

import difflib
import os
import pathlib
import shutil
import subprocess
import typing

import pytest
import pytest_venv  # type: ignore[import-not-found]


def get_all_files_folders(root_path: pathlib.Path) -> set[pathlib.Path]:
    """
    Get all files and folders under a directory.

    The paths are returned relative to the root path given.
    __pycache__ directories and .DS_Store files are ignored.
    """
    file_set: set[pathlib.Path] = set()
    for dirpath, _, filenames in os.walk(root_path):
        dirpath_path = pathlib.Path(dirpath).relative_to(root_path)
        if dirpath_path.name in ["__pycache__"]:
            continue

        # Add this directory
        file_set.update((dirpath_path,))
        # Add any files in it
        for filename in filenames:
            if filename in [".DS_Store"]:
                continue
            file_set.update((dirpath_path / filename,))

    return file_set


def test_package_generation(
    tmp_path: pathlib.Path,
    generate_package: typing.Callable,
) -> None:
    """Test package generation."""
    test_config = {
        "github_owner": "test-user",
        "project_short_description": "description",
        "project_name": "Cookiecutter Test",
        # Not having a git repo makes it easier to check in/out reference
        # data files to the main python-tooling git repository
        "initialise_git_repository": False,
    }
    generate_package(config=test_config, path=tmp_path)

    expected_package_dir = (
        pathlib.Path(__file__).parent / "data" / "test_package_generation"
    )
    # Check project directory exists
    test_project_dir = tmp_path / "cookiecutter-test"
    assert test_project_dir.exists()

    actual_files = get_all_files_folders(test_project_dir)
    expected_files = get_all_files_folders(expected_package_dir)

    assert actual_files == expected_files

    # Check diff between actual and expected file contents
    diff = ""
    for file in actual_files:
        actual_file = test_project_dir / file
        expected_file = expected_package_dir / file

        if actual_file.is_dir():
            continue

        with actual_file.open() as f1, expected_file.open() as f2:
            diff += "".join(
                difflib.unified_diff(
                    f1.readlines(),
                    f2.readlines(),
                    fromfile=str(actual_file),
                    tofile=str(expected_file),
                )
            )

    if diff:
        shutil.rmtree(expected_package_dir)
        shutil.move(test_project_dir, expected_package_dir)
        msg = (
            "Non-zero diff between generated files and expected files.\n"
            "Test data files have been modified with new content.\n"
            "Diff is:\n"
            f"{diff}"
        )
        raise RuntimeError(msg)


def test_pip_installable(
    tmp_path: pathlib.Path,
    venv: pytest_venv.VirtualEnvironment,
    generate_package: typing.Callable,
) -> None:
    """Test generated package is pip installable."""
    test_config = {
        "github_owner": "test-user",
        "project_short_description": "description",
        "project_name": "Cookiecutter Test",
    }
    generate_package(config=test_config, path=tmp_path)
    test_project_dir = tmp_path / "cookiecutter-test"
    # Try to install package in virtual environment with pip
    pipinstall = subprocess.run(  # noqa: S603
        [
            venv.python,
            "-m",
            "pip",
            "install",
            "-e",
            test_project_dir,
        ],
        capture_output=True,
        check=False,
    )
    assert pipinstall.returncode == 0, (
        f"Something went wrong with installation: {pipinstall.stderr!r}"
    )


@pytest.mark.parametrize("funder", ["", "STFC"])
def test_optional_funder(
    tmp_path: pathlib.Path, generate_package: typing.Callable, funder: str
) -> None:
    """Test package generation."""
    config = {
        "github_owner": "test-user",
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
