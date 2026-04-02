# -------------------------
# Do not change the below Code
# -------------------------
from typing import Optional, List

class TreeNode:
    def __init__(self, value: int, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.value] + inorder(root.right)

def print_all_nodes(root: TreeNode|None):
    if root is None:
        return
    for value in inorder(root):
        print(value)

def height(root):
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))

# ------------------------------------------------------------
# Q1 — sorted_array_to_bst
# ------------------------------------------------------------
# Given a sorted array nums (ascending order),
# build and return a height-balanced BST.
#
# Requirements:
# - Choose the middle element as the root.
# - Use Python integer division:
#       mid = (left + right) // 2
# - Recursively build left and right subtrees.
# ------------------------------------------------------------
"""
_build(0,6) -> mid=3 -> node 3
|
|-- left: _build(0,2) -> mid=1 -> node 1
|   |
|   |-- left: _build(0,0) -> mid=0 -> node 0
|   |   |
|   |   |-- left:  _build(0,-1) -> None
|   |   |-- right: _build(1,0)  -> None
|   |   |
|   |   `-- return node 0
|   |
|   |-- right: _build(2,2) -> mid=2 -> node 2
|   |   |
|   |   |-- left:  _build(2,1) -> None
|   |   |-- right: _build(3,2) -> None
|   |   |
|   |   `-- return node 2
|   |
|   `-- return node 1
|
|-- right: _build(4,6) -> mid=5 -> node 5
|   |
|   |-- left: _build(4,4) -> mid=4 -> node 4
|   |   |
|   |   |-- left:  _build(4,3) -> None
|   |   |-- right: _build(5,4) -> None
|   |   |
|   |   `-- return node 4
|   |
|   |-- right: _build(6,6) -> mid=6 -> node 6
|   |   |
|   |   |-- left:  _build(6,5) -> None
|   |   |-- right: _build(7,6) -> None
|   |   |
|   |   `-- return node 6
|   |
|   `-- return node 5
|
`-- return node 3

        3
      /   \
     1     5
    / \   / \
   0   2 4   6

"""

def _build(nums: List[int], left: int, right: int):
    if left > right:
        return None

    mid = (left + right) // 2
    root_value = nums[mid]
    root = TreeNode(root_value)

    left_subtree = _build(nums, left, mid - 1)
    right_subtree = _build(nums, mid + 1, right)

    root.left = left_subtree
    root.right = right_subtree

    return root



def sorted_array_to_bst(nums: List[int]) -> Optional[TreeNode]:
   new_tree_root = _build(nums, 0, len(nums) - 1)
   return new_tree_root

# ------------------------------------------------------------
# Q2 — insert_bst
# ------------------------------------------------------------
# Write a function insert_bst(root, value) that inserts
# a value into a Binary Search Tree (BST).
#
# Requirements:
# - If root is None, create and return a new TreeNode.
# - If value < root.value, insert into the left subtree.
# - If value > root.value, insert into the right subtree.
# - Do NOT allow duplicate values.
# - Return the root of the tree after insertion.
# ------------------------------------------------------------

def insert_bst(root: Optional[TreeNode], value: int):
    if root is None:
        return TreeNode(value)
    if value < root.value:
        root.left = insert_bst(root.left, value)
    elif value > root.value:
        root.right = insert_bst(root.right, value)
    return root

# ------------------------------------------------------------
# Q3 — BST in real life application
# ------------------------------------------------------------
# In this course, each student has a PY102 ID (e.g., 1001, 1002, ...).
#
# Task:
# 1) Create a list of consecutive PY102 IDs for your group.
#    Example: if init_id = 1001 and num_stus = 6,
#    then the list should be:
#        [1001, 1002, 1003, 1004, 1005, 1006]
#
# 2) Use your sorted_array_to_bst(nums) function from Q1
#    to build a height-balanced BST from this list.
#
# 3) Then, insert additional out-of-order IDs
#    (if any) using your insert_bst(root, value) function from Q2.
#
# 4) Print all nodes of the final BST using provided function.
#
# 5) Print the max possible iterations to search a student id in your final BST. 
# ------------------------------------------------------------

def build_class_bst():
    init_id = 1001
    num_stus = 6
    nums = list(range(init_id, init_id + num_stus))
    root = sorted_array_to_bst(nums)
    additional_ids = [1037, 1018, 1011]
    for student_id in additional_ids:
        root = insert_bst(root, student_id)
    print_all_nodes(root)
    print(height(root))
    return root
