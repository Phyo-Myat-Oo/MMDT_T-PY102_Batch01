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

    def get_files(path):
        only_file=[]
        if not os.path.exists(path):
            return []

        all_items=os.listdir(path)
        for item in all_items:
            full_path = os.path.join(path,item)
            if os.path.isfile(full_path):
                only_file.append(item)
        return only_file


    def build_file_nodes(files):
        if not files:
            return None

        root = TreeNode(files[0])
        current = root

        for f in files[1:]:
            current.right=TreeNode(f)
            current=current.right

        return root

    files1 = get_files(os.path.join(base_path, folder1))
    files2 = get_files(os.path.join(base_path, folder2))

    node_folder1 = TreeNode(folder1, left = build_file_nodes(files1))
    node_folder2 = TreeNode(folder2, left = build_file_nodes(files2))

    return TreeNode(base_path, left=node_folder1, right=node_folder2)

    # raise NotImplementedError

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

    node = preorder(root)
    for value in node:
        print(value)

    #raise NotImplementedError("Implement Q2 here.")

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

    result=[]
    node=preorder(root)
    curr_folder=""
    
    for value in node:
        if "." not in value:
            curr_folder=value
        elif value.endswith(".py"):
            result.append(f"{curr_folder}/{value}")

    return result

    # raise NotImplementedError("Implement Q3 here.")
 