counts = {}
for m in range(2, 20):
    for n in range(1, m):
        print(m, n)
        a = m ** 2 - (n ** 2)
        b = 2 * n * m
        c = n ** 2 + (m ** 2)

        print(a, b, c)
        print(a + b + c)
        perimeter = a + b + c
        if perimeter > 1000:
            continue

        if perimeter in counts:
            counts[perimeter] += 1
        else:
            counts[perimeter] = 1

print({i: v for i, v in counts.items() if v > 1})
print(counts)