import euler
import itertools

digits_list = []
for i in range(3, 10):
    l = list(range(1, i + 1))
    digits_list.append(l)

digits_list = digits_list[::-1]
print(digits_list)

for x_list in digits_list:
    x_perms = list(itertools.permutations(x_list))
    x_perms = sorted(x_perms)
    x_perms = x_perms[::-1]
    for num_tup in x_perms:
        num = ''.join(map(str, num_tup))
        if euler.is_prime(int(num)):
            print(num)

