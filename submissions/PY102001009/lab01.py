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

    previous = None
    current = head
    while current is not None:
        next = current.next
        current.next = previous
        previous = current
        current = next

    return previous


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

    if head is None:
        return None

    # Reverse list
    head = reverseList(head)

    carry = 0
    current = head

    # Double digits
    while current:
        total = current.val * 2 + carry
        current.val = total % 10
        carry = total // 10

        # If at last node and carry remains, append new node
        if current.next is None and carry:
            current.next = Node(carry)
            carry = 0
            break

        current = current.next

    # Reverse back
    return reverseList(head)


# Testing reverseList with the example:

n1 = Node(1)

ll_lst = SinglyLinkedList(n1)
lst = ll_lst.to_list()

lst.append(2)
lst.append(3)
lst.append(4)
lst.append(5)

n2 = ll_lst.from_list(lst)
reverse_node = reverseList(n2.head)
reversed_list = SinglyLinkedList(reverse_node)
rev_lst = reversed_list.to_list()

print(lst)
print(rev_lst)


# Testing doubleIt with the example:

node_9 = Node(9)
sll_lst = SinglyLinkedList(node_9)
lst = sll_lst.to_list()

lst.append(9)
lst.append(9)

node = sll_lst.from_list(lst)
double_node = doubleIt(node.head)

sll_double_list = SinglyLinkedList(double_node)
double_list = sll_double_list.to_list()

print(lst)
print(double_list)
