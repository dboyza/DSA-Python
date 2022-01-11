"""
SELECTION SORT IMPLEMENTATION
Smallest number is found in each iteration and sorted by "appending"
to the end of the already sorted section of the list
"""

# Selection Sort: O(n^2)
def selection_sort(nums):
    # i starts at beginning of list and goes to end-1
    # since the last number will already be sorted
    for i in range(len(nums)-1):
        # Index of the minimum value is initially set to the index of
        # the first element after the sorted section of the list
        min_index = i
        for j in range(i+1, len(nums)):
            # Find the new minimum index
            if nums[j] < nums[min_index]:
                min_index = j
        # "Append" newly found minimum value to the end of the sorted section of the list
        if i != min_index:
            temp = nums[i]
            nums[i] = nums[min_index]
            nums[min_index] = temp
    # Return the sorted list
    return nums


print(selection_sort([4, 2, 6, 5, 1, 3]))
