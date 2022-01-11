"""
QUEUE IMPLEMENTATION W/ LINKED LIST
-ENQUEUE AT TAIL AND DEQUEUE AT HEAD: O(1)
"""


# Creates a linked list node
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# Queue implementation
class Queue:
    # Queue constructor
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1
    
    # Add a node to the queue - tail of the linked list: O(1)
    def enqueue(self, value):
        new_node = Node(value)
        if self.length == 0:
            new_node = self.first
            new_node = self.last
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    # Remove a node from the queue - head of the linked list: O(1)
    def dequeue(self):
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = temp.next
            temp.next = None
        self.length -= 1
        return temp

    # Print all queue values
    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next

queue = Queue(5)
queue.enqueue(1)
queue.enqueue(4)
queue.enqueue(7)
queue.dequeue()
queue.dequeue()
queue.dequeue()

queue.print_queue()