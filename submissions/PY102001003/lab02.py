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
    parenthesese_dict = {"}":"{","]":"[",")":"("}
    paren_list = []
    for char in s:
        if char in parenthesese_dict.values():
            paren_list.append(char)
              # print(paren_list)
        elif char in parenthesese_dict.keys():
            if len(paren_list)==0 or parenthesese_dict[char] != paren_list[-1]:
                return False
            paren_list.pop()
    return not paren_list

    raise NotImplementedError
print(is_balanced_parentheses("a+(b*c)-{d/e}"))


def next_greater_to_right(nums: list[int]) -> list[int]:
    """
    For each element, find the next greater element to its right.
    If none exists, output -1 for that position.

    Example:
      nums = [2, 1, 2, 4, 3]
      output -> [4, 2, 4, -1, -1]
    """
    # TODO: implement using a stack (monotonic stack)
    """
    def "monotonic stack"
    element are arranged in a strictly increasing or decreasing order.
    This is used monotonic decreasing as 
    When a larger element arrives, smaller elements are popped first.
    """
    s_index = []
    res_nums = [None]*len(nums)#None is required as it is considered as an object in Python and indexing can be possible
    for i in range(len(nums)):
        while s_index and nums[i] > nums[s_index[-1]]:
          res_nums[s_index[-1]] = nums[i]
          s_index.pop()
        s_index.append(i)

        #assigning -1 to the remained indexes in the s_idex
    for r in s_index:
       res_nums[r] = -1
    return res_nums
    raise NotImplementedError
print(next_greater_to_right([2, 1, 2, 4, 3]))


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
    count_dict = {}
    ch_de = deque()
    result = []
    for char in stream:
        if char in count_dict:
            count_dict[char] +=1
        else:
            count_dict[char] = 1

        # count_dict.setdefault(char,0)
        # count_dict[char] += 1
        ch_de.append(char)

        while ch_de and count_dict[ch_de[-1]] > 1:
            ch_de.popleft()
        if ch_de:
            result.append(ch_de[0])
        else:
            result.append("#")
    return "".join(result)
    raise NotImplementedError
print(first_non_repeating("aabc"))

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
    de_names = deque(names)
    while len(de_names) > 1:
        #alternative way: 
        # de_names.rotate(-k)
        for _ in range(k):# we just do looping here for k times
            af_loop_name = de_names.popleft()
            de_names.append(af_loop_name) #if I did looping over a name, sent it to the back. 
        de_names.popleft()

    return f"The winner is {de_names[0]}."
    raise NotImplementedError

print(hot_potato(["A","B", "C", "D"],2))
