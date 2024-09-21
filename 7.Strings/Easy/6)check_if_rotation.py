def rotation(s, goal):
    if len(s) == len(goal):
        if goal in s * 2:
            return True
    return False


s = "abcde"
goal = "cdeab"
print(rotation(s, goal))
