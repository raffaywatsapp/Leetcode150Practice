class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0  # pointer for new length
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k


if __name__ == "__main__":
    # Example input
    nums = [3, 2, 2, 3]
    val = 3

    sol = Solution()
    k = sol.removeElement(nums, val)

    print("New length:", k)
    print("Array after removal:", nums[:k])
" code"