# -------------------------
# Do not change the below Code
# -------------------------
import os


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

def build_submission_tree(base_path: str, folder1: str, folder2: str) -> TreeNode:
    """
    base_path: "submissions"
    folder1: name of your folder inside submissions
    folder2: name of your friend's folder inside submissions
    returns: root TreeNode
    """
    # TODO
#    raise NotImplementedError
    root = TreeNode("submissions")
    def folder_node(folder_name: str) -> TreeNode:
        folder_path = os.path.join(base_path, folder_name)
        # Only include files, ignore subfolders
        files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
        folder = TreeNode(folder_name)
        # Attach files as linked nodes (left first, right for siblings)
        current = None
        for f in files:
            node = TreeNode(f)
            if not folder.left:
                folder.left = node
            else:
                current.right = node
            current = node
        return folder

    root.left = folder_node(folder1)
    root.right = folder_node(folder2)
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
    # raise NotImplementedError("Implement Q2 here.")
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
    # raise NotImplementedError("Implement Q3 here.")
    py_files = []

    def helper(node: TreeNode, path: str):
        if not node:
            return
        # Build current path
        current_path = f"{path}/{node.value}" if path else node.value
        # Leaf node ending with .py
        if not node.left and not node.right and node.value.endswith(".py"):
            py_files.append(current_path)
        helper(node.left, current_path)
        helper(node.right, current_path)

    helper(root, "")
    return py_files
if __name__ == "__main__":
    base = "submissions"
    my_id = "PY102001022"
    friend_id = "PY102001020"  # Your friend’s folder

    root = build_submission_tree(base, my_id, friend_id)

    print("All nodes in the submission tree:")
    print_all_nodes(root)

    py_files = find_py_files(root)
    print("\nPython files found:")
    print(py_files)
 