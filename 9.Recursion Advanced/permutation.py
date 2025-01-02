nums = [1, 2, 3]
ans = []
index = 0


def permutation(nums, ans, index):
    if index == len(nums):
        ans.append(nums.copy())
        return
    for i in range(index, len(nums)):
        nums[index], nums[i] = nums[i], nums[index]
        permutation(nums, ans, index + 1)
        nums[index], nums[i] = nums[i], nums[index]


permutation(nums, ans, index)
print(ans)
