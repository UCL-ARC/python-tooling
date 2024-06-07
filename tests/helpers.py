"""Checks that the cookiecutter works."""

import pathlib
import subprocess


def gen_package(
    path: pathlib.Path, project_config: dict[str, str]
) -> subprocess.CompletedProcess[str]:
    """
    Generate project from cookiecutter template.

    Arguments:
    ---------
    path: Path
        Directory to create pacakge in.
    project_config: dict
        A dictionary with values for the cookiecutter template,
        as defined in the cookiecutter.json

    """
    args = [f"{key}={val}" for key, val in project_config.items()]
    cmd = ["cookiecutter", ".", "--no-input", "--output-dir", f"{path}"]
    return subprocess.run(
        cmd + args,
        check=False,
        shell=False,  # noqa: S603
        capture_output=True,
        text=True,
    )
