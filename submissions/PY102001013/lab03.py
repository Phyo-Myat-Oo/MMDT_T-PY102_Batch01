"""
Lab 03 — Hash Tables (4 Questions)

Rules:
- Do NOT use print() or input().
- Implement the functions exactly as named.
- You may use basic Python lists and dictionaries.
- Do NOT use any built-in hash table libraries except dict for Q1.

Questions:
Q1) Hash map usage
Q2) Hash table with chaining (conceptual simulation)
Q3) Linear probing simulation
Q4) Quadratic probing simulation
"""


# -------------------------
# Q1 — Hash Map
# -------------------------


def char_frequency(s: str) -> dict[str, int]:
    """
    Q1:
    Given a string s, return a dictionary showing the frequency
    of each character in the string.

    Example:
      s = "banana"
      output = {'b': 1, 'a': 3, 'n': 2}
    """

    char_table = {}

    for char in s.lower():
        if char in char_table.keys():
            char_table[char] += 1
        if char not in char_table.keys():
            char_table[char] = 1
    # print(char_table)

    return char_table


# char_frequency("aabbccdd")

# -------------------------
# Q2 — Chaining (Collision Handling)
# -------------------------


def insert_chaining(table: list[list[int]], key: int, size: int) -> list[list[int]]:
    """
    Q2:
    Simulate inserting a key into a hash table using chaining.

    - table is a list of buckets (each bucket is a list).
    - hash function: key % size
    - Insert the key into the correct bucket.

    Example:
      table = [[], [], []]
      key = 5
      size = 3

      index = 5 % 3 = 2
      output = [[], [], [5]]
    """

    def hashFunc(x, y):
        return x % y

    hash = hashFunc(key, size)
    # print(hashed)
    # print(table[hashed])
    table[hash].append(key)
    # print(table)
    return table


# insert_chaining([[], [], []], 5, 3)

# -------------------------
# Q3 — Linear Probing
# -------------------------


def insert_linear_probing(table: list[int | None], key: int) -> list[int | None]:
    """
    Q3:
    Simulate inserting a key into a hash table using linear probing.

    Rules:
    - hash function: key % len(table)
    - If a slot is occupied, move to the next index (circular).
    - Insert the key into the first empty (None) slot.

    Example:
      table = [None, 4, None, None]
      key = 8

      hash = 8 % 4 = 0
      slot 0 is empty → insert

      output = [8, 4, None, None]
    """

    # TODO
    def hashFunc(x, y):
        return x % len(y)

    hash = hashFunc(key, table)

    if table[hash] is None:
        table[hash] = key
    else:
        for i in range(len(table)):
            idx = (hash + i) % len(table)
            if table[idx] is None:
                table[idx] = key
                break
    # print(table)

    return table


# insert_linear_probing([None, 4, None, None], 8)

# -------------------------
# Q4 — Quadratic Probing
# -------------------------


def insert_quadratic_probing(table: list[int | None], key: int) -> list[int | None]:
    """
    Q4:
    Simulate inserting a key into a hash table using quadratic probing.

    Rules:
    - hash function: key % len(table)
    - Probe sequence:
        (hash + i*i) % len(table), for i = 0, 1, 2, ...
    - Insert the key into the first empty (None) slot.

    Example:
      table = [None, 7, None, None]
      key = 11

      hash = 11 % 4 = 3
      i = 0 → index = 3
      slot 3 is empty → insert

      output = [None, 7, None, 11]
    """

    def hashFunc(x, y):
        return x % len(y)

    hash = hashFunc(key, table)

    if table[hash] is None:
        table[hash] = key
    else:
        for i in range(len(table)):
            idx = (hash + i * i) % len(table)
            if table[idx] is None:
                table[idx] = key
                break

    return table
