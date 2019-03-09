import math

test_num = 600851475143


def is_prime(i):
    if i % 2 == 0:
        return False

    max_div = math.ceil(math.sqrt(i))
    for x in range(1, max_div, 2):
        if i % x == 0:
            return False

    return True


max_prime = math.ceil(math.sqrt(test_num))
print("max_prime = " + str(max_prime))
primes = [2]
for i in range(3, max_prime, 2):
    if is_prime(i):
        primes.append(i)

print(primes)
for j in reversed(primes):
    if test_num % j == 0:
        print(j)
        break
