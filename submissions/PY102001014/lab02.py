from typing import List
from collections import deque

# -------------------------
# Question 1 — Balanced Parentheses
# -------------------------
def is_balanced_parentheses(s: str) -> bool:
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}

    for ch in s:
        if ch in "([{":
            stack.append(ch)
        elif ch in ")]}":
            if not stack or stack.pop() != pairs[ch]:
                return False
    return not stack


# -------------------------
# Question 2 — Next Greater Element to Right
# -------------------------
def next_greater_to_right(nums: List[int]) -> List[int]:
    stack = []
    result = [-1] * len(nums)

    for i, num in enumerate(nums):
        while stack and num > nums[stack[-1]]:
            idx = stack.pop()
            result[idx] = num
        stack.append(i)

    return result


# -------------------------
# Question 3 — First Non-Repeating Character in Stream
# -------------------------
def first_non_repeating(stream: str) -> str:
    q = deque()
    freq = {}
    output = []

    for ch in stream:
        freq[ch] = freq.get(ch, 0) + 1
        q.append(ch)

        while q and freq[q[0]] > 1:
            q.popleft()

        output.append(q[0] if q else '#')

    return ''.join(output)


# -------------------------
# Question 4 — Hot Potato
# -------------------------
def hot_potato(names: List[str], k: int) -> str:
    q = deque(names)

    while len(q) > 1:
        for _ in range(k):
            q.append(q.popleft())
        q.popleft()

    return q[0]


# -------------------------
# Check with print statements
# -------------------------

