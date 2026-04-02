import importlib.util
import os
from pathlib import Path
import math
import pytest

def load_lab05():
    student_dir = os.environ.get("STUDENT_DIR")
    assert student_dir, "STUDENT_DIR env var not set"

    lab_path = Path(student_dir) / "lab05.py"
    assert lab_path.exists(), f"Missing file: {lab_path}"

    spec = importlib.util.spec_from_file_location("student_lab05", lab_path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.mark.points(5)
def test_q1_sorted_array_to_bst_inorder_correct():
    m = load_lab05()
    assert hasattr(m, "sorted_array_to_bst"), "Missing function: sorted_array_to_bst(nums)"
    assert hasattr(m, "inorder"), "Missing function: inorder(root)"

    nums = [-10, -3, 0, 5, 9]
    root = m.sorted_array_to_bst(nums)
    assert m.inorder(root) == nums

    nums2 = [1]
    root2 = m.sorted_array_to_bst(nums2)
    assert m.inorder(root2) == nums2

    nums3 = [1, 2]
    root3 = m.sorted_array_to_bst(nums3)
    assert m.inorder(root3) == nums3


@pytest.mark.points(5)
def test_q2_sorted_array_to_bst_middle_index_rule():
    """
    Enforces the lab rule:
      mid = (left + right) // 2
    which makes the construction deterministic.
    """
    m = load_lab05()
    assert hasattr(m, "sorted_array_to_bst"), "Missing function: sorted_array_to_bst(nums)"

    nums = [-10, -3, 0, 5, 9]
    root = m.sorted_array_to_bst(nums)
    assert root is not None
    assert root.value == 0

    assert root.left is not None
    assert root.left.value == -10

    nums_even = [1, 2, 3, 4]
    root_even = m.sorted_array_to_bst(nums_even)
    assert root_even is not None
    assert root_even.value == 2


@pytest.mark.points(5)
def test_q3_insert_bst_inserts_and_ignores_duplicates():
    m = load_lab05()
    assert hasattr(m, "TreeNode"), "Missing class: TreeNode"
    assert hasattr(m, "insert_bst"), "Missing function: insert_bst(root, value)"
    assert hasattr(m, "inorder"), "Missing function: inorder(root)"

    root = None
    root = m.insert_bst(root, 10)
    root = m.insert_bst(root, 5)
    root = m.insert_bst(root, 15)
    root = m.insert_bst(root, 10)  # duplicate (should be ignored)

    assert m.inorder(root) == [5, 10, 15]

    root = m.insert_bst(root, 12)
    assert m.inorder(root) == [5, 10, 12, 15]


@pytest.mark.points(5)
def test_q4_build_class_bst_inorder_and_height():
    m = load_lab05()
    assert hasattr(m, "build_class_bst"), "Missing function: build_class_bst()"
    assert hasattr(m, "inorder"), "Missing function: inorder(root)"
    assert hasattr(m, "height"), "Missing function: height(root)"

    root = m.build_class_bst()
    values = m.inorder(root)
    n = len(values)

    assert n > 0
    assert values == sorted(values)

    h = m.height(root)
    max_ok = math.ceil(math.log2(n)) + 1
    assert h <= max_ok, f"Tree height too large: got {h}, expected <= {max_ok} for n={n}"

