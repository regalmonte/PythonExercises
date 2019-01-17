# Uses python3


def findPeriod(n, m):
    global FiboNumbers
    p = [0, 1, 1]
    s = [0, 1, 2]
    for i in range(1, n):
        p.append((p[-1] + p[-2]) % 10)
        s.append((s[-1] + p[-1]) % 10)
        if p[-3] % m == 0 and p[-2] % m == 1 and p[-1] % m == 1:
            FiboNumbers = s
            return i
    FiboNumbers = s
    return n+1


def fibonacci_sum_fast(n):
    if n <= 1:
        return n

    period = findPeriod(n, 10)
    return FiboNumbers[n % period]


def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_fast(n))
    print(fibonacci_sum_naive(n))
