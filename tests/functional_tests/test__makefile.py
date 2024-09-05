import subprocess
from pathlib import Path


def test__linting_passes(project_dir: Path):
    """Check that linting passes in the project directory."""
    subprocess.run(["make", "lint-ci"], cwd=project_dir, check=True)


def test__tests_pass(project_dir: Path):
    """Check that tests pass in the project directory."""
    subprocess.run(["make", "install"], cwd=project_dir, check=True)
    subprocess.run(["make", "test-wheel-locally"], cwd=project_dir, check=True)
