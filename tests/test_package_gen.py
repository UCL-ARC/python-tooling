"""Checks that the cookiecutter works."""

import pathlib
import subprocess


def test_package_generation(
    tmp_path: pathlib.Path,
    project_config: dict,
):
    """
    Creates a project from the cookiecutter template.

    Once the project is made it verifies a series of files and
    directories exist.

    Args:
    ----
        tmp_path: Path
            A temporary directory path object which is unique.
        project_config: dict
            A dictionary with values for the cookiecutter template,
            as defined in the cookiecutter.json

    Note that 'tmp_path' pytest fixture is preferred over 'tmpdir'
    (see https://docs.pytest.org/en/7.3.x/how-to/tmp_path.html#the-tmpdir-and-tmpdir-factory-fixtures)
    """
    # Run cookiecutter with project_slug set to the value in the project config
    subprocess.run(
        [  # noqa: S607
            "cookiecutter",
            ".",
            "--no-input",
            "--output-dir",
            f"{tmp_path}",
            f"project_name='{project_config['project_name']}'",
        ],
        check=False,
        shell=False,  # noqa: S603
    )

    # Check project directory exists
    test_project_dir = tmp_path / project_config["expected_repo_name"]
    assert test_project_dir.exists()

    # Check main files and directories inside
    expected_files = [
        "README.md",
        ".pre-commit-config.yaml",
        "LICENSE.md",
        "pyproject.toml",
        "src",
        pathlib.Path("src") / project_config["expected_package_name"],
        pathlib.Path("src") / project_config["expected_package_name"] / "__init__.py",
        "tests",
        pathlib.Path(".github"),
        pathlib.Path(".github") / "workflows",
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
            f"{test_project_dir}",
        ],
        capture_output=True,
        check=False,
    )
    assert (
        pipinstall.returncode == 0
    ), f"Something went wrong with installation: {pipinstall.stderr!r}"
