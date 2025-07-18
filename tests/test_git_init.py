"""Checks that the git repo initialisation works."""

import subprocess
import typing

import pytest


@pytest.mark.parametrize("init", [True, False])
def test_initialisation_of_git_repo(
    init: bool,  # noqa: FBT001
    default_config_with: typing.Callable,
    generate_package: typing.Callable,
) -> None:
    """Checks to see if git was correctly initialised if desired."""
    # Run cookiecutter with initialise_git_repository
    config = default_config_with("initialise_git_repository", str(init))
    result, test_project_dir = generate_package(config=config)

    # check if git is initialised
    git_status = subprocess.run(  # noqa: S603
        [  # noqa: S607
            "git",
            f"--git-dir={test_project_dir / '.git'}",
            "status",
        ],
        capture_output=True,
        check=False,
        text=True,
    )

    if not init:
        # should not have found git
        assert "fatal: not a git repository" in git_status.stderr
        return  # nothing more to test

    # git status should succeed
    assert git_status.returncode == 0

    try:
        # check for presence of GitHub CLI
        subprocess.run(
            [  # noqa: S607
                "gh",
                "--version",
            ],
            check=True,
            capture_output=True,
        )
        assert (
            "GitHub CLI detected, you can create a repo with the following:\n\n"
            f"gh repo create {config['github_owner']}/"
            f"cookiecutter-test -d "
            f'"{config["project_short_description"]}" --public -r '
            f"origin --source cookiecutter-test" in result.stdout
        )
    except FileNotFoundError:
        # if GitHub CLI isn't installed then instead point to GitHub
        # Note: On GitHub Actions, the CLI is always installed
        # https://docs.github.com/en/actions/using-workflows/using-github-cli-in-workflows
        assert (
            "You now have a local git repository. To sync this to GitHub you "
            "need to create an empty GitHub repo with the name "
            f"{config['github_owner']}/"
            f"cookiecutter-test - DO NOT SELECT ANY "
            "OTHER OPTION.\n\nSee this link for more detail "
            "https://docs.github.com/en/get-started/quickstart/create-a-repo"
            ".\n\nThen run:\n\ngit remote add origin git@github.com:"
            f"{config['github_owner']}/"
            f"cookiecutter-test.git" in result.stdout
        )
