import os

# --- Do not change TreeNode, preorder, inorder, postorder ---
class TreeNode:
    def __init__(self, value: str, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

def preorder(root):
    if not root: return []
    return [root.value] + preorder(root.left) + preorder(root.right)

# -------------------------
# Q1 — Build Submission Tree
# -------------------------
def build_submission_tree(base_path: str, folder1: str, folder2: str) -> TreeNode:
    
    def get_folder_node(folder_name):
        path = os.path.join(base_path, folder_name)
        # Get all files in the folder and sort them
        files = sorted([f.name for f in os.scandir(path) if f.is_file()])
        
        # Simple binary structure: first file on left, second on right
        # (If you have more than 2 files, this links the first two)
        file_left = TreeNode(files[0]) if len(files) > 0 else None
        file_right = TreeNode(files[1]) if len(files) > 1 else None
        
        return TreeNode(folder_name, left=file_left, right=file_right)

    # Root node "submissions" with two folder children
    return TreeNode("submissions", 
                    left=get_folder_node(folder1), 
                    right=get_folder_node(folder2))

# -------------------------
# Q2 — Visit All Nodes
# -------------------------
def print_all_nodes(root: TreeNode) -> None:
    # Use the provided preorder function
    for value in preorder(root):
        print(value)

# -------------------------
# Q3 — Find All Python Files (.py)
# -------------------------
def find_py_files(root: TreeNode) -> list[str]:
    # 1. Get all nodes in a flat list
    all_values = preorder(root)
    
    # 2. Identify the two folder names to track location
    folder_names = {root.left.value, root.right.value}
    py_files = []
    current_folder = ""

    for val in all_values:
        if val in folder_names:
            current_folder = val
        elif val.endswith(".py") and current_folder:
            # Format as "folder/filename.py"
            py_files.append(f"{current_folder}/{val}")

    return py_files

# --- Example Execution ---
if __name__ == "__main__":
    # Path setup: assumes your script is inside a subfolder of 'submissions'
    # Adjust 'base' if your folder structure is different!
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    try:
        my_tree = build_submission_tree(base, "PY102001013", "PY102001015")
        
        print("--- All Nodes (Preorder) ---")
        print_all_nodes(my_tree)
        
        print("\n--- Python Files Found ---")
        print(find_py_files(my_tree))
    except FileNotFoundError:
        print("Error: Ensure the folder names match your actual local directories.")