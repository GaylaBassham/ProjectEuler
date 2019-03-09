import euler

max = 1000000

primes = {}
primes[2] = 1

for i in range(3, max, 2):
    if euler.is_prime(i):
        primes[i] = 0

circular = set()
circular.add(2)
for i in range(3, max, 2):
    print(i)
    if i in primes:
        if primes[i] != 1:
            print(str(i) + " is a prime")
            primes[i] = 1
            rotated_i = str(i)

            i_len = len(rotated_i)
            is_circular = True
            temp = set()
            for digit in range(0, i_len):
                rotated_i = rotated_i[1:] + rotated_i[0]
                print("rotating to " + rotated_i)
                int_rotated = int(rotated_i)
                if int_rotated in primes:
                    primes[int_rotated] = 1
                    temp.add(int_rotated)
                    print(rotated_i + " is a prime")
                else:
                    is_circular = False
                    break
            if is_circular:
                for n in temp:
                    circular.add(n)
        print()

print(circular)
print(primes)
print(len(circular))
