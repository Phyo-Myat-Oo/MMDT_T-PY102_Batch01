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
    import os
    if not base_path or not folder1 or not folder2:
        raise ValueError("Base path, folder1, and folder2 must be provided.")
    
    root = TreeNode("submissions")
    folder1_node = TreeNode(folder1)
    folder2_node = TreeNode(folder2)
    root.left = folder1_node
    root.right = folder2_node
    def file_chain_tree(files):
        if not files:
            return None
        node = [TreeNode(file) for file in files]
        for i in range(len(node) - 1):
            node[i].right = node[i + 1]
        return node[0] if node else None

    folder1_path = os.path.join(base_path, folder1)
    folder1_files = os.listdir(folder1_path)
    folder1_files = sorted([f for f in folder1_files if os.path.isfile(os.path.join(folder1_path,f))])
    folder1_node.left = file_chain_tree(folder1_files)

    folder2_path = os.path.join(base_path, folder2)
    folder2_files = os.listdir(folder2_path)
    folder2_files = sorted([f for f in folder2_files if os.path.isfile(os.path.join(folder2_path,f))])
    folder2_node.left = file_chain_tree(folder2_files)

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
    if not root:
        return 
    print_value = preorder(root)
    for i in print_value:
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
    if not root:
        return []
    
    py_files = []
    
    def traverse(node, current_path=""):
        if not node:
            return
        
        if node.value == ".gitkeep":
            traverse(node.left, current_path)
            traverse(node.right, current_path)
            return
                
        if node.value.endswith('.py'):
            py_files.append(f"{current_path}/{node.value}")
            traverse(node.left, current_path)
            traverse(node.right, current_path)
            return
                
        new_path = node.value if not current_path else f"{current_path}/{node.value}"
        traverse(node.left, new_path)
        traverse(node.right, new_path)
       
    traverse(root.left)
    traverse(root.right)
    
    return py_files