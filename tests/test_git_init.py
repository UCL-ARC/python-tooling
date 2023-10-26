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
    # Run cookiecutter with initialise_git_repository
    cookie = subprocess.run(
        [  # noqa: S603,S607
            "cookiecutter",
            ".",
            "--no-input",
            "--output-dir",
            f"{tmp_path}",
            f"github_username={project_config['github_username']}",
            f"project_name={project_config['project_name']}",
            f"project_short_description={project_config['project_short_description']}",
            git_init_cookiecutter_option,
        ],
        capture_output=True,
        check=True,
        text=True,
    )

    test_project_dir = tmp_path / project_config["expected_repo_name"]

    # check if git is initialised
    git_status = subprocess.run(
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
        # git status should succeed
        assert git_status.returncode == 0

        try:
            # check for presence of GitHub CLI
            subprocess.run(
                [  # noqa: S603,S607
                    "gh",
                    "--version",
                ],
                check=True,
                capture_output=True,
            )
            # ensure GitHub CLI is printed
            assert (
                cookie.stdout
                == f"Initialized empty Git repository in {test_project_dir}/.git/\n"
                "GitHub CLI detected, you can create a repo with the following:\n\n"
                f"gh repo create {project_config['github_username']}/"
                f"{project_config['expected_repo_name']} -d "
                f"'{project_config['project_short_description']}' --public -r "
                f"origin --source {project_config['expected_repo_name']}\n"
            )
        except FileNotFoundError:
            # if GitHub CLI isn't installed then instead point to GitHub
            # Note: On GitHub Actions, the CLI is always installed
            # https://docs.github.com/en/actions/using-workflows/using-github-cli-in-workflows
            assert (
                cookie.stdout
                == f"Initialized empty Git repository in {test_project_dir}/.git/\n"
                "You now have a local git repository. To sync this to GitHub you "
                "need to create an empty GitHub repo with the name "
                f"{project_config['github_username']}/"
                f"{project_config['expected_repo_name']} - DO NOT SELECT ANY "
                "OTHER OPTION.\n\nSee this link for more detail "
                "https://docs.github.com/en/get-started/quickstart/create-a-repo"
                ".\n\nThen run:\n\ngit remote add origin git@github.com:"
                f"{project_config['github_username']}/"
                f"{project_config['expected_repo_name']}.git\n"
            )
    else:
        # should not have found git
        assert (
            git_status.stderr
            == "fatal: not a git repository (or any of the parent directories): .git\n"
        )
