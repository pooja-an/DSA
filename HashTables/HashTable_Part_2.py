################################################
# Implementing Dictionary using HashTable - Part 2
# Collision Handling
################################################

# as per our below implementation, it does not handle collision
# When collision happens it will just overrite the value of existing key
# which will result in inconsistent data


class HashTable_old:
    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % 10

    def add(self, key, value):
        h = self.get_hash(key)
        self.arr[h] = value

    def get(self, key):
        h = self.get_hash(key)
        return self.arr[h]

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        self.arr[h] = value

    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None


# ---------------------------------------------------------------------
# Now this will be array of array which stores a linked list i.e. tuple
# and before stoing the value we need to check if the given key already exists
# in that case we will just update the value of that key.
# ---------------------------------------------------------------------
class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % 10

    def __getitem__(self, key):

        h = self.get_hash(key)

        for index, element in enumerate(self.arr[h] ):
            if len(element) == 2 and element[0] == key:
                return self.arr[h][index][1]

        # OR both for loops works
        
        for element in (self.arr[h]):
            if element[0] == key:
                return element[1]

    def __setitem__(self, key, value):
        
        h = self.get_hash(key)

        for index, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][index] = (key, value)
                return
            
        self.arr[h].append((key, value))

    def __delitem__(self, key):

        h = self.get_hash(key)

        for index, element in enumerate(self.arr[h]):
            print(index, element)
            if len(element) == 2 and element[0] == key:
                del self.arr[h][index]
                return      


t = HashTable()
print(t.arr)
# [[], [], [], [], [], [], [], [], [], []]

t["Pooja"] = 20
print(t.arr)
# [[], [], [], [], [], [('Pooja', 20)], [], [], [], []]

value = t["Pooja"]
print(value)
# 20

del t["Pooja"]
print(t.arr)
# [[], [], [], [], [], [], [], [], [], []]

#####################################
# Multile keys at same hash

t["Pooja"] = 20
print(t.arr)
# [[], [], [], [], [], [('Pooja', 20)], [], [], [], []]

t['\x05'] = 100
print(t.arr)
# [[], [], [], [], [], [('Pooja', 20), ('\x05', 100)], [], [], [], []]


value = t['\x05']
print(value)
# 100

print(t["Pooja"])
# 20

del t["Pooja"]
print(t.arr)
[[], [], [], [], [], [('\x05', 100)], [], [], [], []]



