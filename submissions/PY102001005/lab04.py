import os
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
    
    def build_file_subtree(file_names: list[str]) -> TreeNode | None:
        if not file_names:
            return None

        middle = len(file_names) // 2
        return TreeNode(
            file_names[middle],
            build_file_subtree(file_names[:middle]),
            build_file_subtree(file_names[middle + 1:]),
        )

    def build_folder_node(folder_name: str) -> TreeNode:
        folder_path = os.path.join(base_path, folder_name)
        file_names = []

        with os.scandir(folder_path) as entries:
            for entry in entries:
                if entry.is_file():
                    file_names.append(entry.name)

        file_names.sort()
        folder_node = TreeNode(folder_name)

        if not file_names:
            return folder_node

        split_index = (len(file_names) + 1) // 2
        folder_node.left = build_file_subtree(file_names[:split_index])
        folder_node.right = build_file_subtree(file_names[split_index:])

        print(f"Built folder node for '{folder_name}' with files: {file_names}")

        return folder_node

    return TreeNode(
        os.path.basename(os.path.normpath(base_path)),
        build_folder_node(folder1),
        build_folder_node(folder2),
    )

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
    values = preorder(root)   

    for value in values:
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
    values = preorder(root)
    py_files = []
    folder_names = {root.left.value, root.right.value}
    current_folder = ""

    for value in values[1:]:
        if value in folder_names:
            current_folder = value
        elif value.endswith(".py"):
            py_files.append(f"{current_folder}/{value}")

    return py_files

#if __name__ == "__main__":
    # current_dir = os.path.dirname(os.path.abspath(__file__))
    # print("Current Directory:", current_dir)
    # submissions_dir = os.path.dirname(current_dir)
    # print("Submissions Directory:", submissions_dir)
    # my_folder = os.path.basename(current_dir)
    # friend_folder = "PY102001006"

    # if not os.path.isdir(os.path.join(submissions_dir, friend_folder)):
    #     for entry in sorted(os.scandir(submissions_dir), key=lambda item: item.name):
    #         if entry.is_dir() and entry.name != my_folder:
    #             friend_folder = entry.name
    #             break

    # tree = build_submission_tree(submissions_dir, my_folder, friend_folder)
    # print("Preorder:", preorder(tree))
    # print("Inorder:", inorder(tree))
    # print("Postorder:", postorder(tree))

    # base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # print("base_path:", base_path)
    # print_all_nodes(build_submission_tree(base_path, "PY102001005", "PY102001006"))

    # base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # print(find_py_files(build_submission_tree(base_path, "PY102001005", "PY102001006")))