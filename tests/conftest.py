"""Fixtures for the cookiecutter template tests."""

import pathlib
import subprocess
import typing

import pytest


def _generate_package(
    config: dict[str, str], path: pathlib.Path
) -> subprocess.CompletedProcess[str]:
    """
    Generate a project from the cookiecutter template.

    Arguments:
    ---------
    config: dict
        A dictionary with values for the cookiecutter template,
        as defined in the cookiecutter.json
    path: Path
        Directory to create package in.

    """
    args = [f"{key}={val}" for key, val in config.items()]
    cmd = ["cookiecutter", ".", "--no-input", "--output-dir", f"{path}"]
    return subprocess.run(
        cmd + args,
        check=False,
        shell=False,  # noqa: S603
        capture_output=True,
        text=True,
    )


@pytest.fixture()
def generate_package() -> typing.Callable:
    """Generate project from cookiecutter template."""
    return _generate_package
