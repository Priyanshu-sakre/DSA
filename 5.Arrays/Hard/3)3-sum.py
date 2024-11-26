# brute
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        st = set()
        for i in range(len(nums)):
            hash_map = {}
            for j in range(i + 1, len(nums)):
                k = -(nums[i] + nums[j])
                if k in hash_map:
                    temp = [nums[i], nums[j], k]
                    temp.sort()
                    st.add(tuple(temp))
                hash_map[nums[j]] = 1
        ans = [list(items) for items in st]
        return ans


# better
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        st = set()
        for i in range(len(nums)):
            hash_map = {}
            for j in range(i + 1, len(nums)):
                k = -(nums[i] + nums[j])
                if k in hash_map:
                    temp = [nums[i], nums[j], k]
                    temp.sort()
                    st.add(tuple(temp))
                hash_map[nums[j]] = 1
        ans = [list(items) for items in st]
        return ans
# optimal
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                sum1 = nums[i] + nums[j] + nums[k]
                if sum1 < 0:
                    j += 1
                elif sum1 > 0:
                    k -= 1
                else:
                    temp = [nums[i], nums[j], nums[k]]
                    ans.append(temp)
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
        return ans
