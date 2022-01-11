"""
BINARY SEARCH TREE IMPLEMENTATION
GOOD FOR: 
-FINDING/INSERTING/GETTING A SPECIFIC NODE 
-IN AVERAGE CASE O(LOGN), WORST CASE O(N)

"""


# Creates a tree node
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Binary Search Tree implementation
class BinarySearchTree:
    # Binary Search Tree constructor
    def __init__(self):
        self.root = None

    # Insert a node into the BST: O(n), Theta(logn)
    def insert(self, value):
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
            return True

        curr = self.root
        while True:
            # Don't insert if same value is in the tree
            if new_node.value == curr.value:
                return False
            # Go left
            if new_node.value < curr.value:
                if curr.left is None:
                    curr.left = new_node
                    return True
                curr = curr.left
            # Go right
            else:
                if curr.right is None:
                    curr.right = new_node
                    return True
                curr = curr.right

    # Return if the value is in the BST (True/False): O(n), Theta(logn)
    def contains(self, value):
        curr = self.root
        while curr:
            # Go left
            if value < curr.value:
                curr = curr.left
            # Go right
            elif value > curr.value:
                curr = curr.right
            # Return the node
            else:
                return True
        return False

    # Return the smallest tree in the inputted tree: O(n)
    def min_value(self, curr_node):
        curr = curr_node
        while curr_node.left:
            curr_node = curr_node.left
        return curr_node  # .value

    # Return the largest node in the inputted tree: O(n)
    def max_value(self, curr_node):
        curr = curr_node
        while curr_node.right:
            curr_node = curr_node.right
        return curr_node  # .value
    
    # Breadth First Search implementation
    def BFS(self):
        curr = self.root
        queue = []
        results = []
        queue.append(curr)
        
        while len(queue) > 0:
            curr = queue.pop(0)
            results.append(curr)
            if curr.left is not None:
                queue.append(curr.left)
            if curr.right is not None:
                queue.append(curr.right)
        return results
    
    
    # Depth First Search PRE-ORDER implementation using recursion (call stack)
    def dfs_pre_order(self):
        results = []
        def traverse(curr):
            results.append(curr)
            if curr.left is not None:
                traverse(curr.left)
            if curr.right is not None:
                traverse(curr.right)
        traverse(self.root)
        return results
    
    # Depth First Search POST-ORDER implementation using recursion (call stack)
    def dfs_post_order(self):
        results = []
        def traverse(curr):
            if curr.left is not None:
                traverse(curr.left)
            if curr.right is not None:
                traverse(curr.right)
            results.append(curr)
        traverse(self.root)
        
        
    # Depth First Search IN-ORDER (numerical with BST) implementation using
    # recursion (call stack)
    def dfs_in_order(self):
        results = []
        def traverse(curr):
            if curr.left is not None:
                traverse(curr.left)
            results.append(curr)
            if curr.right is not None:
                traverse(curr.right)
        traverse(self.root)

tree = BinarySearchTree()
tree.insert(2)
tree.insert(1)
tree.insert(55)
tree.insert(43)
tree.insert(2)
tree.insert(8)
print(tree.contains(0))
print(tree.min_value(tree.root))
print(tree.max_value(tree.root))
