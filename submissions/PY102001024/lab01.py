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
    crt = head
    while crt is not None:
        next_node = crt.next
        crt.next = prev
        prev = crt
        crt = next_node

    return prev
    #raise NotImplementedError

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

    # Step 1: Reverse list
    head = reverseList(head)

    carry = 0
    curr = head

    # Step 2: Double digits
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

    # Step 3: Reverse back
    return reverseList(head)


    #raise NotImplementedError

node1 = Node(1)
sList = SinglyLinkedList(node1)
list1 = sList.to_list()

list1.append(2)
list1.append(3)
list1.append(4)
list1.append(5)
print("List 1 : ",list1)

node2 = sList.from_list(list1)
print("node2 : ", node2)

reverseNode = reverseList(node2.head)
reversed_list = SinglyLinkedList(reverseNode)
list2 = reversed_list.to_list()
print(list2)



node3 = Node(1)
sList3 = SinglyLinkedList(node3)
list3 = sList3.to_list()

list3.append(8)
list3.append(9)
print("List 3 : ",list3)

node4 = sList3.from_list(list3)
doubleNode = doubleIt(node4.head)

print("Double : ",doubleNode)

sll_double_list = SinglyLinkedList(doubleNode)
double_list = sll_double_list.to_list()
print(double_list)
