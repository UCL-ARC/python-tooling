"""Checks that the git repo initialisation works."""

import pathlib
import subprocess

import pytest

from .helpers import gen_package


@pytest.mark.parametrize(
    "git_init_cookiecutter_option",
    ["True", "False"],
)
def test_initialisation_of_git_repo(
    tmp_path: pathlib.Path,
    git_init_cookiecutter_option: str,
) -> None:
    """Checks to see if git was correctly initialised if desired."""
    config = {
        "github_username": "test-user",
        "project_short_description": "description",
        "project_name": "Cookiecutter Test",
        "initialise_git_repository": git_init_cookiecutter_option,
    }
    # Run cookiecutter with initialise_git_repository
    result = gen_package(tmp_path, config)

    test_project_dir = tmp_path / "cookiecutter-test"

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
            assert (
                "GitHub CLI detected, you can create a repo with the following:\n\n"
                f"gh repo create {config['github_username']}/"
                f"cookiecutter-test -d "
                f"'{config['project_short_description']}' --public -r "
                f"origin --source cookiecutter-test" in result.stdout
            )
        except FileNotFoundError:
            # if GitHub CLI isn't installed then instead point to GitHub
            # Note: On GitHub Actions, the CLI is always installed
            # https://docs.github.com/en/actions/using-workflows/using-github-cli-in-workflows
            assert (
                "You now have a local git repository. To sync this to GitHub you "
                "need to create an empty GitHub repo with the name "
                f"{config['github_username']}/"
                f"cookiecutter-test - DO NOT SELECT ANY "
                "OTHER OPTION.\n\nSee this link for more detail "
                "https://docs.github.com/en/get-started/quickstart/create-a-repo"
                ".\n\nThen run:\n\ngit remote add origin git@github.com:"
                f"{config['github_username']}/"
                f"cookiecutter-test.git" in result.stdout
            )
    else:
        # should not have found git
        assert (
            git_status.stderr
            == "fatal: not a git repository (or any of the parent directories): .git\n"
        )
