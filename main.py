import timeit
import hs_double_hash, hs_linear_probing, hs_separate_chaining
import random, string

times = []
length = 900000
keysG = lambda: [''.join(random.choices(string.ascii_letters, k=20)) for _ in range(length)]
valuesG = lambda: [random.randint(1, 9) for _ in range(length)]

keys, values = keysG(), valuesG()

# DOUBLE HASHING
# DH_hash_table = hs_double_hash.HashTable(1000000)
#
#
# def DH_insert():
#     DH_hash_table.insert("apple", 1)
#     for v in range(length):
#         DH_hash_table.insert(keys[v], values[v])
#
#
# DHtime = timeit.timeit(lambda: DH_insert(), number=1)
# print("Time", DHtime)

# LINEAR PROBING
LP_hash_table = hs_linear_probing.HashTable(1000000)


def LP_insert():
    LP_hash_table.insert("apple", 1)
    for v in range(length):
        LP_hash_table.insert(keys[v], values[v])


LPtime = timeit.timeit(lambda: LP_insert(), number=1)
print("Time", LPtime)

# SEPARATE CHAINING
SC_hash_table = hs_separate_chaining.HashTable(1000000)


def SC_insert():
    SC_hash_table.insert("apple", 1)
    for v in range(length):
        SC_hash_table.insert(keys[v], values[v])


SCtime = timeit.timeit(lambda: SC_insert(), number=1)
print("Time", SCtime)
