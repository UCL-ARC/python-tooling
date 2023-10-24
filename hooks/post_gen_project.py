"""Post project generation hook."""

import subprocess
import sys


def main() -> int:
    """
    Create a git repository on generation of the project.

    Returns
    -------
        The return code of the process
    """
    cmd = ["git", "init"]
    result = subprocess.run(cmd, check=True)  # noqa: S603
    print(
        "You now have a local git repository. To sync this to GitHub you need "
        "to create an empty GitHub repo with the name "
        "{{cookiecutter.project_slug}} - DO NOT SELECT ANY OTHER OPTION. "
        "Alternatively, if you have the GitHub CLI installed "
        "https://cli.github.com, then you can run "
        "gh repo create {{cookiecutter.project_slug}} -d "
        "{{cookiercutter.description}} --public -r origin --source .",
    )
    return result.returncode


if __name__ == "__main__":
    if "{% cookiecutter.initialise_git_repository %}":
        sys.exit(main())
