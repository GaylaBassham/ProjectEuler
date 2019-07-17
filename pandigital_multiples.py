def has_doubles(n):
    return len(set(str(n))) < len(str(n))


for i in range(9999, 9001, -1):
    if not has_doubles(i):
        second_half = i * 2
        if not has_doubles(second_half):
            pandigital = str(i) + str(second_half)
            if not has_doubles(int(pandigital)):
                print(pandigital)
