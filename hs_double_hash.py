class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        h = 0

        if isinstance(key, str):
            for char in key:
                h ^= (h << 5) + (h >> 2) + ord(char)
        else:
            for num in key:
                h ^= (h << 5) + (h >> 2) + num

        return h % self.size

    def _double_hash(self, key, i):
        return (self.hash_function(key) + i * (1 + self.hash_function(key) % (self.size - 1))) % self.size

    def insert(self, key, value):
        i = 0
        hash_value = self.hash_function(key)

        while self.table[hash_value] is not None:
            i += 1
            hash_value = self._double_hash(key, i)

        self.table[hash_value] = (key, value)

    def search(self, key):
        i = 0
        hash_value = self.hash_function(key)

        while self.table[hash_value] is not None:
            stored_key, value = self.table[hash_value]
            if stored_key == key:
                return value

            i += 1
            hash_value = self._double_hash(key, i)

        return None

    def display(self):
        for index, item in enumerate(self.table):
            print(f'Index {index}:', end=' ')
            if item is None:
                print('Empty')
            else:
                print(f'({item[0]}: {item[1]})')
