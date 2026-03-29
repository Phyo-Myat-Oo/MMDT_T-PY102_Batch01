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
    isunique =[]
    iscount = []
    # ord(s[0])
    # index = ord(s[0])%26
    for char in s:
      if char not in isunique:
        isunique.append(char)
        iscount.append(1)
      else:
         iscount[isunique.index(char)]+=1
    return dict(zip(isunique,iscount))

# print('char','banana',char_frequency("banana"))
# print('char','aaabe',char_frequency("aaabe"))
# print('char','abcabc',char_frequency("abcabc"))
# print('char','a',char_frequency("a"))
# print('char','AaABBBEE',char_frequency("AaABBBEE"))
# print('char','112333',char_frequency("112333"))


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
    index = key % size
    table[index].append(key)
    return table

# print(insert_chaining([[], [], []],5,3))
# print(insert_chaining([[8], [], [2]],9,3))
# print(insert_chaining([[], [1], [2,6],[]],5,3))


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
    index = key % len(table)
    #print('first index is ',index,'first value is ',table[index])
    for _ in range(len(table)):
      if table[index] is None:
        table[index] = key
        #print('index is ',index,'value is ',table[index])
        return table
      #print('loop index is ',index,'loop value is ',table[index])
      index = (index + 1) % len(table)
    return table
  
# print(insert_linear_probing([None, 4, None, None],8))
# print(insert_linear_probing([5,6,7],8))
# print(insert_linear_probing([1, None,None, None, None],8))
# print(insert_linear_probing([3, 7, None, 9,None],8))
# print(insert_linear_probing([1, 2, 3, None],8))



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
    temp = key % len(table)
    #print('first index is ',temp,'first value is ',table[temp])
    for i in range(len(table)):
      index = (temp+i*i)%len(table)
      #print('index before if is ',index,'value before if  is ',table[index])
      if table[index] is None:
        table[index] = key
        #print('index is ',index,'value is ',table[index])
        return table
      #print('loop index is ',index,'loop value is ',table[index])
    return table

# print(insert_quadratic_probing([None, 4, None, None,None],8))
# print(insert_quadratic_probing([5,6,7,9],8))
# print(insert_quadratic_probing([None,1, None,None, None, None],8))
# print(insert_quadratic_probing([3, 7, None, 9,None],8))
# print(insert_quadratic_probing([1, 2, 3, None,6],8))
