import euler

max = 2000000
prime_sum = 2
for i in range(3, max, 2):
    if euler.is_prime(i):
        prime_sum += i

print(prime_sum)