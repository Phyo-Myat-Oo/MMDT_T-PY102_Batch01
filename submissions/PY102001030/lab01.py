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
    curr = head
    
    while curr:
        # 1. Save the next node (so we don't lose it)
        nxt = curr.next
        
        # 2. Reverse the pointer
        curr.next = prev
        
        # 3. Step forward: current becomes previous, 
        #    and we move to the next node we saved earlier
        prev = curr
        curr = nxt
        
    # At the end, curr is None and prev is the new head
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
    

    head = reverseList(head)
    
    curr = head
    carry = 0
    prev_node = None
    #multiply its value by 2 and add any carry from the previous node's multiplication
    while curr:
        new_val = (curr.val * 2) + carry
        curr.val = new_val % 10    
        carry = new_val // 10      
        prev_node = curr
        curr = curr.next
     #If there is a final carry remaining at the front, add a new Node
    if carry:
        prev_node.next = Node(carry)
     #Reverse the result one more time to restore it to the original format.
    return reverseList(head)


