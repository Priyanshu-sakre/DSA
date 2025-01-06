class Solution:
    def subsetSums(self, arr):
        # Function to calculate all subsets
        def subset(ans, a, i, arr):
            if i == len(arr):
                ans.append(sum(a))  # Append the sum of the subset directly
                return
            subset(ans, a, i + 1, arr)  # Exclude the current element
            a.append(arr[i])  # Include the current element
            subset(ans, a, i + 1, arr)
            a.pop()  # Backtrack

        ans = []
        subset(ans, [], 0, arr)
        return ans
