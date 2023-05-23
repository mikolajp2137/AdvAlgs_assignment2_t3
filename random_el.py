import random
import string


def add_random_elements(hash_table, num_elements, key_length):
    for _ in range(num_elements):
        key = ''.join(random.choice(string.ascii_letters) for _ in range(key_length))
        value = random.randint(1, 1000)  # Generate a random value
        hash_table.insert(key, value)
