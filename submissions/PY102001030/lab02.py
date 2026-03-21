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
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    for char in s:
        # If it's an opening bracket, push to stack
        if char in "({[":
            stack.append(char)
        # If it's a closing bracket, check for a match
        elif char in ")}]":
            # If stack is empty or the top doesn't match the pair, it's unbalanced
            if not stack or stack.pop() != mapping[char]:
                return False
                
    # If the stack is empty, all brackets were matched correctly
    return len(stack) == 0
    
    


def next_greater_to_right(nums: list[int]) -> list[int]:
    """
    For each element, find the next greater element to its right.
    If none exists, output -1 for that position.

    Example:
      nums = [2, 1, 2, 4, 3]
      output -> [4, 2, 4, -1, -1]
    """
    n = len(nums)
    result = [-1] * n
    stack = []  # This will store values to compare against
    
    # Traverse the list from right to left
    for i in range(n - 1, -1, -1):
        # While there is a smaller or equal element on the stack, it can't be the "Next Greater"
        while stack and stack[-1] <= nums[i]:
            stack.pop()
        
        # If stack is not empty, the top element is the next greater one
        if stack:
            result[i] = stack[-1]
            
        # Push the current element onto the stack for the elements to its left
        stack.append(nums[i])
        
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
    char_counts = {}
    queue = deque()
    result_list = []
    for char in stream:
        # Update character frequency
        char_counts[char] = char_counts.get(char, 0) + 1
        # Add current character to the queue
        queue.append(char)
        
        # Clean the front of the queue: remove characters that are now repeating
        while queue and char_counts[queue[0]] > 1:
            queue.popleft()
            
        # The front of the queue is the first non-repeating character
        if not queue:
            result_list.append("#")
        else:
            result_list.append(queue[0])
            
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
    if not names:
        return ""
        
    # Initialize the queue with all players
    queue = deque(names)
    
    while len(queue) > 1:
        # Move the potato k times (k passes)
        # Each pass moves the person from the front to the back
        for _ in range(k):
            queue.append(queue.popleft())
        
        # After k passes, the person at the front is eliminated
        queue.popleft()
        
    # The last person remaining is the winner
    return queue[0]


