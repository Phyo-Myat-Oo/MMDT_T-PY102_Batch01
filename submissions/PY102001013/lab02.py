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


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[-1] if self.items else None

    def pop(self):
        return self.items.pop() if self.items else None


class Queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.items:
            return None
        return self.items.pop(0)

    def peek(self):
        if not self.items:
            return None
        return self.items[0]

    def size(self):
        return len(self.items)

    def for_debug(self):
        return self.items


def is_balanced_parentheses(s: str) -> bool:
    """
    Return True if the string s has balanced brackets: (), {}, [].
    Ignore non-bracket characters.

    Examples:
      is_balanced_parentheses("([]){}") -> True
      is_balanced_parentheses("(]") -> False
      is_balanced_parentheses("a+(b*c)-{d/e}") -> True
    """
    st = Stack()

    p_list = {"(": ")", "{": "}", "[": "]"}

    openings = list(p_list.keys())
    closings = list(p_list.values())

    for par in s:
        if par in openings:
            st.push(par)
        elif par in closings:
            if st.size() == 0:
                return False
            # check if the last item in stack is a match
            # check the last item in stack
            # get the last item in stack
            last_opening = st.peek()
            # use that as a key on p_list
            # print("From HERE")
            # print(p_list[last_opening])
            if p_list[last_opening] == par:
                st.pop()
            else:
                return False
    return st.size() == 0


def next_greater_to_right(nums: list[int]) -> list[int]:
    """
    For each element, find the next greater element to its right.
    If none exists, output -1 for that position.

    Example:
      nums = [2, 1, 2, 4, 3]
      output -> [4, 2, 4, -1, -1]
    """
    # TODO: implement using a stack (monotonic stack)
    stk = Stack()
    result = [-1 for _ in range(len(nums))]

    # use stack to store
    for n_left_idx, n_left in enumerate(nums):
        # 1. store current n_left's value or index in a Stack
        # 2. iterate the nums again with n_right from the Stack's last value - index + 1
        # 3. if n_right is greater than n_left
        # 4. append the n_right's value to the result list

        while stk.size() > 0 and nums[stk.peek()] < n_left:
            left_idx = stk.peek()
            stk.pop()
            result[left_idx] = n_left

        # store current index for future comparison
        stk.push(n_left_idx)
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
    char_counter = {}
    q = Queue()

    result_string = ""

    for current_char in stream:
        if current_char not in char_counter:
            char_counter[current_char] = 1
        else:
            char_counter[current_char] += 1

        if char_counter[current_char] == 1:
            q.push(current_char)

        while q.size() > 0:
            first_candidate_character = q.peek()

            if char_counter[first_candidate_character] > 1:
                q.pop()
            else:
                break

        # decide what to append to result
        if q.size() > 0:
            result_string += q.peek()
        else:
            result_string += "#"

    return result_string


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
    q = Queue()

    for name in names:
        q.push(name)

    # while size of Q is not 1

    # pop k times
    # and then get the pop resul and then push back into the q
    while q.size() != 1:
        for _ in range(k - 1):
            get_back_in_line = q.pop()
            # print("get_back_in_line", get_back_in_line)

            q.push(get_back_in_line)

            # print("q.peek", q.peek())

            # print(q.for_debug())
            # print("-----FINISH ONE FOR-----")
        q.pop()
        # print("--FINISH ONE WHILE RESULT >>> ", q.for_debug())
    return q.peek()
    # print(q.peek())
