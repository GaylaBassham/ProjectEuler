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


def is_right_triangle(sides):
    abc = sorted(sides)
    hypotenuse = abc[2] ** 2
    ab = abc[0] ** 2 + abc[1] ** 2
    return hypotenuse == ab


def is_pandigital(n):
    str_n = str(n)
    sorted_n = sorted(str_n)

    ctr = 1
    for x in sorted_n:
        if int(x) != ctr:
            return False
        ctr += 1
    return True
