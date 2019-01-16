# Uses python3


def calc_fib(n):
    p = [0, 1]
    for i in range(n-1):
        p[-2], p[-1] = p[-1], p[-1] + p[-2]
    return p[-1] if n else n


def slow_calc_fib(n):
    if n < 2:
        return n
    return slow_calc_fib(n-1) + slow_calc_fib(n-2)


if __name__ == '__main__':
    n = int(input())
    print(calc_fib(n))
