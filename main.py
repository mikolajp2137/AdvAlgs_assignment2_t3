import hs_linear_probing, hs_separate_chaining, hs_double_hash, random_el
import timeit, matplotlib

# SEPARATE CHAINING
SC_hash_table = hs_separate_chaining.HashTable(200)
SC_hash_table.insert("apple", 1)
random_el.add_random_elements(SC_hash_table, 175, 10)
SC_hash_table.display()
