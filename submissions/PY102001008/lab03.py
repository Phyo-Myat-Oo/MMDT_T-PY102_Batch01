def char_frequency(s: str) -> dict[str, int]:
    """
    Q1:
    Given a string s, return a dictionary showing the frequency
    of each character in the string.
    """
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq
#s = "banana"
#print(f"Q1 Test: {char_frequency(s)}")


# -------------------------
# Q2 — Chaining (Collision Handling)
# -------------------------

def insert_chaining(table: list[list[int]], key: int, size: int) -> list[list[int]]:
    """
    Q2:
    Simulate inserting a key into a hash table using chaining.
    """
    # The hash function is key % size [1, 2].
    index = key % size
    
    # In chaining, each bucket is a list where multiple elements can be stored [1, 3].
    # We append the key to the list at the calculated index [4, 5].
    table[index].append(key)
    
    return table

#table_q2 = [[], [], []]
#size = 3
#print(f"Q2 Test 1: {insert_chaining(table_q2, 5, size)}") 



# -------------------------
# Q3 — Linear Probing
# -------------------------

def insert_linear_probing(table: list[int | None], key: int) -> list[int | None]:
    """
    Q3:
    Simulate inserting a key into a hash table using linear probing.
    """
    n = len(table)
    # The hash function is key % length of the table [6].
    index = key % n
    
    # Linear probing moves to the next index if a slot is occupied [7, 8].
    # It continues until it finds an empty (None) slot [6, 9].
    while table[index] is not None:
        index = (index + 1) % n # Move to the next index circularly [8, 10].
        
    table[index] = key
    return table

#table_q3 = [None, 21, None, None]
#print(f"Q3 Test: {insert_linear_probing(table_q3, 13)}")



# -------------------------
# Q4 — Quadratic Probing
# -------------------------

def insert_quadratic_probing(table: list[int | None], key: int) -> list[int | None]:
    """
    Q4:
    Simulate inserting a key into a hash table using quadratic probing.
    """
    n = len(table)
    # The base hash function is key % length of the table [11].
    base_hash = key % n
    
    # Quadratic probing uses a sequence (hash + i*i) to find an empty slot [11-13].
    i = 0
    while True:
        # Probe sequence: (hash + i*i) % len(table) [11, 12].
        index = (base_hash + i * i) % n
        if table[index] is None:
            table[index] = key
            break
        i += 1
        
    return table

#table_q4 = [None, 7, None, None]
#print(f"Q4 Test 1: {insert_quadratic_probing(table_q4, 11)}")