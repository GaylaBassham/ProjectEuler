import euler

max = 1000000

primes = [2]

for i in range(3, max, 2):
    if euler.is_prime(i):
        primes.append(i)
print("finished generating primes")

trunc_primes = []
for num in primes:
    if num > 10:
        s_num = str(num)
        digits = len(s_num)

        trunc = True
        for i in range(1, digits):
            nleft = int(s_num[i:])
            nright = int(s_num[:i])

            if num == 3797:
                print(nleft)
                print(nright)

            if nleft not in primes:
                if num == 3797:
                    print("left not in primes")
                trunc = False
                break

            if nright not in primes:
                if num == 3797:
                    print("right not in primes")
                trunc = False
                break

        if trunc:
            trunc_primes.append(num)

    if len(trunc_primes) >= 11:
        break

print(primes)
print(trunc_primes)
print(sum(trunc_primes))