import math


def get_length(i):
    return int(math.log10(i)) + 1


if __name__ == '__main__':
    num = 1
    nums_to_find = [1, 10, 100, 1000, 10000, 100000, 1000000]
    running_product = 1
    num_pos = 0
    running_count = 0
    current_num = nums_to_find[num_pos]
    while True:
        val = get_length(num)
        running_count += val
        if running_count >= current_num:
            digits_past = running_count - current_num
            s_num = str(num)
            digit = s_num[len(s_num) - digits_past - 1]
            running_product *= int(digit)

            num_pos += 1
            if num_pos == len(nums_to_find):
                break
            else:
                current_num = nums_to_find[num_pos]

        num += 1
    print(running_product)
