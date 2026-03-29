import importlib.util
import os
from pathlib import Path
import pytest

def load_lab04():
    student_dir = os.environ.get("STUDENT_DIR")
    assert student_dir, "STUDENT_DIR env var not set"

    lab_path = Path(student_dir) / "lab04.py"
    assert lab_path.exists(), f"Missing file: {lab_path}"

    spec = importlib.util.spec_from_file_location("student_lab04", lab_path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

@pytest.mark.points(6)
def test_q1_build_submission_tree():
    lab04 = load_lab04()

    root = lab04.build_submission_tree("submissions", "PY102001001", "PY102001002")

    assert root is not None
    assert root.value == "submissions"
    assert root.left is not None
    assert root.right is not None
    assert root.left.value.startswith("PY102001")
    assert root.right.value.startswith("PY102001")

    cur = root.left.left
    count = 0
    while cur is not None:
        assert cur.left is None
        count += 1
        cur = cur.right
    assert count >= 1

    cur = root.right.left
    count = 0
    while cur is not None:
        assert cur.left is None
        count += 1
        cur = cur.right
    assert count >= 1


@pytest.mark.points(7)
def test_q2_print_all_nodes(capsys):
    lab04 = load_lab04()

    base_path = "submissions"
    root = lab04.build_submission_tree(base_path, "PY102001001", "PY102001002")

    lab04.print_all_nodes(root)
    printed = [ln.strip() for ln in capsys.readouterr().out.splitlines() if ln.strip()]
    pre = lab04.preorder(root)
    ino = lab04.inorder(root)
    post = lab04.postorder(root)
    assert printed in (pre, ino, post)
    
@pytest.mark.points(7)
def test_q3_find_py_files():
    lab04 = load_lab04()

    base_path = "submissions"
    root = lab04.build_submission_tree(base_path, "PY102001001", "PY102001002")

    result = lab04.find_py_files(root)

    assert isinstance(result, list)

    for item in result:
        assert str(item).endswith(".py")



 



