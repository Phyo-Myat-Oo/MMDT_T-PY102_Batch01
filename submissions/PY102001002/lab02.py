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
    p_dict = {")":"(", "}":"{", "]":"["}
    s_list = []
    #print(s)
    for cha in s:
      #print("char is",cha)
      if cha in p_dict:
        if(len(s_list)==0):
          #print('cloasing char is found')
          #print("the stack is empty")
          return False
        temp = s_list[-1]
        #print("the last temp ",temp)
        if temp!=p_dict[cha]:
          #print("opening is",temp)
          print("closing is",cha)
          return False
        s_list.pop()
        #print('removelast char',temp)
        #print(s_list)
      elif cha in p_dict.values():
        s_list.append(cha)
        #print('add char')
        #print(s_list)
    return len(s_list)==0


def next_greater_to_right(nums: list[int]) -> list[int]:
    """
    For each element, find the next greater element to its right.
    If none exists, output -1 for that position.

    Example:
      nums = [2, 1, 2, 4, 3]
      output -> [4, 2, 4, -1, -1]
    """
    temp = []
    for n in range(len(nums)):
      found = False
      for j in range(n+1,len(nums)):
        if nums[j]>nums[n]:
          temp.append(nums[j])
          #print(temp)
          found = True
          break
      if not found:
        temp.append(-1) 
    return temp


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
    result = ''
    for i in range(len(stream)):
      current = stream[:i+1]
      #print('current',current)
      cha_count = {}
      for cha in current:
        if cha in cha_count:
          cha_count[cha] += 1
        else:
          cha_count[cha] = 1
      #print('CHACOUNT',cha_count)

      found = False
      for cha in current:
        if cha_count[cha] == 1:
          result += cha
          found = True
          break
      if not found:
        result += '#'
        #print ('result',result)
    return result




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
    while len(names)>1:
      for i in range(k):
        names.append(names.pop(0))
        #print("name",names)
      names.pop(0)
    return names[0]
    #print(names) 
