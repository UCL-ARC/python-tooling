"""Post project generation hook."""

import logging
import subprocess
import sys

_EXIT_FAILURE = 1
_EXIT_SUCCESS = 0
_logger = logging.getLogger(__name__)
_logger.setLevel("ERROR")


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
            subprocess.run(["git", "init"], check=True)  # noqa: S603,S607
            # old versions of git still default to `master`
            subprocess.run(["git", "branch", "-M", "main"], check=True)  # noqa: S603,S607
        except FileNotFoundError:
            _logger.error("git isn't installed")
            return _EXIT_FAILURE
        except subprocess.CalledProcessError as e:
            _logger.error(f"There was an error with git: {e.returncode}\n{e.stderr}")
            return _EXIT_FAILURE

        # create GitHub repo with CLI if possible
        try:
            github_cli = subprocess.run(
                [  ## noqa: S603,S607
                    "gh",
                    "repo",
                    "create",
                    "{{cookiecutter.project_slug}}",
                    "-d",
                    "'{{cookiecutter.project_short_description}}'",
                    "--public",
                    "-r",
                    "origin",
                    "--source",
                    ".",
                ],
                capture_output=True,
                check=True,
                text=True,
            )
            _logger.info(f"GitHub CLI created a repo at {github_cli.stdout}")
        except FileNotFoundError:
            _logger.info(
                "You now have a local git repository. To sync this to GitHub "
                "you need to create an empty GitHub repo with the name "
                "{{cookiecutter.project_slug}} - DO NOT SELECT ANY OTHER "
                "OPTION. See this link for more detail "
                "https://docs.github.com/en/get-started/quickstart/create-a-repo.",
            )
        except subprocess.CalledProcessError as e:
            _logger.error(
                f"There was an error with the GitHub CLI: {e.returncode}\n{e.stderr}"
            )
            return _EXIT_FAILURE

    return _EXIT_SUCCESS


if __name__ == "__main__":
    sys.exit(main("{{ cookiecutter.initialise_git_repository }}"))
