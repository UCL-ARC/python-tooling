"""Post project generation hook."""

import shlex
import subprocess
import sys

_EXIT_FAILURE = 1
_EXIT_SUCCESS = 0


def main(initialise_git_repository: str) -> int:
    """
    Create a git repository on generation of the project.

    Args:
        initialise: Whether to initialise the repo

    Returns:
        The return code of the process
    """
    if initialise_git_repository == "True":
        # initialise git repo
        try:
            subprocess.run(shlex.split("git init"), check=True)  # noqa: S603
            # old versions of git still default to `master`
            subprocess.run(
                shlex.split("git branch -M main"),  # noqa: S603
                check=True,
                capture_output=True,
            )
        except FileNotFoundError:
            print("git isn't installed")  # noqa: T201
            return _EXIT_FAILURE
        except subprocess.CalledProcessError as e:
            print(  # noqa: T201
                f"There was an error with git: {e.returncode}\n{e.stderr}"
            )
            return _EXIT_FAILURE

        # check for presence of GitHub CLI
        try:
            subprocess.run(
                shlex.split("gh --version"),  # noqa: S603
                check=True,
                capture_output=True,
            )
            print(  # noqa: T201
                "GitHub CLI detected, you can create a repo with the following:\n\n"
                "gh repo create {{cookiecutter.github_username}}/"
                "{{cookiecutter.project_slug}} -d "
                "'{{cookiecutter.project_short_description}}' --public -r "
                "origin --source {{cookiecutter.project_slug}}"
            )
        except FileNotFoundError:
            print(  # noqa: T201
                "You now have a local git repository. To sync this to GitHub "
                "you need to create an empty GitHub repo with the name "
                "{{cookiecutter.github_username}}/{{cookiecutter.project_slug}} "
                "- DO NOT SELECT ANY OTHER OPTION.\n\nSee this link for more detail "
                "https://docs.github.com/en/get-started/quickstart/create-a-repo.",
            )
        except subprocess.CalledProcessError as e:
            print(  # noqa: T201
                f"There was an error with the GitHub CLI: {e.returncode}\n{e.stderr}"
            )
            return _EXIT_FAILURE

    return _EXIT_SUCCESS


if __name__ == "__main__":
    sys.exit(main("{{ cookiecutter.initialise_git_repository }}"))
