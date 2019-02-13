import math


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def is_prime(i):
    if i % 2 == 0:
        return False

    max_div = math.ceil(math.sqrt(i))
    for x in range(3, max_div, 2):
        if i % x == 0:
            return False

    return True


prod = 1
for x in range(20, 1, -1):
    if prod % x == 0:
        continue

    if is_prime(x) or prod == 1:
        prod = prod * x
    else:
        if prod % x != 0:
            prod = prod * (x // gcd(prod, x))

print(prod)
