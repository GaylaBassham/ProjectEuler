import math


def is_prime(i):
    if i % 2 == 0:
        return False

    max_div = math.ceil(math.sqrt(i)) + 1
    for x in range(3, max_div, 2):
        if i % x == 0:
            return False

    return True


def is_palindrome(n):
    str_n = str(n)
    return str_n == str_n[::-1]
