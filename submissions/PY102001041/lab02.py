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
    # initialize stack and paris
    bracket_pairs = {
        "(": ")",
        "[": "]",
        "{": "}",
    }
    stack_list = deque()
    
    for char in input_str:

        # process for keys
        if char in bracket_pairs:
            stack_list.append(char)

        # process for values
        if char in bracket_pairs.values():
            if len(stack_list) == 0:
                return False

            if bracket_pairs[stack_list[-1]] != char:
                return False
            
            else:
                stack_list.pop()

    # return false if list is not empty
    if stack_list:
        return False
    
    return True


def next_greater_to_right(nums: list[int]) -> list[int]:
    """
    For each element, find the next greater element to its right.
    If none exists, output -1 for that position.

    Example:
      nums = [2, 1, 2, 4, 3]
      output -> [4, 2, 4, -1, -1]
    """

    # initialize vars
    out_list = [-1] * len(nums)
    stack = deque()

    # reverse for iteration
    for i in range((len(nums) -1), -1, -1):
        
        # pop smaller or equal numbers
        while stack and stack[-1] <= nums[i]:
            stack.pop()

        if stack:
            out_list[i] = stack[-1]

        stack.append(nums[i])


    return out_list


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
    # initialize vars
    count_map = {}
    check_queue = deque()
    out_str = ""


    # iteration
    for char in stream:
        
        # # validate chars to check_stack
        # if char not in check_stack:
        #     check_stack.append(char)
        # else:
        #     check_stack.remove(char)

        # # get output from check_stack
        # if len(check_stack) == 0:
        #     out_str += "#"
        # else:
        #     out_str += check_stack[0]

        if char not in count_map:
            count_map[char] = 1
        else:
            count_map[char] += 1

        check_queue.append(char)

        while check_queue and count_map[check_queue[0]] > 1:
            check_queue.popleft()

        if check_queue:
            out_str += check_queue[0]

        else:
            out_str += "#"

    return out_str


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
    # create queue from input
    queue = deque(names)

    # iteration 
    while len(queue) > 1:
        for i in range(k):
            queue.append(queue.popleft())

        queue.popleft()

    return queue[0]


# # TESTING PURPOSE
# if __name__ == "__main__":
#     nums = [1, 2, 6, 3, 5, 7, 4, 1]
#     print(next_greater_to_right(nums))

#     # input_str = "aabcc"
#     # print(first_non_repeating(input_str))

#     # check parentheses
#     input_str = "(({{[[fadfoa]]}}))"
#     print (is_balanced_parentheses(input_str))

#     # test for hot potato
#     names = ["A", "B", "C", "D"]
#     k = 2
#     print(hot_potato(names, k)) 
