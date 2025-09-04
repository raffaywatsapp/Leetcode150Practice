from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res, count = 0, 0   # res = candidate, count = its vote strength

        for n in nums:
            if count == 0:          # no candidate yet
                res = n             # pick current number as candidate
            count += 1 if n == res else -1  # vote for / against candidate

        return res


# ---------- quick test ----------
if __name__ == "__main__":
    nums = [2, 2, 1, 1, 1, 2, 2]
    obj = Solution()
    print("Majority Element:", obj.majorityElement(nums))
