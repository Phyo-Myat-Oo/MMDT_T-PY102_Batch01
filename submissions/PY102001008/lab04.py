# -------------------------
# Q1 — Build Submission Tree
# -------------------------
def build_submission_tree(base_path: str, folder1: str, folder2: str) -> TreeNode:
   
    lab0 = TreeNode("lab00.py")
    lab1 = TreeNode("lab01.py")
    lab2 = TreeNode("lab02.py")
    lab3 = TreeNode("lab03.py")
    
  
    lab2.right = lab3
    lab1.right = lab2
    lab0.right = lab1
    folder1_node = TreeNode(folder1, left = lab0)


    lab0b = TreeNode("lab00.py")
    lab1b = TreeNode("lab01.py")
    lab2b = TreeNode("lab02.py")
    lab3b = TreeNode("lab03.py")

    lab2b.right = lab3b
    lab1b.right = lab2b
    lab0b.right = lab1b
    folder2_node = TreeNode(folder2, left = lab0b)


    return TreeNode(base_path, left = folder1_node, right = folder2_node)

# -------------------------
# Q2 — Visit All Nodes (Print Everything)
# -------------------------
def print_all_nodes(root: TreeNode) -> None:
 
    for value in preorder(root):
        print(value)

# -------------------------
# Q3 — Find All Python Files (.py)
# -------------------------
def find_py_files(root: TreeNode) -> list[str]:
    """
    Returns a list of strings in 'folder/file.py' format.
    """
    py_list = []
    for folder_node in [root.left, root.right]:
        if folder_node:
         folder node
            file_node = folder_node.left
            while file_node:
                if file_node.value.endswith(".py"):
                    py_list.append(folder_node.value + "/" + file_node.value)
                file_node = file_node.right
    return py_list
