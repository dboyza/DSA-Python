"""
DOUBLY LINKED LIST
GOOD FOR:
-REMOVING LAST ELEMENT IN CONSTANT TIME
-OPTIMIZED GET METHOD = OPTIMIZED INSERT/REMOVE

"""


# Create a doubly linked node
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# Doubly Linked List implementation
class DoublyLinkedList:
    # Double Linked List constructor
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    # Create a node and adds it to the beginning: O(1)
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

    # Create a node and adds it to the end: O(1)
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            new_node = self.head
            new_node = self.tail
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    # Removes the first node from the linked list: O(1)
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = temp.next
            self.head.prev = None
            temp.next = None
        return temp

    # Removes the last node from the linked list: O(n)
    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = temp.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp

    # Returns node at given index: O(n)
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length/2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp

    # Sets the value at the given index O(n)
    def set_value(self, index, value):
        temp = self.get(index)
        if temp is not None:
            temp.val = value
            return True
        return False

    # Create a node and inserts it at the given index: O(n)
    def insert(self, index, value):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)

        new_node = Node(value)

        before = self.get(index - 1)
        after = before.next

        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node

        self.length += 1
        return True

    # Removes a node from a particular index: O(n)
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first(index)
        if index == self.length:
            return self.pop(index)

        temp = self.get(index)
        before = temp.prev
        after = temp.next

        temp.prev = None
        temp.next = None
        before.next = after
        after.prev = before

        self.length -= 1
        return temp

    # Reverses the linked list: O(n)

    def reverse(self):
        pass

    # Prints out the entire linked list
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next


dll = DoublyLinkedList(0)
dll.append(1)
dll.append(4)
dll.append(3)

print(dll.get(3))
