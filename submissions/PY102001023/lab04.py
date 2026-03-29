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
    # TODO
    # root
    root = TreeNode(base_path)

    # folder nodes
    folder1_node = TreeNode(folder1)
    folder2_node = TreeNode(folder2)

    # attach folders to root
    root.left = folder1_node
    root.right = folder2_node

    # get files from folder1
    folder1_path = os.path.join(base_path, folder1)
    files1 = os.listdir(folder1_path)

    # add first two files only (binary tree limitation)
    if len(files1) > 0:
        folder1_node.left = TreeNode(files1[0])
    if len(files1) > 1:
        folder1_node.right = TreeNode(files1[1])

    # get files from folder2
    folder2_path = os.path.join(base_path, folder2)
    files2 = os.listdir(folder2_path)

    if len(files2) > 0:
        folder2_node.left = TreeNode(files2[0])
    if len(files2) > 1:
        folder2_node.right = TreeNode(files2[1])

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
    result = preorder(root)   # use given function
    
    for value in result:
        print(value)

def find_py_files(root: TreeNode) -> list[str]:
    result = preorder(root)
    
    py_files = []

    for value in result:
        if value.endswith(".py"):
            py_files.append(value)

    return py_files

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
    result = preorder(root)
    
    py_files = []

    for value in result:
        if value.endswith(".py"):
            py_files.append(value)

    return py_files