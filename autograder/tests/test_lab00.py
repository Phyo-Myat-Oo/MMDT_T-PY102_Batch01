import os
import importlib.util
from pathlib import Path
import re
import pytest

def load_lab00():
    student_dir = os.environ.get("STUDENT_DIR")
    assert student_dir, "STUDENT_DIR environment variable is not set"

    lab00 = Path(student_dir) / "lab00.py"
    assert lab00.exists(), "lab00.py not found in your submission folder"

    spec = importlib.util.spec_from_file_location("lab00", lab00)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module


def test_submission_check_exists():
    m = load_lab00()
    assert hasattr(m, "submission_check"), "Function submission_check() not found"


def test_submission_check_returns_string():
    m = load_lab00()
    result = m.submission_check()
    assert isinstance(result, str), "submission_check() must return a string"


def test_submission_check_not_placeholder():
    m = load_lab00()
    result = m.submission_check()
    assert result != "REPLACE_WITH_YOUR_STUDENT_ID", (
        "You must replace the placeholder with your actual student ID"
    )

@pytest.mark.points(1)
def test_submission_check_format():
    m = load_lab00()
    result = m.submission_check()
    assert re.fullmatch(r"PY102001\d{3}", result), (
        "Student ID must match format PY102001XXX"
    )
