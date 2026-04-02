# -------------------------
# Do not change the below Code
# -------------------------
class TreeNode:
    def __init__(self, value: str, left=None, right=None):
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
# -------------------------

def build_submission_tree(base_path: str, folder1: str, folder2: str) -> TreeNode:
    """
    base_path: "submissions"
    folder1: name of your folder inside submissions (PY102001007)
    folder2: name of your friend's folder inside submissions (PY102001037)
    returns: root TreeNode
    """
    # Create root node
    root = TreeNode(base_path)
    
    # Create and attach folder nodes
    root.left = TreeNode(folder1)
    root.right = TreeNode(folder2)
    
    # For folder1 - create files using a loop
    lab_files = ["lab00.py", "lab01.py", "lab02.py", "lab03.py", "autograder_results.json"]
    
    # Build chain from first to last
    current = None
    for file_name in reversed(lab_files):
        file_node = TreeNode(file_name)
        file_node.right = current
        current = file_node
    
    root.left.left = current
    
    # For folder2 - create files using a different approach (building forward)
    lab_files2 = ["lab00.py", "lab01.py", "lab02.py", "lab03.py", "autograder_results.json"]
    
    # Build chain forward
    head = TreeNode(lab_files2[0])
    current_node = head
    for file_name in lab_files2[1:]:
        current_node.right = TreeNode(file_name)
        current_node = current_node.right
    
    root.right.left = head
    
    return root

# -------------------------
# Q2 — Visit All Nodes Using Tree Traversal (Print Everything)
# -------------------------

def print_all_nodes(root: TreeNode) -> None:
    """
    Traverse the tree and print the value stored in EVERY node.
    root: the TreeNode returned from build_submission_tree
    """
    values = preorder(root)
    for value in values:
        print(value)

# -------------------------
# Q3 — Find All Python Files (.py)
# -------------------------

def find_py_files(root: TreeNode) -> list[str]:
    """
    Traverse the tree and return a list of all '.py' files.
    root: the TreeNode returned from build_submission_tree
    """
    py_files = []
    
    def traverse_files(file_node: TreeNode, folder_name: str):
        """Traverse through the chain of files starting from file_node"""
        if not file_node:
            return
        
        if file_node.value.endswith(".py"):
            py_files.append(f"{folder_name}/{file_node.value}")
        
        traverse_files(file_node.right, folder_name)
    
    if root.left and root.left.left:
        traverse_files(root.left.left, root.left.value)
    
    if root.right and root.right.left:
        traverse_files(root.right.left, root.right.value)
    
    return py_files