"""Fixtures for the cookiecutter template tests."""

import pathlib
import subprocess
import typing

import pytest


@pytest.fixture
def default_config() -> dict[str, str]:
    """
    Get the minimal default configuration for cutting a cookie in tests.

    This is used if `generate_package` is called without arguments.
    """
    return {
        "github_owner": "test-user",
        "project_short_description": "description",
        "project_name": "Cookiecutter Test",
        "project_slug": "cookiecutter-test",
    }


@pytest.fixture
def default_config_with(default_config: dict[str, str]) -> typing.Callable:
    """Extend or modify the default configuration with one additional value."""

    def _wrapped_with(key: str, value: str) -> dict[str, str]:
        default_config[key] = value
        return default_config

    return _wrapped_with


def _generate_package(
    config: dict[str, str], path: pathlib.Path
) -> tuple[subprocess.CompletedProcess[str], pathlib.Path]:
    """
    Generate a project from the cookiecutter template.

    Parameters
    ----------
    config
        A dictionary with values for the cookiecutter template,
        as defined in the cookiecutter.json
    path
        Directory to create package in.

    Returns
    -------
    subprocess.CompletedProcess, pathlib.Path
        The result of the cookiecutter command and the path to the generated package.

    """
    args = [f"{key}={val}" for key, val in config.items()]
    cmd = ["cookiecutter", ".", "--no-input", "--output-dir", f"{path}"]
    return subprocess.run(  # noqa: S603
        cmd + args,
        check=False,
        shell=False,
        capture_output=True,
        text=True,
    ), path / config["project_slug"]


@pytest.fixture
def generate_package(
    default_config: dict[str, str], tmp_path: pathlib.Path
) -> typing.Callable:
    """Generate project from cookiecutter template."""

    def _wrapped_with_tmp_path(
        config: dict[str, str] = default_config,
    ) -> tuple[subprocess.CompletedProcess, pathlib.Path]:
        return _generate_package(config, tmp_path)

    return _wrapped_with_tmp_path
