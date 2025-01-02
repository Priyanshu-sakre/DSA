n = 3
fromm = "A"
to = "C"
helper = "B"


def tower(n, fromm, to, helper):
    if n == 1:
        print(f"move disk {n} from {fromm} to {to}")
        return
    tower(n - 1, fromm, to, helper)
    print(f"move disk {n} from {fromm} to {to}")
    tower(n - 1, helper, fromm, to)


tower(n, fromm, to, helper)
