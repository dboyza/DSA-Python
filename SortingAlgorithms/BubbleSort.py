"""
BUBBLE SORT IMPLEMENTATION
"Bubble up" largest number to the end of the list during each iteration
Each iteration does not make comparisons to the "bubbled" number
"""

# Bubble Sort: O(n^2)
def bubble_sort(nums):
    # i starts at the end of list and decrements by 1 since a num gets "bubbled up"
    for i in range(len(nums) - 1, 0, -1):
        # Swaps happen every time a number is less than the next to move it up in the list
        for j in range(i):
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp
        # Largest num not "bubbled" is now "bubbled up"
    # Return the sorted list
    return nums


print(bubble_sort([4, 2, 6, 5, 1, 3]))
