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
    parentheses_pair = {")":"(","]":"[","}":"{"}
    stack_list = []

    for char in s:
      if char in parentheses_pair:
        if (len(stack_list)==0):
          return False
        top = stack_list[-1]
        if top != parentheses_pair[char]:
          return False
        stack_list.pop()
      elif char in parentheses_pair.values():
        stack_list.append(char)
    return True

def next_greater_to_right(nums: list[int]) -> list[int]:
    """
    For each element, find the next greater element to its right.
    If none exists, output -1 for that position.

    Example:
      nums = [2, 1, 2, 4, 3]
      output -> [4, 2, 4, -1, -1]
    """
    # TODO: implement using a stack (monotonic stack)
    result = []

    for i in range(len(nums)):
      j = i+1
      while j<len(nums) and nums[i] >= nums[j]:
        j+=1

      if j<len(nums):
        result.append(nums[j])
      else:
        result.append(-1)
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
    count= {}
    result =[]

    for char in stream:
      if char in count:
        count[char] = count[char] + 1
      else:
        count[char] = 1

      queue.append(char)
      while queue and count[queue[0]] > 1:
        queue.popleft()

      if queue:
        result.append(queue[0])
      else:
        result.append('#')

    return "".join(result)


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
    players = deque(names)

    while len(players) > 1:
      for i in range(k):
        players.append(players.popleft())
      players.popleft()

    return players[0]

print("Q1")
print("([]){} ==>",is_balanced_parentheses("([]){}"))
print("(] ==>",is_balanced_parentheses("(]"))
print("a+(b*c)-{d/e} ==>",is_balanced_parentheses("a+(b*c)-{d/e}"))

number=[2,1,2,4,6,3,5]
print("\nQ2")
print(f"Output of {number} ==> {next_greater_to_right(number)}")

text = "aabcceb"
print("\nQ3")
print(f"{text} => ",first_non_repeating(text))

print("\nQ4")
print("The winner :",hot_potato(["A", "B", "C", "D", "E"], 3))
