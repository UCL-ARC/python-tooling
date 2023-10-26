"""Checks that the git repo initialisation works."""

import pathlib
import subprocess

import pytest


@pytest.mark.parametrize(
    "git_init_cookiecutter_option",
    ["initialise_git_repository=True", "initialise_git_repository=False"],
)
def test_initialisation_of_git_repo(
    tmp_path: pathlib.Path, project_config: dict, git_init_cookiecutter_option: str
) -> None:
    """
    Checks to see if git was correctly initialised if desired.

    Args:
        tmp_path: A temporary directory path object which is unique.
        project_config: A dictionary with values for the cookiecutter template,
            as defined in the cookiecutter.json
        git_init_cookiecutter_option: A string defined in cookiecutter.json,
            which determines if git should be initialised or not
    """
    # Run cookiecutter with `initialise_git_repository=False`
    subprocess.run(
        [  # noqa: S603,S607
            "cookiecutter",
            ".",
            "--no-input",
            "--output-dir",
            f"{tmp_path}",
            f"project_name={project_config['project_name']}",
            git_init_cookiecutter_option,
        ],
        check=True,
    )

    test_project_dir = tmp_path / project_config["expected_repo_name"]

    result = subprocess.run(
        [  # noqa: S603,S607
            "git",
            "-C",
            f"{test_project_dir}",
            "status",
        ],
        capture_output=True,
        check=False,
        text=True,
    )

    if "True" in git_init_cookiecutter_option:
        assert result.returncode == 0
    else:
        # should not have found repo
        assert (
            result.stderr
            == "fatal: not a git repository (or any of the parent directories): .git\n"
        )
