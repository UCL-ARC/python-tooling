"""Post project generation hook."""

import subprocess
import sys

_EXIT_FAILURE = 1
_EXIT_SUCCESS = 0


def main(initialise_git_repository: str, deploy_docs_to_github_pages: str) -> int:
    """
    Create a git repository on generation of the project.

    Args:
        initialise_git_repository: Whether to initialise the repo
        deploy_docs_to_github_pages: Whether to deploy built docs to GitHub Pages

    Returns:
        The return code of the process

    """
    if initialise_git_repository == "True":
        try:
            # initialise git repo
            subprocess.run(
                [  # noqa: S603,S607
                    "git",
                    "init",
                ],
                check=True,
            )
            # old versions of git still default to `master`
            subprocess.run(
                [  # noqa: S603,S607
                    "git",
                    "branch",
                    "-M",
                    "main",
                ],
                check=True,
                capture_output=True,
            )
        except FileNotFoundError:
            # cannot find git
            print("git isn't installed")
            return _EXIT_FAILURE
        except subprocess.CalledProcessError as e:
            # some other error
            print(f"There was an error with git: {e.returncode}\n{e.stderr}")
            return _EXIT_FAILURE

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
            print(
                "GitHub CLI detected, you can create a repo with the following:\n\n"
                "gh repo create "
                "{{cookiecutter.github_username}}/{{cookiecutter.project_slug}} "
                '-d "{{cookiecutter.project_short_description}}" '
                "--public "
                "-r origin "
                "--source {{cookiecutter.project_slug}}\n"
            )
        except FileNotFoundError:
            # GitHub CLI isn't installed
            print(
                "You now have a local git repository. To sync this to GitHub "
                "you need to create an empty GitHub repo with the name "
                "{{cookiecutter.github_username}}/{{cookiecutter.project_slug}} "
                "- DO NOT SELECT ANY OTHER OPTION.\n\nSee this link for more detail "
                "https://docs.github.com/en/get-started/quickstart/create-a-repo.\n\n"
                "Then run:\n\n"
                "git remote add origin git@github.com:"
                "{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}.git\n"
            )
        except subprocess.CalledProcessError as e:
            # some other error
            print(f"There was an error with the GitHub CLI: {e.returncode}\n{e.stderr}")
            return _EXIT_FAILURE
    if deploy_docs_to_github_pages == "True":
        print(
            "The 'Documentation' GitHub Actions workflow has been set up to push the "
            "built HTML documentation to a branch gh-pages on pushes to main for "
            "deploying as a GitHub Pages website. To allow the GitHub Actions bot to "
            "push to the gh-pages branch you need to enable 'Read and write "
            "permissions' under 'Workflow permissions' at\n\n"
            "https://github.com/{{cookiecutter.github_username}}/"
            "{{cookiecutter.project_slug}}/settings/actions\n\n"
            "After the 'Documentation' workflow has successfully completed at least "
            "once you will also need to configure the repository to deploy a GitHub "
            "pages site from the content on the gh-pages branch by going to\n\n"
            "https://github.com/{{cookiecutter.github_username}}/"
            "{{cookiecutter.project_slug}}/settings/pages\n\n"
            "and under 'Built and deployment' selecting 'Deploy from a branch' for "
            "the 'Source' drop-down and 'gh-pages' for the 'Branch' drop-down, "
            "leaving the branch path drop-down with its default value of '/ (root)'."
        )

    return _EXIT_SUCCESS


if __name__ == "__main__":
    sys.exit(
        main(
            "{{ cookiecutter.initialise_git_repository }}",
            "{{ cookiecutter.deploy_docs_to_github_pages }}",
        )
    )
