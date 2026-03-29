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

def build_submission_tree(base_path: str, folder1: str, folder2: str) -> TreeNode:
    """
    base_path: "submissions"
    folder1: name of your folder inside submissions
    folder2: name of your friend's folder inside submissions
    returns: root TreeNode
    """
    # Create the root node for submission
    root = TreeNode(base_path)

    # Create nodes for two student's folder submission
    # Left Branch (PY102001019)
    f1_node = TreeNode(folder1)
    f1_node.left = TreeNode("lab00.py")
    f1_node.right = TreeNode("lab01.py")

    # Right Branch (PY102001007)
    f2_node = TreeNode(folder2)
    f2_node.left = TreeNode("lab00.py")
    f2_node.right = TreeNode("lab01.py")

    # Attach student folders to the root
    root.left = f1_node
    root.right = f2_node

    return root 

# Initializing with the specific folder names
root_node = build_submission_tree("submissions", "PY102001019", "PY102001007")

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
    nodes = preorder(root)

    for value in nodes:
        print(value)

print_all_nodes(root_node)

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
    Traverse the tree and return a list of all '.py' files 
    formatted as 'foldername/filename.py'.
    """
    python_files = []

    # Helper function for recursion that keeps track of the 'current_folder'
    def traverse(node, current_folder):
        if not node:
            return

        # Check if the node is a student folder 
        if node.value.startswith("PY"):
            new_folder_context = node.value
        else:
            new_folder_context = current_folder

        # If it's a .py file, format it with the current folder context
        if node.value.endswith(".py"):
            if new_folder_context:
                python_files.append(f"{new_folder_context}/{node.value}")
            else:
                python_files.append(node.value)

        # Recurse to children
        traverse(node.left, new_folder_context)
        traverse(node.right, new_folder_context)

    # Start traversal
    traverse(root, None)
    return python_files
