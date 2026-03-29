# -------------------------
# Do not change the below Code
# -------------------------
class TreeNode:
    def __init__(self, value: str, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def preorder(root):
    if not root:
        return []
    return [root.value] + preorder(root.left) + preorder(root.right)


def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.value] + inorder(root.right)


def postorder(root):
    if not root:
        return []
    return postorder(root.left) + postorder(root.right) + [root.value]


# -------------------------

# -------------------------
# Q1 — Build Submission Tree for submissions folder
# Visit our class homework submission repo.
# Look inside the "submissions" folder.
# Pick TWO folders: your folder and your friend's folder (choose with files).
#
# Notes:
# - Ignore any subfolders inside the chosen folders.
# - Only consider FILES inside each chosen folder (each filename becomes a node).
# - Tree structure should be:
#     submissions
#     ├── folder1
#     │   ├── fileA
#     │   └── fileB
#     └── folder2
#         ├── fileC
#         └── fileD
# -------------------------


def build_submission_tree(base_path: str, folder1: str, folder2: str) -> TreeNode:
    """
    base_path: "submissions"
    folder1: name of your folder inside submissions
    folder2: name of your friend's folder inside submissions
    returns: root TreeNode

    submissions
    ├── PY102001009
    │   ├── .gitkeep
    │   │   ├── lab00.py
    │   │   ├── lab01.py
    │   ├── autograder_results.json
    │   │   ├── lab02.py
    │   │   ├── lab03.py
    │── PY102001012
    │   ├── .gitkeep
    │   │   ├── lab00.py
    │   │   ├── lab01.py
    │   ├── autograder_results.json
    │   │   ├── lab02.py
    │   │   ├── lab03.py
    """

    root = TreeNode(base_path)
    folder1_node = TreeNode(folder1)
    folder2_node = TreeNode(folder2)

    root.left = folder1_node
    root.right = folder2_node

    folder1_node.left = TreeNode(".gitkeep")
    folder1_node.right = TreeNode("autograder_results.json")

    folder1_node.left.left = TreeNode("lab00.py")
    folder1_node.left.right = TreeNode("lab01.py")

    folder1_node.right.left = TreeNode("lab02.py")
    folder1_node.right.right = TreeNode("lab03.py")

    folder2_node.left = TreeNode(".gitkeep")
    folder2_node.right = TreeNode("autograder_results.json")

    folder2_node.left.left = TreeNode("lab00.py")
    folder2_node.left.right = TreeNode("lab01.py")

    folder2_node.right.left = TreeNode("lab02.py")
    folder2_node.right.right = TreeNode("lab03.py")

    return root


# -------------------------
# Q2 — Visit All Nodes Using Tree Traversal (Print Everything)
#
# Use the provided traversal function to visit ALL nodes in the tree,
# including:
#   1) the root node: "submissions"
#   2) the two folder nodes
#   3) all file nodes under each folder
#
# Notes:
# - The printing order depends on the traversal you use (preorder, BFS, etc.).
# - You must use the provided traversal function (do not manually recurse).
# - Print exactly the node.value for each visited node.
# -------------------------


def print_all_nodes(root: TreeNode) -> None:
    """
    Traverse the tree and print the value stored in EVERY node.
    root: the TreeNode returned from build_submission_tree
    """
    for value in preorder(root):
        print(value, end=" ")


# -------------------------
# Q3 — Find All Python Files (.py)
#
# Write a function that traverses the tree and returns
# a list of all files ending with ".py".
#
# Notes:
# - Use traversal (do not manually access children).
# - Return a list of strings.
# - The function should NOT print — it should return the list.
# - Example return:
#     ["folderA/file1.py", "folderB/main.py"]
# -------------------------


def find_py_files(root: TreeNode) -> list[str]:
    """
    Traverse the tree and return a list of all '.py' files.
    root: the TreeNode returned from build_submission_tree
    """
    py_files_lst = []
    folder_path = ""

    for node_value in preorder(root):

        if node_value.startswith("PY102"):
            folder_path = node_value

        if node_value.endswith(".py"):
            py_files_lst.append(f"{folder_path}/{node_value}")

    return py_files_lst


"""

def test_build_submission_tree():
    root = build_submission_tree("submissions", "PY102001009", "PY102001012")
    assert root.value == "submissions"

    assert root.left.value == "PY102001009"
    assert root.right.value == "PY102001012"
    assert root.left.left.value == ".gitkeep"
    assert root.left.right.value == "autograder_results.json"
    assert root.left.left.left.value == "lab00.py"
    assert root.left.left.right.value == "lab01.py"
    assert root.left.right.left.value == "lab02.py"
    assert root.left.right.right.value == "lab03.py"
    assert root.right.left.value == ".gitkeep"
    assert root.right.right.value == "autograder_results.json"
    assert root.right.left.left.value == "lab00.py"
    assert root.right.left.right.value == "lab01.py"
    assert root.right.right.left.value == "lab02.py"
    assert root.right.right.right.value == "lab03.py"


def test_print_all_nodes():
    root = build_submission_tree("submissions", "PY102001009", "PY102001012")

    print()
    print("test_print_all_nodes")
    print_all_nodes(root)


def test_find_py_files():
    root = build_submission_tree("submissions", "PY102001009", "PY102001012")
    py_files = find_py_files(root)
    expected_files = [
        "PY102001009/lab00.py",
        "PY102001009/lab01.py",
        "PY102001009/lab02.py",
        "PY102001009/lab03.py",
        "PY102001012/lab00.py",
        "PY102001012/lab01.py",
        "PY102001012/lab02.py",
        "PY102001012/lab03.py",
    ]

    print()
    print("py_files")
    print(py_files)
    # print("=" * 100)

    print("expected_files")
    print(expected_files)
    # print("=" * 100)

    assert sorted(py_files) == sorted(expected_files)


def main() -> None:

    # test_build_submission_tree()

    root_node = build_submission_tree("submissions", "PY102001009", "PY102001012")

    # print("=" * 100)
    # print("print_all_nodes")
    # print_all_nodes(root_node)
    # print("=" * 100)

    # test_print_all_nodes()

    find_py_files(root_node)

    test_find_py_files()

    print("All tests passed!")


if __name__ == "__main__":
    main()

"""
