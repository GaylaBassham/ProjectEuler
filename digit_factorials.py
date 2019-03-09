import math

factorials = [1]
for i in range(1, 10):
    factorials.append(math.factorial(i))
print(factorials)

total_sum = 0
for i in range(10, factorials[9] * 7):
    temp = i
    dig_fact_sum = 0
    while temp > 0:
        dig_fact_sum += factorials[temp % 10]
        temp //= 10

    if i == 40585:
        print(dig_fact_sum)

    if dig_fact_sum == i:
        total_sum += i

print(total_sum)
