from pathlib import Path


def test__can_generate_project(project_dir: Path):
    """Test to generate a project using cookiecutter with a specified configuration."""
    assert project_dir.exists()
