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
# Q1 — Build Submission Tree
# -------------------------
def build_submission_tree(base_path: str, folder1: str, folder2: str) -> TreeNode:
    """
    Constructs a tree representing the submission directory.
    - Root is the base_path.
    - root.left is folder1, root.right is folder2.
    - Files are linked via .right chains starting at folder.left.
    """
    root = TreeNode(base_path)
    root.left = TreeNode(folder1)
    root.right = TreeNode(folder2)

    # Standard lab file list
    lab_files = ["lab00.py", "lab01.py", "lab02.py", "lab03.py", "autograder_results.json"]

    # Build chain for Folder 1
    if lab_files:
        head1 = TreeNode(lab_files[0])
        current = head1
        for file_name in lab_files[1:]:
            current.right = TreeNode(file_name)
            current = current.right
        root.left.left = head1

    # Build chain for Folder 2
    if lab_files:
        head2 = TreeNode(lab_files[0])
        current = head2
        for file_name in lab_files[1:]:
            current.right = TreeNode(file_name)
            current = current.right
        root.right.left = head2

    return root

# -------------------------
# Q2 — Visit All Nodes Using Tree Traversal
# -------------------------
def print_all_nodes(root: TreeNode) -> None:
    """Prints every node value using the provided preorder traversal."""
    values = preorder(root)
    for value in values:
        print(value)

# -------------------------
# Q3 — Find All Python Files (.py)
# -------------------------
def find_py_files(root: TreeNode) -> list[str]:
    """
    Traverses the tree to find all .py files.
    Returns a list in the format: "folder_name/file_name"
    """
    py_files = []

    def traverse_files(file_node: TreeNode, folder_name: str):
        """Helper to walk the sibling chain of files"""
        if not file_node:
            return
        if file_node.value.endswith(".py"):
            py_files.append(f"{folder_name}/{file_node.value}")
        # Move to the next file in the chain
        traverse_files(file_node.right, folder_name)

    # Start traversal from the file heads of each folder
    if root.left and root.left.left:
        traverse_files(root.left.left, root.left.value)
    
    if root.right and root.right.left:
        traverse_files(root.right.left, root.right.value)

    return py_files
