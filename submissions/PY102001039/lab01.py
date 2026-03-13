"""
Lab01.py — Linked List Lab (Auto-graded)

Covers:
- LeetCode 206: Reverse Linked List
- LeetCode 2816: Double a Number Represented as a Linked List

Lab format:
- Node classes are defined separately from LinkedList wrappers.

Student instructions:
- Do NOT change required function names/signatures.
- You MAY add helper functions/methods.
- Use pointer manipulation (don’t solve by converting the whole list to an int or Python list).
"""

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next 


class SinglyLinkedList:
    def __init__(self, head=None):
        self.head = head

    @classmethod
    def from_list(cls, values):
        head = None
        tail = None
        for v in values:
            node = Node(v)
            if head is None:
                head = node
                tail = node
            else:
                assert tail is not None
                tail.next = node
                tail = node
        return cls(head)

    def to_list(self):
        result = []
        curr = self.head
        while curr:
            result.append(curr.val)
            curr = curr.next
        return result


# ============================================================
#  REQUIRED FUNCTIONS (Implement these)
# ============================================================

def reverseList(head):
    """
    LeetCode 206 — Reverse Linked List
    Reverse a singly linked list and return the new head.
    Time: O(n), Space: O(1)
    """
    # TODO: Implement
    prev = None
    curr = head
    while curr is not None:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    return prev

def doubleIt(head):
    """
    LeetCode 2816 — Double a Number Represented as a Linked List

    Digits are stored in forward order (most significant digit first).
    Return the head of a new list (or reuse nodes) representing 2x the number.

    Examples:
      1 -> 8 -> 9   (189)  =>  3 -> 7 -> 8  (378)
      9 -> 9 -> 9   (999)  =>  1 -> 9 -> 9 -> 8  (1998)

    Requirements:
    - Use linked-list operations/pointer logic.
    - Avoid converting the entire list into an integer/string for the core solution.
    """

    # TODO: Implement
    if head is None:
        return None

    # Reverse list
    head = reverseList(head)

    carry = 0
    curr = head

    # Double digits
    while curr:
        total = curr.val * 2 + carry
        curr.val = total % 10
        carry = total // 10

        # If at last node and carry remains, append new node
        if curr.next is None and carry:
            curr.next = Node(carry)
            carry = 0
            break

        curr = curr.next

    # Reverse back
    return reverseList(head)

node_1 = Node(1)

sll_list = SinglyLinkedList(node_1)
list_1 = sll_list.to_list()

list_1.append(2)
list_1.append(3)
list_1.append(4)
list_1.append(5)

node_2 = sll_list.from_list(list_1)

reverse_node = reverseList(node_2.head)
reversed_list = SinglyLinkedList(reverse_node)
list_2 = reversed_list.to_list()
print(list_2)

###################################################

node_3 = Node(9)
sll_list_2 = SinglyLinkedList(node_3)
list_3 = sll_list_2.to_list()

list_3.append(9)
list_3.append(9)

node_4 = sll_list_2.from_list(list_3)
double_node = doubleIt(node_4.head)

sll_double_list = SinglyLinkedList(double_node)
double_list = sll_double_list.to_list()
print(double_list)
