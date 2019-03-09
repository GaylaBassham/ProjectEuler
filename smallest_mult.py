import euler

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

prod = 1
for x in range(20, 1, -1):
    if prod % x == 0:
        continue

    if euler.is_prime(x) or prod == 1:
        prod = prod * x
    else:
        if prod % x != 0:
            prod = prod * (x // gcd(prod, x))

print(prod)
