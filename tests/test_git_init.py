"""Checks that the git repo initialisation works."""

import pathlib
import subprocess


def test_git_not_initialised(
    tmp_path: pathlib.Path,
    project_config: dict,
):
    """ """
    # Run cookiecutter with project_slug set to the value in the project config
    subprocess.run(
        [  # noqa: S603,S607
            "cookiecutter",
            ".",
            "--no-input",
            "--output-dir",
            str(tmp_path),
            "initialise_git_repository=false",
            f"project_name={project_config['project_name']}",
        ],
        check=False,
    )

    test_project_dir = tmp_path / project_config["expected_repo_name"]

    result = subprocess.run(
        ["git", "-C", str(test_project_dir), "status"],  # noqa: S603,S607
        capture_output=True,
        check=False,
    )
    assert (
        result.returncode != 0
        and result.stderr
        == b"fatal: not a git repository (or any of the parent directories): .git\n"
    ), "git initialised when it shouldn't be"
