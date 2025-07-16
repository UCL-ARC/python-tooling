"""Helper functions for the cookiecutter template tests."""

import os
import pathlib
import subprocess

DEFAULT_CONFIG = {
    "github_owner": "test-user",
    "project_short_description": "description",
    "project_name": "Cookiecutter Test",
    "project_slug": "cookiecutter-test",
}


def _generate_package(
    config: dict[str, str], path: pathlib.Path
) -> tuple[subprocess.CompletedProcess[str], pathlib.Path]:
    """
    Generate a project from the cookiecutter template.

    Arguments:
    ---------
    config: dict
        A dictionary with values for the cookiecutter template,
        as defined in the cookiecutter.json
    path: Path
        Directory to create package in.

    Returns:
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


def get_all_files_folders(root_path: pathlib.Path) -> set[pathlib.Path]:
    """
    Get all files and folders under a directory.

    The paths are returned relative to the root path given.
    __pycache__ directories and .DS_Store files are ignored.
    """
    file_set: set[pathlib.Path] = set()
    for dirpath, _, filenames in os.walk(root_path):
        dirpath_path = pathlib.Path(dirpath).relative_to(root_path)
        if dirpath_path.name in ["__pycache__"]:
            continue

        # Add this directory
        file_set.update((dirpath_path,))
        # Add any files in it
        for filename in filenames:
            if filename in [".DS_Store"]:
                continue
            file_set.update((dirpath_path / filename,))

    return file_set
