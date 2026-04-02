# -------------------------
# Do not change the below Code
# -------------------------
class TreeNode:
    def __init__(self, value: str, left = None, right = None):
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
import os
def build_submission_tree(base_path: str, folder1: str, folder2: str) -> TreeNode:
    """
    base_path: "submissions"
    folder1: name of your folder inside submissions
    folder2: name of your friend's folder inside submissions
    returns: root TreeNode
    """
    # building root
    root = TreeNode(base_path)

    # folder nodes
    f1_root = TreeNode(folder1)
    f2_root = TreeNode(folder2)

    root.left = f1_root
    root.right = f2_root


    
    f1_path = os.path.join(base_path, folder1)
    f2_path = os.path.join(base_path, folder2)

    files1 = [f for f in os.listdir(f1_path)
              if os.path.isfile(os.path.join(f1_path, f))]

    files2 = [f for f in os.listdir(f2_path)
              if os.path.isfile(os.path.join(f2_path, f))]


    # attach files to folder1
    # prev = None
    for f in files1[:2]:
        node = TreeNode(f)
        if not f1_root.left:
            f1_root.left = node   # first child
        else:
            f1_root.right = node     # next sibling
        # prev = node
    # attach files to folder2
    # prev = None
    for f in files2[:2]:
        node = TreeNode(f)
        if not f2_root.left:
            f2_root.left = node
        else:
            f2_root.right = node
        # prev = node

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
        print(value) 


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
    result = []
    values = preorder(root)
    curr_folder1 = root.left.value
    curr_folder2 = root.right.value
    curr_folder = None

    for value in values:
        if curr_folder1 == value or curr_folder2 == value:
            curr_folder = value
        elif value.endswith('.py') and curr_folder is not None:
            result.append(f"{curr_folder}/{value}")
    return result





# tree = build_submission_tree("submissions", "PY102001003", "PY102001004")
    
# print_all_nodes(tree)

# print(find_py_files(tree))
