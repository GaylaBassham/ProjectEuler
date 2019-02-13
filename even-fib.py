if __name__ == '__main__':
    fib = 5
    prev_fib = 3
    prev_prev_fib = 2
    fib_sum = 2
    while fib < 4000000:
        prev_prev_fib = prev_fib
        prev_fib = fib
        fib = prev_prev_fib + prev_fib

        if fib % 2 == 0:
            fib_sum += fib

    print(fib_sum)
