# brute 1
def two_sum(nums, n, target):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            else:
                if nums[i] + nums[j] == target:
                    return [i, j]


nums = [2, 7, 11, 15]
n = len(nums)
target = 9
print(two_sum(nums, n, target))


# brute 2
def two_sum2(nums, n, target):
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]


"""
both have nearly same tc
TC->O(N^2)
SC->O(1)
"""

print(two_sum2(nums, n, target))


# one more
def two_sum3(nums, n, target):
    for i in range(n):
        j = target - nums[i]
        if j in nums and nums.index(j) != i:
            return [i, nums.index(j)]


print(two_sum3(nums, n, target))


# better for (yes/no) type but optimal for (index) types
def two_sum4(nums, n, target):
    hash_map = {}
    for i in range(n):
        a = nums[i]
        b = target - a
        if b in hash_map:
            return [hash_map[b], i]
        else:
            hash_map[a] = i


print(two_sum4(nums, n, target))


# optimal
def two_sum5(book, n, target):
    book.sort()
    i = 0
    j = n - 1
    while i < j:
        s = book[i] + book[j]
        if s > target:
            j -= 1
        elif s < target:
            i += 1
        else:
            return "YES"
    return "NO"


book = [4, 1, 2, 3, 1]
n = len(book)
target = 5
print(two_sum5(book, n, target))
