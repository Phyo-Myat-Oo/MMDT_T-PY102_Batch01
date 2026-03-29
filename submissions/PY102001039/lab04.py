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
    
    root = TreeNode(base_path)
    folder1 = TreeNode(folder1)
    folder2 = TreeNode(folder2)

    root.left = folder1
    root.right = folder2

    folder1.left = TreeNode(".gitkeep")
    folder1.right = TreeNode("autograder_results.json")
    folder1.left.left = TreeNode("lab00.py")
    folder1.left.right = TreeNode("lab01.py")
    folder1.right.left = TreeNode("lab02.py")
    folder1.right.right = TreeNode("lab03.py")

    folder2.left = TreeNode(".gitkeep")
    folder2.right = TreeNode("autograder_results.json")
    folder2.left.left = TreeNode("lab00.py")
    folder2.left.right = TreeNode("lab01.py")
    folder2.right.left = TreeNode("lab02.py")
    folder2.right.right = TreeNode("lab03.py")

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
    res = preorder(root)
    for i in res:
        print(i)

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
    lst = []
    parent = ""
    res = preorder(root)
    for i in res:
        if(i.startswith("PY102")):
            parent = i

        if(i.endswith(".py")):
            lst.append(f"{parent}/{i}")
    return sorted(lst)

# base_path = "submissions"
# folder1 = "PY102001039"
# folder2 = "PY102001004"
# tree = build_submission_tree(base_path, folder1, folder2)
# print(tree)

# print_all_nodes(tree)

# python_files = find_py_files(tree)
# print(python_files)
