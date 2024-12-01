def prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def prime_factor(n):
    for i in range(2, n + 1):
        if prime(i):
            x = i
            while n % x == 0:
                print(i, end=" ")
                x *= i


n = 100
prime_factor(100)
