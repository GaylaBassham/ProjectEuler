import euler

min_prod = 100
max_prod = 999


double_pals = []
for i in range(1, 1000000):
    if euler.is_palindrome(i):
        bin_i = bin(i)[2:]
        if euler.is_palindrome(bin_i):
            double_pals.append(i)

print(double_pals)
print(sum(double_pals))
