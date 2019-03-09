for c in range(334, 501):
    for a in range(1, c):
        b = 1000 - c - a
        a_2 = a * a
        b_2 = b * b
        c_2 = c * c

        if a_2 + b_2 == c_2:
            if a + b + c == 1000:
                print(a, b, c)
                print(a * b * c)
