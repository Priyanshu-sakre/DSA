# brute
# better
# same as subarray approach
# optimal
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        rs = 0
        hash_map = {0: 1}
        count = 0
        for i in range(len(A)):
            rs = rs ^ A[i]
            x = rs ^ B
            count += hash_map.get(x, 0)
            hash_map[rs] = hash_map.get(rs, 0) + 1
        return count
