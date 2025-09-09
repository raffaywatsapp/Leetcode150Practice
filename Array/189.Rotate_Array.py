from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n   # in case k > n

        # Step 1: reverse whole array
        l, r = 0, n - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        # Step 2: reverse first k elements
        l, r = 0, k - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        # Step 3: reverse remaining n-k elements
        l, r = k, n - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1


# Example
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3

obj = Solution()
obj.rotate(nums, k)

print(nums)   # Output → [5, 6, 7, 1, 2, 3, 4]
