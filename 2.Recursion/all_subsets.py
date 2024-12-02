def all_subsets(n, curr="", i=0):
    if i == len(n):
        print(f"'{curr}'", end=" ")
        return
    all_subsets(n, curr, i + 1)
    all_subsets(n, curr + n[i], i + 1)


n = "ABC"
all_subsets(n)
