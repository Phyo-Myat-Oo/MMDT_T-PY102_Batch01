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

    curr = head
    prev = None

    while curr is not None:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    
    return prev

# lst = SinglyLinkedList.from_list([1,2,3,4,5])

# reversed_head = reverseList(lst.head)

# reversed_lst = SinglyLinkedList(reversed_head)
# print(reversed_lst.to_list())

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

    r_lst = reverseList(head)
    curr = r_lst
    carry = 0

    dummy = Node(0)
    tail = dummy
    while curr is not None:
        dcurr = curr.val * 2 + carry
        if dcurr >= 10:
            digit = dcurr-10
            carry = 1
        else:
            digit = dcurr
            carry = 0
        tail.next = Node(digit)
        tail = tail.next
        curr = curr.next
    if carry == 1:
        tail.next = Node(carry)
    
    return reverseList(dummy.next)

# lst = SinglyLinkedList.from_list([9,9,9])

# doubled_head = doubleIt(lst.head)

# doubled_lst = SinglyLinkedList(doubled_head)
# print(doubled_lst.to_list())


