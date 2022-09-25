################################################
# Implementing Dictionary using HashTable - Part 1
################################################

def get_hash(key):
    h = 0
    for char in key:
        h += ord(char)
    return h % 100


print(get_hash("Pooja"))
#5

class HashTable:
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

# Create a HashTable object

t = HashTable()
print(t.arr)
# [None, None, None, None, None, None, None, None, None, None]

index = t.get_hash("Pooja")
print(index)
# 5

#--------------------------------------------------------------------------
# Now we want to implement a function to add an item into HashMap and get an item from HashMap.
# in our example we wanted to store Day and stock prices on that day.
# it is like a key,value pair
# so, To Store the information: add(key, value)
# 1. Get key and value as input
# 2. Call get_hash() function to get the index at which we want to store the value
# 3. Store the value in our internal array

# To retrieve the information: get(key)
# 1. get the key in input
# 2. call a get_hash() function for input key to find the index at which
# its corresponding value is stored
# return value stored in internal array at given index
#--------------------------------------------------------------------------

t.add("Pooja", 20)
print(t.arr)
# [None, None, None, None, None, 20, None, None, None, None]

value = t.get("Pooja")
print(value)
# 5

# -----------------------------------------------------

# Python allows us to override operators
# when we write arr[index] = 10, we are indirectly calling __setitem__
# and when we write print(arr[index]), we are indirectly calling __getitem__
# so, lets replace add() and get() methods by the dunder methods
# ---------------------------------------------------------

index = t.get_hash("Anne")
print(index)
# 6

t["Anne"] = 3
print(t.arr)
# [None, None, None, None, None, 20, 3, None, None, None]

value = t["Anne"]
print(value)
# 3

del t["Anne"]
print(t.arr)
# [None, None, None, None, None, 20, None, None, None, None]

