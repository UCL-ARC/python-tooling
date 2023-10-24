"""Post project generation hook."""

import subprocess


def main() -> None:
    """Create a git repository on generation of the project."""
    cmd = ["git", "init"]
    subprocess.run(cmd, check=True)  # noqa: S603


if __name__ == "__main__":
    main()
