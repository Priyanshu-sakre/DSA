"""https://www.geeksforgeeks.org/problems/frequency-of-array-elements-1587115620/0"""
class Solution:
    # Function to count the frequency of all elements from 1 to N in the array.
    def frequencyCount(self, arr, N, P):
        #  do modify in the given array
        f = [0] * N
        for i in arr:
            if i > N:
                continue
            f[i - 1] += 1
        for i in range(len(f)):
            arr[i] = f[i]
