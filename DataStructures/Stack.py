"""
STACK IMPLEMENTATION W/ LINKED LIST
-TOP OF THE STACK IS THE HEAD OF THE LINKED LIST
-PUSH/POP FROM TOP OF THE STACK: O(1)
"""


# Creates a linked list node
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# Stack implementation
class Stack:
    # Stack constructor
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    # Push a new node onto the top of the stack: O(1)
    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1

    # Pop a node from the top of the stack: O(1)
    def pop(self):
        if self.height == 0:
            return None
        temp = self.top
        self.top = temp.next
        temp.next = None
        self.height -= 1
        return temp

    # Print all stack values
    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

stack = Stack(1)
stack.push(3)
stack.push(24)
stack.push(87)
stack.pop()

stack.print_stack()