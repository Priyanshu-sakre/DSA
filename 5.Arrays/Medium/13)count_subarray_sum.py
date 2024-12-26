class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum1 = 0
        hash_map = {0: 1}
        count = 0
        for num in nums:
            sum1 += num
            if sum1 - k in hash_map:
                count += hash_map[sum1 - k]
            hash_map[sum1] = hash_map.get(sum1, 0) + 1
        return count
