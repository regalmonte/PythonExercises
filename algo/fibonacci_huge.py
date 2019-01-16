# Uses python3
import sys
FiboNumbers = []


def findPeriod(n, m):
    global FiboNumbers
    p = [0, 1, 1]
    for i in range(1, n):
        p.append(p[-1] + p[-2])
        if p[-3] % m == 0 and p[-2] % m == 1 and p[-1] % m == 1:
            FiboNumbers = p
            return i
    FiboNumbers = p
    return n


def get_fibonacci_huge_fast(n, m):
    if n < 2:
        return n
    period = findPeriod(n, m)
    print(FiboNumbers)
    print(n, m, period)
    return FiboNumbers[n % period] % m


def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m


print("input 2 integers (n, m):", end=" ")
input = sys.stdin.read();
n, m = map(int, input.split())
print(get_fibonacci_huge_fast(n, m))
print(get_fibonacci_huge_naive(n, m))
