"""Checks that the cookiecutter works."""

import subprocess
from pathlib import Path


def test_package_generation(
    tmp_path: Path,
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
            str(tmp_path),
            f"project_slug={project_config['project_slug']}",
        ],
        check=False,
        shell=False,  # noqa: S603
    )

    test_project_dir = tmp_path / project_config["project_slug"]

    # Check parent directory exists
    assert test_project_dir.exists()

    # Check main files and directories inside parent directory
    expected_files = [
        "README.md",
        ".pre-commit-config.yaml",
        "LICENCE.md",
        "pyproject.toml",
        "src",
        Path("src") / project_config["project_slug"],
        "tests",
        Path(".github"),
        Path(".github") / "workflows",
    ]
    for f in expected_files:
        assert (test_project_dir / f).exists()

    # Need a .git directory in the project root
    subprocess.run(["git", "init", test_project_dir], check=False)  # noqa: S603,S607

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
    ), f"Something went wrong with intallation: {pipinstall.stderr!r}"
