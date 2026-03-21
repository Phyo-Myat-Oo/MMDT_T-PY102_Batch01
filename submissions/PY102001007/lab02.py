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
# Stack Questions (1)
# -------------------------

def is_balanced_parentheses(s: str) -> bool:
    matching_open = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    stack = []

    for char in s:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if len(stack) == 0:
                return False

            top_of_stack = stack[-1]
            expected_open = matching_open[char]

            if top_of_stack != expected_open:
                return False

            stack.pop()

    return len(stack) == 0

# -------------------------
# Queue Questions (2)
# -------------------------

def next_greater_to_right(nums: list[int]) -> list[int]:
    result = [-1] * len(nums)
    stack = []

    for current_index in range(len(nums)):
        current_value = nums[current_index]

        while len(stack) > 0 and nums[stack[-1]] < current_value:
            waiting_index = stack.pop()
            result[waiting_index] = current_value

        stack.append(current_index)

    return result


# -------------------------
# Queue Questions (3)
# -------------------------

def first_non_repeating(stream: str) -> str:
    count = {}
    queue = deque()
    result = []

    for char in stream:
        if char not in count:
            count[char] = 1
        else:
            count[char] = count[char] + 1

        queue.append(char)

        while len(queue) > 0 and count[queue[0]] > 1:
            queue.popleft()

        if len(queue) > 0:
            result.append(queue[0])
        else:
            result.append('#')

    return ''.join(result)
  
# -------------------------
# Queue Questions (4)
# -------------------------

  
def hot_potato(names: list[str], k: int) -> str:
    queue = deque(names)

    while len(queue) > 1:
        for pass_number in range(k):
            person_at_front = queue.popleft()
            queue.append(person_at_front)

        queue.popleft()

    winner = queue[0]
    return winner
