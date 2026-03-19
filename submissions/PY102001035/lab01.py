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
    prev = None
    crt = head
    while crt is not None:
        next_node = crt.next
        crt.next = prev
        prev = crt
        crt = next_node
    return prev
    # TODO: Implement
    raise NotImplementedError

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
    new_head = reverseList(head)

    carry = 0
    crt = new_head
    prev = None

    while crt is not None:
        total = crt.val * 2 + carry
        crt.val = total % 10
        carry = total // 10

        prev = crt
        crt = crt.next
    
    if carry:
        prev.next = Node(carry)
    
    head = reverseList(new_head)

    return head

    # TODO: Implement
    raise NotImplementedError

def showStrValue(head):
    crt = head
    number = 0
    while crt:
        number = number * 10 + crt.val
        crt = crt.next
    return number

if __name__ == "__main__":
    s1 = SinglyLinkedList.from_list([1,2,3,4,5])
    print("Original List:", s1.to_list())

    new_head = reverseList(s1.head)
    print("Reverse List:", SinglyLinkedList(new_head).to_list())

    s2 = SinglyLinkedList.from_list([9,9,9])
    print("Before List:", s2.to_list())

    new_head1 = doubleIt(s2.head)
    print("After doubleIt:", SinglyLinkedList(new_head1).to_list())
    print("DoubleIt value:", showStrValue(new_head1))