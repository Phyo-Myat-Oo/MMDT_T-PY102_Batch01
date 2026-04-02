# -------------------------
# Do not change the below Code
# -------------------------
from typing import Optional, List
import random

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

def _build(nums: List[int], left: int, right: int):
    if left > right:
        return None
    mid = (left + right) // 2
    root = TreeNode(nums[mid])
    root.left = _build(nums, left, mid-1)
    root.right = _build(nums, mid+1, right)
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
        root = TreeNode(value)
    if value == root.value:
        return root
    elif value < root.value:
        root.left = insert_bst(root.left, value)
    else:
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
    nums = [init_id + k for k in range(num_stus)]
    
    root = sorted_array_to_bst(nums)

    new_order_ids = [1037, 1023, 1041]
    for id_val in new_order_ids:
        if id_val not in nums:
            root = insert_bst(root, id_val)

    print_all_nodes(root)
    print(height(root))