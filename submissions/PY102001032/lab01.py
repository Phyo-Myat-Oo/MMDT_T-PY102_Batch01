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
    current = head
    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
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
    reverse_original = reverseList(head)
    
    reverse_crt = reverse_original

    temp_val = 0
    extra_node = False
    while reverse_crt is not None:
        val = reverse_crt.val
        mul_val = val * 2
        if temp_val != 0:
            mul_val = mul_val + temp_val
            temp_val = 0
        if mul_val > 9:
            reverse_crt.val = mul_val % 10
            temp_val = mul_val // 10
            if reverse_crt.next is None:
                extra_node = True
        else:
            reverse_crt.val = mul_val
        # print(reverse_crt.val)
        reverse_crt = reverse_crt.next
        if extra_node is True:
            reverse_original
    

    if extra_node:
        new_node = Node(temp_val)
        reverse_crt = reverse_original
        while reverse_crt.next:
            reverse_crt = reverse_crt.next
        reverse_crt.next = new_node


    result = reverseList(reverse_original)
    return result

        

