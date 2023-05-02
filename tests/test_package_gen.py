import subprocess


def test_package_generation(tmpdir):
    subprocess.run(
        ["cookieninja", ".", "--no-input", "--output-dir", str(tmpdir)]  # noqa: S603,S607
    )

    assert (tmpdir / "python-template").exists()
    expected_files = ["README.md"]
    for f in expected_files:
        assert (tmpdir / "python-template" / f).exists()
