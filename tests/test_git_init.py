"""Checks that the git repo initialisation works."""

import pathlib
import subprocess
import typing

import pytest


@pytest.mark.parametrize("initialise_git_repository", [True, False])
def test_initialisation_of_git_repo(
    initialise_git_repository: bool,  # noqa: FBT001
    generate_package: typing.Callable,
    tmp_path: pathlib.Path,
) -> None:
    """Checks to see if git was correctly initialised if desired."""
    test_config = {
        "github_owner": "test-user",
        "project_short_description": "description",
        "project_name": "Cookiecutter Test",
        "initialise_git_repository": initialise_git_repository,
    }
    # Run cookiecutter with initialise_git_repository
    result = generate_package(config=test_config, path=tmp_path)

    test_project_dir = tmp_path / "cookiecutter-test"

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

    if not initialise_git_repository:
        # should not have found git
        assert "fatal: not a git repository" in git_status.stderr
        return  # nothing more to test

    # git status should succeed
    assert git_status.returncode == 0

    try:
        # check for presence of GitHub CLI
        subprocess.run(  # noqa: S603
            [  # noqa: S607
                "gh",
                "--version",
            ],
            check=True,
            capture_output=True,
        )
        assert (
            "GitHub CLI detected, you can create a repo with the following:\n\n"
            f"gh repo create {test_config['github_owner']}/"
            f"cookiecutter-test -d "
            f"\"{test_config['project_short_description']}\" --public -r "
            f"origin --source cookiecutter-test" in result.stdout
        )
    except FileNotFoundError:
        # if GitHub CLI isn't installed then instead point to GitHub
        # Note: On GitHub Actions, the CLI is always installed
        # https://docs.github.com/en/actions/using-workflows/using-github-cli-in-workflows
        assert (
            "You now have a local git repository. To sync this to GitHub you "
            "need to create an empty GitHub repo with the name "
            f"{test_config['github_owner']}/"
            f"cookiecutter-test - DO NOT SELECT ANY "
            "OTHER OPTION.\n\nSee this link for more detail "
            "https://docs.github.com/en/get-started/quickstart/create-a-repo"
            ".\n\nThen run:\n\ngit remote add origin git@github.com:"
            f"{test_config['github_owner']}/"
            f"cookiecutter-test.git" in result.stdout
        )
