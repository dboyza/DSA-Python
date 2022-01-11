"""
MERGESORT IMPLEMENTATION
-Breaks list of numbers in half recursively then combines solutions
-Time Complexity: O(nlogn) <--- The best for sorting algorithms
-Space Complexity: O(n)
"""


# Merge helper function: O(n)
# -Takes 2 lists as parameters and combines them into a sorted list
def merge(nums1, nums2):
    combined = []
    i = 0
    j = 0

    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            combined.append(nums1[i])
            i += 1
        else:
            combined.append(nums2[j])
            j += 1
    while i < len(nums1):
        combined.append(nums1[i])
        i += 1
    while j < len(nums2):
        combined.append(nums2[j])
        j += 1
    return combined


# Breaks lists in half using recursion: O(nlogn); Space: O(n)
def merge_sort(nums):
    if len(nums) == 1:
        return nums
    mid = len(nums)//2
    left = nums[:mid]
    right = nums[mid:]
    return merge(merge_sort(left), merge_sort(right))


#print(merge([1, 2, 7, 8], [3, 4, 5, 6]))
print(merge_sort([4, 2, 6, 5, 1, 3]))
