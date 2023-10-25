"""Post project generation hook."""

import logging
import subprocess
import sys

import colorama


def main(initialise_git_repository: str) -> int:
    """
    Create a git repository on generation of the project.

    Args:
        initialise: Whether to initialise the repo

    Returns:
        The return code of the process
    """
    if initialise_git_repository == "True":
        # initialise git repository and ensure on `main` branch`
        try:
            subprocess.run(["git", "init"], check=True)  # noqa: S603,S607
            # old versions of git still default to `master`
            subprocess.run(
                ["git", "branch", "-M", "main"],  # noqa: S603,S607
                check=True,
            )
        except subprocess.CalledProcessError:
            logging.error(f"{colorama.Fore.RED}git not installed")
            return 1

        # create GitHub repo with CLI if possible
        try:
            logging.info(
                f"{colorama.Fore.GREEN}GitHub CLI found, creating a remote",
            )
            subprocess.run(
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
                check=True,
            )
        except FileNotFoundError:
            logging.error(
                f"{colorama.Fore.RED}You now have a local git repository. To "
                "sync this to GitHub you need to create an empty GitHub repo "
                "with the name {{cookiecutter.project_slug}} - DO NOT SELECT "
                "ANY OTHER OPTION. See this link for more detail ",
                "https://docs.github.com/en/get-started/quickstart/create-a-repo.",
            )
            return 2
    return 0


if __name__ == "__main__":
    sys.exit(main("{{ cookiecutter.initialise_git_repository }}"))
