# Uses python3


def findPeriod(n):
    global FiboSums
    s = [0, 1, 2]
    for i in range(1, n):
        s.append((s[-1] + s[-2] + 1) % 10)
        if s[-3] == 0 and s[-2] == 1 and s[-1]  == 2:
            FiboSums = s
            return i
    FiboSums = s
    return n+1


def fibonacci_sum_fast(n):
    if n <= 1:
        return n

    period = findPeriod(n)
    return FiboSums[n % period]


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
