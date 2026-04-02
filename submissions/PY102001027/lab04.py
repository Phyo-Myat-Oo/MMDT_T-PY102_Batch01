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

       # base_path = "submissions"
    # folder1 = "PY102001027"
    # folder2 = "PY102001025"

    #files under folder 1
    file_a = TreeNode("lab00.py")
    file_b = TreeNode("lab01.py")
    file_c = TreeNode("lab02.py")
    file_a.right = file_b
    file_b.right = file_c

    #files under folder 1
    file_d = TreeNode("lab00.py")
    file_e = TreeNode("lab01.py")
    file_f = TreeNode("lab02.py")
    file_d.right = file_e
    file_e.right = file_f

    node_folder1 = TreeNode (folder1)
    node_folder1.left = file_a

    node_folder2 = TreeNode (folder2)
    node_folder2.left = file_d

    root = TreeNode(base_path, left = node_folder1, right = node_folder2)
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
    print_values= preorder(root)
    for val in print_values:
        print(val)


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
    find_result = []
    values =   preorder(root)
    current_folder= ""
    for v in values:
        if  not v.endswith(".py") and "." not in v and v!= root.value:
            current_folder = v
        elif v.endswith(".py") and current_folder:
            find_result.append(f"{current_folder}/{v}")
    return find_result
 
