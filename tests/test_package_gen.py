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
    # Run cookieninja with project_slug set to the value in the project config
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
        assert (tmp_path / project_config["project_slug"] / f).exists()

    # Check it's pip-installable
    return_code = subprocess.run(
        [  # noqa: S603,S607
            "python",
            "-m",
            "pip",
            "install",
            "-e",
            tmp_path / project_config["project_slug"],
        ],
        capture_output=True,
    )
    assert return_code == 0, "Something went wrong with intallation"
