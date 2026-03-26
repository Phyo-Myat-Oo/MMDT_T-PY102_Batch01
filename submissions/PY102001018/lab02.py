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
    # TODO: implement using a stack
    # start the empty stack list 
    
    pair_dict = {')':'(', '}':'{', ']':'['} 
    stack_list = []

    for char in s:
        if char in pair_dict.values():
            stack_list.append(char)

        elif char in pair_dict:
            if not stack_list or stack_list[-1] != pair_dict[char]:
                return False
            stack_list.pop()

    return len(stack_list) == 0

        
        


def next_greater_to_right(nums: list[int]) -> list[int]:
    """
    For each element, find the next greater element to its right.
    If none exists, output -1 for that position.

    Example:
      nums = [2, 1, 2, 4, 3]
      output -> [4, 2, 4, -1, -1]
    """
    # TODO: implement using a stack (monotonic stack)
    n = len(nums)
    result = [-1] * n
    stack_list = []

    for i in range(n - 1, -1, -1):
        while stack_list and stack_list[-1] <= nums[i]:
            stack_list.pop()
            
        if stack_list:
            result[i] = stack_list[-1]
            
        stack_list.append(nums[i])
        
    return result


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
    # TODO: implement using a queue + counts
    
    queue = deque()
    char_count = {}
    result_list = []
    
    for char in stream:
        char_count[char] = char_count.get(char, 0) + 1
        queue.append(char)

        while queue and char_count[queue[0]] > 1:
            queue.popleft()

        if queue:
            result_list.append(queue[0])
        else:
            result_list.append('#')

    return "".join(result_list)


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
    # TODO: implement using a queue (deque)

    queue = deque(names)

    while len(queue) > 1:

        for _ in range(k):
            queue.append(queue.popleft())
            
        queue.popleft()
        
    return queue[0]
