"""
Lab 02 — Stack & Queue Practice (4 Questions)

Rules:
- Do NOT use input() or print() in your solutions.
- Implement the functions below exactly with the given names.
- Use stack/queue operations (append/pop for stack; collections.deque for queue is recommended).

Questions:
  Q1) is_balanced_parentheses(s)
  Q2) next_greater_to_right(nums)

  Q3) first_non_repeating(stream)
  Q4) hot_potato(names, k)
"""

from collections import deque


# -------------------------
# Stack Questions (2)
# -------------------------

def is_balanced_parentheses(s: str) -> bool:
    """
    Return True if the string s has balanced brackets: (), {}, [].
    Ignore non-bracket characters.

    Examples:
      is_balanced_parentheses("([]){}") -> True
      is_balanced_parentheses("(]") -> False
      is_balanced_parentheses("a+(b*c)-{d/e}") -> True
    """
    pair_check = { ")": "(", "}": "{", "]": "["}
    stack = []

    for char in s:
        if char in "({[":
            stack.append(char)
        elif char in pair_check:
            if not stack or stack [-1] != pair_check[char]:
                return False
            stack.pop()
    return len(stack) == 0

    # TODO: implement using a stack
    raise NotImplementedError


def next_greater_to_right(nums: list[int]) -> list[int]:
    """
    For each element, find the next greater element to its right.
    If none exists, output -1 for that position.

    Example:
      nums = [2, 1, 2, 4, 3]
      output -> [4, 2, 4, -1, -1]
    """
    greater_element = [-1]*len(nums)
    stack = []

    for i, num in enumerate(nums):
        while stack and nums[stack[-1]] < num:
            idx = stack.pop()
            greater_element[idx] = num
        stack.append(i)
    return greater_element

    # TODO: implement using a stack (monotonic stack)
    raise NotImplementedError


# -------------------------
# Queue Questions (2)
# -------------------------

def first_non_repeating(stream: str) -> str:
    """
    Given a stream of lowercase letters, build a result string where each character
    is the first non-repeating character seen so far. If none exists, use '#'.

    Example:
      stream = "aabc"

      Process step by step:
      a → 'a'   # 'a' appears once, so it is the first non-repeating character
      a → '#'   # 'a' now appears twice; no character appears once, so use '#'
      b → 'b'   # 'b' appears once and is the first non-repeating character
      c → 'b'   # 'a' repeats, 'b' appears once, 'c' appears once;
                # 'b' appeared earlier than 'c', so output 'b'

      Output: "a#bb"
    """
    queue = deque()
    count = {}
    result =""
    for char in stream:
        count [char] = count.get(char,0)+1
        queue.append(char)

        while queue and count[queue[0]]>1:
            queue.popleft()
        
        result += queue[0] if queue else "#"
    return result

    # TODO: implement using a queue + counts
    raise NotImplementedError


def hot_potato(names: list[str], k: int) -> str:
    """
    Simulate the Hot Potato game.

    - names is a list of players in initial order.
    - The potato starts with the first person in the list.
    - Pass the potato exactly k times in a circular manner.
    - After the k-th pass, eliminate the person holding the potato.
    - The person immediately after the eliminated player
      (in circular order) holds the potato next.
    - Continue until one player remains. Return the winner's name.

    Example:
      names = ["A", "B", "C", "D"]
      k = 2
      1st round: 
      - "A"--> "B-->C
      - C is eliminated. 
      - Remaining: ["A", "B", "D"]
      - Next HOlder: "D"
      2nd round:
      - "D" --> "A" --> "B"
      - B is eliminated
      - Remaining: ["D", "A"]
      3rd round: 
      - "D"--> "A" --> "D"
      - D is eliminated. 

     Winner: "A"

    """
    queue = deque (names)
    while len(queue)>1:
        for _ in range(k):
            queue.append(queue.popleft())
        queue.popleft()      
    return queue[0]

    # TODO: implement using a queue (deque)
    raise NotImplementedError


# print(is_balanced_parentheses("([]){}"))         
# print(is_balanced_parentheses("(]"))             
# print(is_balanced_parentheses("a+(b*c)-{d/e}"))  
# print(next_greater_to_right([2, 1, 2, 4, 3]))   
# print(first_non_repeating("aabc"))               
# print(hot_potato(["A", "B", "C", "D"], 2))       