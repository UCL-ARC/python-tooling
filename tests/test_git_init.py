"""Checks that the git repo initialisation works."""

import pathlib
import subprocess


def test_git_not_initialised(
    tmp_path: pathlib.Path,
    project_config: dict,
) -> None:
    """
    Checks for the case without git initialisation.

    Args:
        tmp_path: A temporary directory path object which is unique.
        project_config: A dictionary with values for the cookiecutter template,
            as defined in the cookiecutter.json
    """
    # Run cookiecutter with `initialise_git_repository=False`
    subprocess.run(
        [  # noqa: S603,S607
            "cookiecutter",
            ".",
            "--no-input",
            "--output-dir",
            str(tmp_path),
            f"project_name={project_config['project_name']}",
            "initialise_git_repository=False",
        ],
        check=True,
    )

    test_project_dir = tmp_path / project_config["expected_repo_name"]

    result = subprocess.run(
        ["git", "-C", str(test_project_dir), "status"],  # noqa: S603,S607
        capture_output=True,
        check=False,
        text=True,
    )
    assert (
        result.stderr
        == "fatal: not a git repository (or any of the parent directories): .git\n"
    ), f"Error: {result.stderr!r}"


def test_git_initialised(
    tmp_path: pathlib.Path,
    project_config: dict,
) -> None:
    """
    Checks for the case with git initialisation.

    Args:
        tmp_path: A temporary directory path object which is unique.
        project_config: A dictionary with values for the cookiecutter template,
            as defined in the cookiecutter.json
    """
    # Run cookiecutter with `initialise_git_repository=True`
    subprocess.run(
        [  # noqa: S603,S607
            "cookiecutter",
            ".",
            "--no-input",
            "--output-dir",
            str(tmp_path),
            f"project_name={project_config['project_name']}",
            "initialise_git_repository=True",
        ],
        check=True,
        capture_output=True,
    )

    test_project_dir = tmp_path / project_config["expected_repo_name"]

    result = subprocess.run(
        ["git", "-C", str(test_project_dir), "status"],  # noqa: S603,S607
        capture_output=True,
        check=False,
        text=True,
    )
    assert result.returncode == 0, f"Error: {result.stderr!r}"
