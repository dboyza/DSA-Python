"""
INSERTION SORT IMPLEMENTATION
Loop through the numbers starting at index 1
Compare current number to each of the previous numbers during while loop
Keep moving number back until it is in the correct place
"""


# Selection Sort: O(n^2); O(n) if sorted/almost sorted
def insertion_sort(nums):
    for i in range(1, len(nums)):
        temp = nums[i]
        j = i-1
        # Do swaps until the number is in the correct place
        while temp < nums[j] and j > -1:
            nums[j+1] = nums[j]
            nums[j] = temp
            j -= 1
    # Return the sorted list
    return nums


print(insertion_sort([4, 2, 6, 5, 1, 3]))
