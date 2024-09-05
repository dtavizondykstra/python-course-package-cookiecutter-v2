import shutil
import subprocess
from pathlib import Path
from typing import Generator
from uuid import uuid4

import pytest

from tests.utils.project import (
    generate_project,
    initialize_git_repo,
)


@pytest.fixture(scope="session")
def project_dir() -> Generator[Path, None, None]:
    test_session_id: str = generate_test_session_id()
    template_values = {
        "repo_name": f"pytest-repo-{test_session_id}",
    }
    generated_repo_name: Path = generate_project(template_values=template_values, test_session_id=test_session_id)
    try:
        initialize_git_repo(repo_dir=generated_repo_name)
        subprocess.run(["make", "lint-ci"], cwd=generated_repo_name, check=False)
        yield generated_repo_name
    finally:
        shutil.rmtree(path=generated_repo_name)
        subprocess.run(["make", "clean"], check=False)

def generate_test_session_id() -> str:
    test_session_id = str(uuid4())[:6]
    return test_session_id
