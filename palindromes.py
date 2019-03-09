import euler

min_prod = 100
max_prod = 999


a_palindromes = []
for i in range(999, 100, -1):
    for j in range(i, 100, -1):
        prod = i * j
        if euler.is_palindrome(prod):
            a_palindromes.append(prod)

print(max(a_palindromes))
