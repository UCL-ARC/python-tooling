"""Checks that the cookiecutter works."""

import difflib
import pathlib
import shutil
import subprocess
import typing

import pytest
import pytest_venv  # type: ignore[import-not-found]

from .helpers import (  # type: ignore[import-not-found]
    DEFAULT_CONFIG,
    get_all_files_folders,
)


def test_package_generation(generate_package: typing.Callable) -> None:
    """Test package generation."""
    test_config = DEFAULT_CONFIG.copy()
    # Not having a git repo makes it easier to check in/out reference
    # data files to the main python-tooling git repository
    test_config["initialise_git_repository"] = "False"
    _, test_project_dir = generate_package(config=test_config)

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
def test_optional_funder(generate_package: typing.Callable, funder: str) -> None:
    """Test specifying funder or not in package generation."""
    config = DEFAULT_CONFIG.copy()
    config["funder"] = funder
    _, test_project_dir = generate_package(config)

    with (test_project_dir / "README.md").open() as f:
        readme_text = "".join(f.readlines())

    if funder == "":
        assert "## Acknowledgements" not in readme_text
    else:
        assert (
            f"## Acknowledgements\n\nThis work was funded by {config['funder']}."
            in readme_text
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
