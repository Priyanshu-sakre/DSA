# brute same as before
# better
class Solution:
    def maxLen(self, arr):
        # code here
        maxl = 0
        sum1 = 0
        hash_map = {}
        for i in range(len(arr)):
            sum1 += arr[i]
            if sum1 == 0:
                maxl = i + 1
            rem = sum1 - 0
            if rem in hash_map:
                l1 = i - hash_map[rem]
                maxl = max(maxl, l1)
            if sum1 not in hash_map:
                hash_map[sum1] = i
        return maxl
