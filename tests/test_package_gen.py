import pathlib as pl
import subprocess

PROJECT_SLUG = "cookiecutter_test"


def test_package_generation(tmpdir):
    # Run cookieninja with PROJECT_SLUG for project_slug
    subprocess.run(
        [  # noqa: S607
            "cookieninja",
            ".",
            "--no-input",
            "--output-dir",
            str(tmpdir),
            "project_slug=",
            PROJECT_SLUG,
        ],
        shell=False,  # noqa: S603
    )

    # Check parent directory of the repo exists
    assert (tmpdir / "python-template").exists()

    # Check files and directories inside
    expected_files = [
        "README.md",
        ".pre-commit-config.yaml",
        # "LICENSE",
        "pyproject.toml",
        # Directories
        pl.Path("src") / PROJECT_SLUG,
        "tests",
        pl.Path(".github"),
        pl.Path(".github") / "workflows",
    ]
    for f in expected_files:
        assert (tmpdir / "python-template" / PROJECT_SLUG / f).exists()
