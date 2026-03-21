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
    parentheses = ["(", ")", "{", "}", "[", "]"]
    mapping = {")": "(", "}": "{", "]": "["}

    # print("processing...", s)

    for char in s:
        if char in parentheses:
            if char in mapping:
                top = stack[-1]

                if mapping[char] == top:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

    if len(stack) == 0:
        return True

    return False


def next_greater_to_right(nums: list[int]) -> list[int]:
    """
    For each element, find the next greater element to its right.
    If none exists, output -1 for that position.

    Example:
      nums = [2, 1, 2, 4, 3]
      output -> [4, 2, 4, -1, -1]
    """
    # TODO: implement using a stack (monotonic stack)

    # stack = []
    result = []

    for i in range(len(nums)):
        num = nums[i]

        found = False

        for j in range(i + 1, len(nums)):
            next_element = nums[j]

            if next_element > num:
                found = True
                result.append(next_element)
                break
        if not found:
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

    repeating_dict = {
        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0,
        "e": 0,
        "f": 0,
        "g": 0,
        "h": 0,
        "i": 0,
        "j": 0,
        "k": 0,
        "l": 0,
        "m": 0,
        "n": 0,
        "o": 0,
        "p": 0,
        "q": 0,
        "r": 0,
        "s": 0,
        "t": 0,
        "u": 0,
        "v": 0,
        "w": 0,
        "x": 0,
        "y": 0,
        "z": 0,
    }

    queue = deque()
    output = ""

    for char in stream:
        repeating_dict[char] += 1

        queue.append(char)

        while len(queue) != 0 and repeating_dict[char] > 1:
            queue.pop()

        if len(queue) == 0:
            output += "#"
        else:
            output += queue[0]

    # print(output)
    return output


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
    winner = ""
    # circular_queue = deque()
    index = 0

    while len(names) != 1:

        remaining_len = len(names)

        for _ in range(k):
            position = index % remaining_len
            element = names[position]
            index += 1

            if index > len(names):
                index = index % remaining_len

        if index >= len(names):
            index = index % len(names)

        holder = names[index]

        names.remove(holder)

    winner = names[0]

    return winner
