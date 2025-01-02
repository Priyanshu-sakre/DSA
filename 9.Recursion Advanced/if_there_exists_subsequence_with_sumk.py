from typing import List


def isSubsetPresent(n: int, k: int, a: List[int]) -> bool:
    def subset(k, a, i, sum1):
        if i == len(a):  # Base case
            return sum1 == k
        # Exclude the current element
        if subset(k, a, i + 1, sum1):
            return True
        # Include the current element
        if subset(k, a, i + 1, sum1 + a[i]):
            return True
        return False

    return subset(k, a, 0, 0)