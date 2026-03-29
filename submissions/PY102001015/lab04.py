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
    # TODO
    #base_path = os.path.join("MMDT_T-PY102_Batch01", "submissions")

    def get_files_in_folder(folder_name):
        path = os.path.join(base_path, folder_name)
        if os.path.exists(path):
            return [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
        return []

    node1 = get_files_in_folder(folder1)
    n1_left = TreeNode(node1[0]) if len(node1) > 0 else None
    n1_right = TreeNode(node1[1]) if len(node1) > 1 else None
    node_folder1 = TreeNode(folder1, left=n1_left, right=n1_right)

    node2 = get_files_in_folder(folder2)
    n2_left = TreeNode(node2[0]) if len(node2) > 0 else None
    n2_right = TreeNode(node2[1]) if len(node2) > 1 else None
    node_folder2 = TreeNode(folder2, left=n2_left, right=n2_right)

    return TreeNode(base_path, left=node_folder1, right=node_folder2)

    raise NotImplementedError

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
    if not root:
        return
    print(root.value)
    if root.left:
        connector = "├──" if root.right else "└──"
        print(f"{connector}", end="")

        print_all_nodes(root.left)

    if root.right:
        connector = "└──"
        print(f"{connector}", end="")

        print_all_nodes(root.right)
    return
    raise NotImplementedError("Implement Q2 here.")

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
    all_nodes = inorder(root)
    
    python_files = [name for name in all_nodes if name.endswith(".py")]

    return python_files
    raise NotImplementedError("Implement Q3 here.")
 