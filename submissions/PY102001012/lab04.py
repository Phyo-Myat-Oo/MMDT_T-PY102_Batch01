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
    # files under folder1
    lab0 = TreeNode("lab00.py")
    lab1 = TreeNode("lab01.py")
    lab2 = TreeNode("lab02.py")
    lab3 = TreeNode("lab03.py")
    autograde = TreeNode("autograder_results.json")

    lab3.right = autograde
    lab2.right = lab3
    lab1.right = lab2
    lab0.right = lab1

    folder1_node = TreeNode(folder1, left = lab0)

    # files under folder2
    lab0b = TreeNode("lab00.py")
    lab1b = TreeNode("lab01.py")
    lab2b = TreeNode("lab02.py")
    lab3b = TreeNode("lab03.py")
    autogradeb = TreeNode("autograder_results.json")

    lab3b.right = autogradeb
    lab2b.right = lab3b
    lab1b.right = lab2b
    lab0b.right = lab1b

    folder2_node = TreeNode(folder2, left = lab0b)

    root = TreeNode(base_path, left = folder1_node, right = folder2_node)

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
    py_list = []
    for folder_node in [root.left, root.right]:
        file_node = folder_node.left
        while file_node:
            if file_node.value.endswith(".py"):
                py_list.append(folder_node.value + "/" + file_node.value)
            file_node = file_node.right
    return py_list
 