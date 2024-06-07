"""Checks that the cookiecutter works."""

import pathlib
import subprocess

from .helpers import gen_package


def test_package_generation(
    tmp_path: pathlib.Path,
) -> None:
    """Test package generation."""
    config = {
        "github_username": "test-user",
        "project_short_description": "description",
        "project_name": "Cookiecutter Test",
    }

    gen_package(tmp_path, config)

    # Check project directory exists
    test_project_dir = tmp_path / "cookiecutter-test"
    assert test_project_dir.exists()

    # Check main files and directories inside
    expected_files: list[str | pathlib.Path] = [
        "README.md",
        ".pre-commit-config.yaml",
        "LICENSE.md",
        "pyproject.toml",
        "src",
        pathlib.Path("src") / "cookiecutter_test",
        pathlib.Path("src") / "cookiecutter_test" / "__init__.py",
        "tests",
        pathlib.Path(".github"),
        pathlib.Path(".github") / "workflows",
        "mkdocs.yml",
        pathlib.Path("docs") / "index.md",
        pathlib.Path("docs") / "api.md",
    ]
    for f in expected_files:
        full_path = test_project_dir / f
        assert (
            full_path.exists()
        ), f"Expected file/folder: {full_path}, but didn't find it."

    # Check it's pip-installable
    pipinstall = subprocess.run(
        [  # noqa: S603,S607
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
