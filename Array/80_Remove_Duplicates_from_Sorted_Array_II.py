def remove_duplicates(nums):
    if len(nums) <= 2:
        return len(nums)

    j = 2  # pointer for next valid spot
    for i in range(2, len(nums)):
        if nums[i] != nums[j - 2]:
            nums[j] = nums[i]
            j += 1

    return j


# ---- Test it ----
nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
length = remove_duplicates(nums)

print("New length:", length)
print("Modified array:", nums[:length])  # only take first 'length' elements
