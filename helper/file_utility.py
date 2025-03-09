import os
from pathlib import Path

PROJECT_ROOT = str(Path(__file__).parent.parent)
API_SCHEMA = os.path.join(PROJECT_ROOT, "tests", "api", "schema")