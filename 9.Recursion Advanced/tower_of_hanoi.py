n = 3
fromm = "A"
to = "C"
helper = "B"


def tower(n, fromm, to, helper):
    if n == 1:
        print(f"move disk {n} from {fromm} to {to}")
        return
    tower(n - 1, fromm, helper, to)
    print(f"move disk {n} from {fromm} to {to}")
    tower(n - 1, helper, to, fromm)


tower(n, fromm, to, helper)
