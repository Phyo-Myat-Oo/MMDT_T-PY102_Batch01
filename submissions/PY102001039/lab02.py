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
    pair_dict = {"}" : "{", ")" : "(", "]" : "[",}
    pair_dict2 = {"{" : "}", "(" : ")", "[" : "]",}
    lst = []

    for char in s:
        if (char in pair_dict):
            if(lst is None):
                return False
            top = lst[-1]
            if(top != pair_dict[char]):
                return False
            lst.pop()

        else:
            
            if (char in pair_dict2):
                lst.append(char)          
                   
            

    return True

result = is_balanced_parentheses("a+(b*c)-{d/e}")
print(result)


def next_greater_to_right(nums: list[int]) -> list[int]:
    """
    For each element, find the next greater element to its right.
    If none exists, output -1 for that position.

    Example:
      nums = [2, 1, 2, 4, 3]
      output -> [4, 2, 4, -1, -1]
    """
    # TODO: implement using a stack (monotonic stack)
    idx = 0
    lst = []
    for num in nums:
        found = False
        while (found == False and idx < 4):
            next = nums[idx + 1]
            
            #print('next:', next)

            if (next > num):
                lst.append(next)
                found = True
                idx = 0
            else:
                idx = idx + 1

        if(found == False):
            lst.append(-1)
    return lst      

        

nums = [2, 1, 2, 4, 3]
result = next_greater_to_right(nums)
print(result)


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
    result_q = ''
    temp_q = deque()
    for char in stream:
        if(char not in temp_q):            
            temp_q.append(char)
            result_q += temp_q[0]

        elif (char in temp_q):
            temp_q.pop()
            if(len(temp_q) == 0):
                result_q += "#"
            else:
                result_q += temp_q[0]
    return result_q
    

result = first_non_repeating("aabc")
print("Result:", result)


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
    q = deque(names)

    while len(q) > 1:
        for _ in range(k):
            q.append(q.popleft())

        eliminated = q.popleft()

    return q[0]


names = ["A", "B", "C", "D"]
k = 2

winner = hot_potato(names, k)
print("Winner:", winner)
