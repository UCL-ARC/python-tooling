"""Fixtures for the cookiecutter template tests."""

import pathlib
import subprocess
import typing

import pytest

from .helpers import DEFAULT_CONFIG, _generate_package  # type: ignore[import-not-found]


@pytest.fixture
def generate_package(tmp_path: pathlib.Path) -> typing.Callable:
    """Generate project from cookiecutter template."""

    def wrapped_with_tmp_path(
        config: dict[str, str] = DEFAULT_CONFIG,
    ) -> tuple[subprocess.CompletedProcess, pathlib.Path]:
        return _generate_package(config, tmp_path)

    return wrapped_with_tmp_path
