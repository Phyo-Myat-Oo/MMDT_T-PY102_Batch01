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
    # define vars
    root = TreeNode(base_path)
    root.left = TreeNode(folder1)
    root.right = TreeNode(folder2)

    import os

    # link all files in f1
    path1 = os.path.join(base_path, folder1)
    f1_files = [f for f in os.listdir(path1) if os.path.isfile(os.path.join(path1, f))]

    next = None
    for i, file in enumerate(f1_files):
        node = TreeNode(file)

        if i == 0:
            root.left.left = node
        else:
            next.right = node       

        next = node

    # link all files in f2
    path2 = os.path.join(base_path, folder2)
    f2_files = [f for f in os.listdir(path2) if os.path.isfile(os.path.join(path2, f))]

    next = None
    for i, file in enumerate(f2_files):
        node = TreeNode(file)

        if i == 0:
            root.right.left = node
        else:
            next.right = node

        next = node

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
    tree = postorder(root)

    for v in tree:
        print(v.value)

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
    # use preorder
    all_nodes = preorder(root)
    out_list = []

    # set curr folder to none
    curr_f = ""

    for node in all_nodes:
        # print (f"node val is {node}")
        
        if node != root.value and "." not in node:
            curr_f = node.split("\\")[-1]
        elif node.endswith(".py"):
            out_list.append(curr_f + "/" + node)

    return out_list
        
 

# # test case
# startf = r"D:\mmdt\MMDT_T-PY102_Batch01\submissions"
# leftf = r"D:\mmdt\MMDT_T-PY102_Batch01\submissions\PY102001041"
# rightf = r"D:\mmdt\MMDT_T-PY102_Batch01\submissions\PY102001042"

# main_tree = build_submission_tree(startf, leftf, rightf)
# print (main_tree)


# print(preorder(main_tree))

# print ("preorder printing DoneQ!\n")
# print(find_py_files(main_tree))
