class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        maxi = 0
        while i < j:
            width = j - i
            heigh = min(height[j], height[i])
            water = width * heigh
            maxi = max(maxi, water)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return maxi
