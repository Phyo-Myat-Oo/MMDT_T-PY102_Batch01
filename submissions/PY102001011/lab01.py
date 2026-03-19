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
    prev = None
    curr = head
    while curr:
        next_temp = curr.next
        curr.next = prev       
        prev = curr            
        curr = next_temp        
    return prev   
    raise NotImplementedError

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def doubleIt(head):
    if not head:
        return None

    def reverse(node):
        prev = None
        curr = node
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

    rev_head = reverse(head)
    curr = rev_head
    carry = 0
    prev = None

    while curr:
        total = curr.val * 2 + carry
        curr.val = total % 10
        carry = total // 10
        prev = curr
        curr = curr.next

    if carry > 0:
        prev.next = ListNode(carry)

    new_head = reverse(rev_head)
    return new_head
    raise NotImplementedError