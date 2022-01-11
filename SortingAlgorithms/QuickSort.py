"""
QUICKSORT IMPLEMENTATION
-Pick pivot as first item in list
-Separate numbers in list in 2 groups:
    1. Less than pivot
    2. Greater than pivot
-Swap pivot and last element in the Less than pivot group
-Recursively call pivot on left and right halves until list is sorted
AVERAGE CASE: O(nlogn)
WORST CASE (already sorted data): O(n^2)
"""


# Swap helper function
# -swaps 2 numbers in the list
def swap(nums, index1, index2):
    temp = nums[index1]
    nums[index1] = nums[index2]
    nums[index2] = temp


# Pivot helper function: O(n)
# -pivot is first item in list
# -i starts at first number after pivot
# -swap_index starts at pivot
def pivot(nums, pivot_index, end_index):
    swap_index = pivot_index
    for i in range(pivot_index+1, end_index+1):
        if nums[i] < nums[pivot_index]:
            swap_index += 1
            swap(nums, swap_index, i)
    swap(nums, pivot_index, swap_index)
    return swap_index

# Quick sort helper function: O(logn)


def quick_sort_helper(nums, left, right):
    if left < right:
        pivot_index = pivot(nums, left, right)
        quick_sort_helper(nums, left, pivot_index-1)
        quick_sort_helper(nums, pivot_index+1, right)
    return nums


# Quick sort: O(nlogn)
def quick_sort(nums):
    return quick_sort_helper(nums, 0, len(nums)-1)


print(quick_sort([4, 6, 1, 7, 3, 2, 5]))
