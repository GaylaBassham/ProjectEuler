max = 100

sum_square = 0
for i in range(1, max + 1):
    sum_square = sum_square + (i * i)

sum = (1 + max) * (max / 2)
square_sum = sum * sum

print(square_sum - sum_square)
