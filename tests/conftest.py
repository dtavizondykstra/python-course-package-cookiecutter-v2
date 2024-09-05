"""
Module configures pytest for the project.

It sets up the necessary paths and plugins for testing.
"""

import sys
from pathlib import Path

THIS_DIR = Path(__file__).parent
TESTS_DIR_PARENT = (THIS_DIR / "../").resolve()

sys.path.insert(0, str(TESTS_DIR_PARENT))

pytest_plugins = [
    "tests.fixtures.project_dir",
]
