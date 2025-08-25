"""
LeetCode #88: Merge Sorted Array

Problem:kk
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
Merge nkums2 into nums1 as one sorted array.
kkkk
Time Complexity: O(m+n)
Space Complexity: O(1)
"""

def merge(nums1, m, nums2, n):
    i, j, k = m - 1, n - 1, m + n - 1

    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1

# Example Test
nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
merge(nums1, 3, nums2, 3)
print(nums1)  # Output: [1,2,2,3,5,6]