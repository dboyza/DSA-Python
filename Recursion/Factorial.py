"""
Recursion - A function that calls iteself until it doesn't
"""

# Calculates and returns the factorial of the passed parameter n
def factorial(n):
    # Base case
    if n == 1:
        return 1
    # Recursive case
    return n * factorial(n-1)

print(factorial(4))