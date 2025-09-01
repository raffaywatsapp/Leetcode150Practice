from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        l = 1  # left pointer (where next unique element goes)
        for r in range(1, len(nums)):  # right pointer scans the array
            if nums[r] != nums[r - 1]:  # found a new unique element
                nums[l] = nums[r]
                l += 1

        return l


# Example usage:
if __name__ == "__main__":
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    sol = Solution()
    k = sol.removeDuplicates(nums)

    print("Number of unique elements:", k)
    print("Array after removing duplicates:", nums[:k])
