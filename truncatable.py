import euler

max = 1000000

primes = [i for i in range(3, max, 2) if euler.is_prime(i)]
primes.append(2)

trunc_primes = []
for num in primes:
    if num > 10:
        s_num = str(num)
        digits = len(s_num)

        for i in range(1, digits):
            trunc = (int(s_num[i:]) in primes) and (int(s_num[:i]) in primes)
            if not trunc:
                break

        if trunc:
            trunc_primes.append(num)

    if len(trunc_primes) >= 11:
        break

print(primes)
print(trunc_primes)
print(sum(trunc_primes))