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
    root = TreeNode("submissions")
    def folder_node(folder_name):
        folder_path = os.path.join(base_path, folder_name)

        # get the files under folder
        files = [
            f for f in os.listdir(folder_path)
            if os.path.isfile(os.path.join(folder_path, f)) and not f.startswith('.')
        ]

        files.sort()

        # linking the files
        head = None
        current = None

        for file in files:
            node = TreeNode(file)
            if head is None:
                head = node
                current = node
            else:
                current.right = node
                current = node

        return TreeNode(folder_name, left=head)

    # building folder nodes
    f1 = folder_node(folder1)
    f2 = folder_node(folder2)

    # connecting folders
    root.left = f1
    f1.right = f2

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
    current_folder = None

    for value in preorder(root):
        if value == "submissions":
            continue

        elif "." not in value:
            current_folder = value

        elif value.endswith(".py"):
            result.append(f"{current_folder}/{value}")

    return result

 
