from typing import List


# brute
def longestSuccessiveElements(a: List[int]) -> int:
    count = 1
    for i in a:
        count_2 = 1
        for j in range(1, len(a)):
            if i + j in a:
                count_2 += 1
            else:
                break
            count = max(count, count_2)
    return count


a = [5, 8, 3, 2, 1, 4]
print(longestSuccessiveElements(a))


# better
def longestSuccessiveElements2(a: List[int]) -> int:
    a.sort()
    longest = 1
    count = 0
    last_small = 0
    for i in range(len(a)):
        if a[i] - 1 == last_small:
            count += 1
            last_small = a[i]
        elif a[i] != last_small:
            count = 1
            last_small = a[i]
        longest = max(count, longest)
    return longest


print(longestSuccessiveElements2(a))


# optimal
def longestSuccessiveElements3(a: List[int]) -> int:
    s = set(a)
    longest = 1
    for i in s:
        if i - 1 in s:
            continue
        else:
            x = i
            count = 1
            while x + 1 in s:
                x += 1
                count += 1
            longest = max(longest, count)
    return longest


print(longestSuccessiveElements3(a))
