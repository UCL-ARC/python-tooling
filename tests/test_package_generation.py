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
    default_config_with: typing.Callable,
    generate_package: typing.Callable,
) -> None:
    """Test package generation."""
    # Not having a git repo makes it easier to check in/out reference
    # data files to the main python-tooling git repository
    config = default_config_with(initialise_git_repository="False")
    _, test_project_dir = generate_package(config=config)

    expected_package_dir = (
        pathlib.Path(__file__).parent / "data" / "test_package_generation"
    )
    assert test_project_dir.exists(), "Project directory does not exist."

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
                ),
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
    venv: pytest_venv.VirtualEnvironment,
    generate_package: typing.Callable,
) -> None:
    """Test generated package is pip installable."""
    _, test_project_dir = generate_package()
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


@pytest.mark.parametrize("funder", ["", "STFC", "UKRI", "Wellcome Trust"])
def test_optional_funder(
    funder: str,
    default_config_with: typing.Callable,
    generate_package: typing.Callable,
) -> None:
    """Test specifying funder or not in package generation."""
    config = default_config_with(funder=funder)
    _, test_project_dir = generate_package(config)

    with (test_project_dir / "README.md").open() as f:
        readme_text = "".join(f.readlines())

    if funder == "":
        assert "## Acknowledgements" not in readme_text
    else:
        assert (
            f"## Acknowledgements\n\nThis work was funded by {funder}." in readme_text
        ), readme_text


def test_docs_build(
    venv: pytest_venv.VirtualEnvironment,
    generate_package: typing.Callable,
) -> None:
    """Test documentation build from package created from template."""
    _, test_project_dir = generate_package()
    venv.install("tox")
    tox_docs_process = subprocess.run(  # noqa: S603
        [
            pathlib.Path(venv.bin) / "tox",
            "-e",
            "docs",
        ],
        cwd=test_project_dir,
        capture_output=True,
        check=False,
    )
    assert tox_docs_process.returncode == 0, (
        f"Something went wrong with building docs: {tox_docs_process.stderr!r}"
    )


def test_package_tests_tox(
    tmp_path: pathlib.Path,
    venv: pytest_venv.VirtualEnvironment,
    generate_package: typing.Callable,
) -> None:
    """
    Test that the package tests pass in all tox environments.

    ...and that no warnings are raised (e.g. coverage).
    """
    config = {
        "github_owner": "test-user",
        "project_short_description": "description",
        "project_name": "Cookiecutter Test",
    }
    generate_package(config, tmp_path)
    test_project_dir = tmp_path / "cookiecutter-test"
    venv.install("tox")
    tox_multienv_test_process = subprocess.run(  # noqa: S603
        [pathlib.Path(venv.bin) / "tox"],
        check=False,
        cwd=test_project_dir,
        capture_output=True,
    )
    tests_pass = tox_multienv_test_process.returncode == 0
    assert tests_pass, "Template tests failed in one or more tox environments."
    output = tox_multienv_test_process.stdout.decode()
    assert "WARNING:" not in output, f"Warnings raised during tests: {output}"
