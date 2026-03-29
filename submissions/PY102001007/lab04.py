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
# ------------------------


def build_submission_tree(base_path: str, folder1: str, folder2: str) -> TreeNode:
    root = TreeNode("submissions")

    folder_node1 = TreeNode(folder1)
    folder_node2 = TreeNode(folder2)

    root.left = folder_node1
    root.right = folder_node2

    #  folder1 
    path1 = os.path.join(base_path, folder1)
    files1 = os.listdir(path1)

    file_nodes1 = []
    for file in files1:
        full_path = os.path.join(path1, file)
        if os.path.isfile(full_path):
            file_nodes1.append(TreeNode(file))

    
    if file_nodes1:
        folder_node1.left = file_nodes1[0]
        current = folder_node1.left
        for i in range(1, len(file_nodes1)):
            current.right = file_nodes1[i]
            current = current.right

    # folder2
    path2 = os.path.join(base_path, folder2)
    files2 = os.listdir(path2)

    file_nodes2 = []
    for file in files2:
        full_path = os.path.join(path2, file)
        if os.path.isfile(full_path):
            file_nodes2.append(TreeNode(file))

    if file_nodes2:
        folder_node2.left = file_nodes2[0]
        current = folder_node2.left
        for i in range(1, len(file_nodes2)):
            current.right = file_nodes2[i]
            current = current.right

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
    values = preorder(root)
    for v in values:
        print(v)


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
    result = []

    def helper(node, current_folder):
        if not node:
            return

        # if node is a folder has children and not root
        if (node.left or node.right) and node.value != "submissions":
            current_folder = node.value

        # if node is a python file
        if node.value.endswith(".py"):
            result.append(current_folder + "/" + node.value)

        helper(node.left, current_folder)
        helper(node.right, current_folder)

    helper(root, "")
    return result