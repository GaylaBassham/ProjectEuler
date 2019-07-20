solutions = {}
for p in range(12, 1001):
    print(p)
    solutions[p] = 0
    for a in range(1, (p // 3) - 1):
        for b in range(a + 1, p // 2):
            c = p - a - b
            if (a + b) > c:
                if c > 0:
                    if c > a and c > b:
                        if ((a ** 2) + (b ** 2)) == (c**2):
                            solutions[p] += 1
    print(str(solutions[p]), " for ", str(p))
filtered_solutions = {key:value for key, value in solutions.items() if value != 0}
print(filtered_solutions)
print(sorted(filtered_solutions.items(), key=lambda x: x[1], reverse = True))