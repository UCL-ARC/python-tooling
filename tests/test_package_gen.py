import pathlib as pl
import subprocess

PROJECT_SLUG = "cookiecutter_test"


def test_package_generation(tmp_path):
    # tmp_path fixture preferred over tmpdir
    # see https://docs.pytest.org/en/7.3.x/how-to/tmp_path.html#the-tmpdir-and-tmpdir-factory-fixtures

    # Run cookieninja with PROJECT_SLUG for project_slug
    subprocess.run(
        [  # noqa: S607
            "cookieninja",
            ".",
            "--no-input",
            "--output-dir",
            str(tmp_path),
            f"project_slug={PROJECT_SLUG}",
        ],
        shell=False,  # noqa: S603
    )

    # Check parent directory exists
    assert (tmp_path / PROJECT_SLUG).exists()

    # Check files and directories inside
    expected_files = [
        "README.md",
        ".pre-commit-config.yaml",
        # "LICENSE",
        "pyproject.toml",
        # Directories
        "src",
        pl.Path("src") / PROJECT_SLUG,
        "tests",
        pl.Path(".github"),
        pl.Path(".github") / "workflows",
    ]
    for f in expected_files:
        assert (tmp_path / PROJECT_SLUG / f).exists()
