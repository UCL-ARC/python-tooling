"""Checks that the cookiecutter works."""

import subprocess
from pathlib import Path


def test_package_generation(tmpdir: Path):
    """
    Creates a project cookiecutter from the template.

    Once the project is made it verifies a series of actions work.

    Args:
    ----
        tmpdir: A temporary directory path object which is unique.
    """
    subprocess.run(["cookieninja", ".", "--no-input", "--output-dir", str(tmpdir)])

    assert (tmpdir / "python-template").exists()
    expected_files = ["README.md"]
    for f in expected_files:
        assert (tmpdir / "python-template" / f).exists()
