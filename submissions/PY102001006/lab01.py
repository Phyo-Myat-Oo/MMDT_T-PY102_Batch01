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
    
    current = head
    prev = None
    
    while current is not None:
        NextNode = current.next

        current.next = prev

        prev = current

        current = NextNode
    
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
    head = reverseList(head)

    carry = 0
    current = head

    while current:
        total = current.val * 2 + carry
        current.val = total % 10
        carry = total // 10

        if not current.next and carry:
            current.next = Node(carry)
            break

        current = current.next
        
    return reverseList(head)
    




