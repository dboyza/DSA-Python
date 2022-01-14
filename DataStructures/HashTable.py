"""
HASHTABLE IMPLEMENTATION
GOOD FOR: 
-O(1) KEY LOOKUPS
"""


# HashTable Implementation
class HashTable:
    # HashTable constructor
    def __init__(self, size=7):
        self.data_map = [None] * size

    # Mathematical function to determine what index the data
    # is mapped to in the hash table : O(1)
    def __hash(self, key):
        hash = 0
        for letter in key:
            # Formula to create a unique hash for each value [0-6]
            hash = (hash + ord(letter) * 23) % len(self.data_map)
        return hash

    # Adds a value to the hash table given a key and a value: O(1)
    def set_item(self, key, value):
        # Get the index by calling the hash function with the key
        index = self.__hash(key)

        # Create an empty list at the table's index if empty
        if self.data_map[index] == None:
            self.data_map[index] = []

        # Append the key value pair as a list to the table's index
        self.data_map[index].append([key, value])

    # Returns a value from the hash table given a key: O(1)
    def get_item(self, key):
        # Get the index by calling the hash function with the key
        index = self.__hash(key)

        # Loop through the list at the table's index if it exists
        # If found, return the value of the key in the list
        if self.data_map[index]:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        # Return None if there was no list at the index found by the hash
        return None

    # Returns a list of all keys in the hash table: O(n^2)
    def keys(self):
        # Create an empty list to store the keys
        keys = []
        # Look through the hash table
        for i in range(len(self.data_map)):
            # If there is a list at the current index, loop
            # through it and append each key to the list
            if self.data_map[i]:
                for j in range(len(self.data_map[i])):
                    keys.append(self.data_map[i][j][0])
        # Return the keys list
        return keys

    # Prints the key, value pairs in the hash table
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ":", val)


table = HashTable()
table.set_item('cat', 'brown')
table.set_item('dog', 'black')
table.set_item('fish', 'orange')
table.set_item('zebra', 'white')

table.print_table()
print(table.get_item('zebra'))
