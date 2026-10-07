"""Checks that the cookiecutter works."""

import pathlib
import subprocess
import typing

import pytest
import pytest_venv  # type: ignore[import-not-found]


def test_package_generation(
    default_config_with: typing.Callable,
    generate_package: typing.Callable,
) -> None:
    """
    Test package generation works.

    Ensures that the template can be cookiecut, and that the default project name is as
    expected from the default config fixture.
    """
    config = default_config_with(initialise_git_repository="False")
    result, test_project_dir = generate_package(config=config)

    assert result.returncode == 0, result.stderr
    assert test_project_dir.exists(), "Project directory does not exist."

    expected = (
        pathlib.Path("README.md"),
        pathlib.Path("pyproject.toml"),
        pathlib.Path("docs/index.md"),
        pathlib.Path("src/cookiecutter_test/__init__.py"),
    )
    for file in expected:
        assert (test_project_dir / file).is_file(), f"Missing generated file: {file}"

    readme_text = (test_project_dir / "README.md").read_text()
    pyproject_text = (test_project_dir / "pyproject.toml").read_text()
    package_text = (test_project_dir / "src/cookiecutter_test/__init__.py").read_text()
    assert "# Cookiecutter Test" in readme_text
    assert 'name = "cookiecutter-test"' in pyproject_text
    assert 'description = "description"' in pyproject_text
    assert '"cookiecutter_test package."' in package_text


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
