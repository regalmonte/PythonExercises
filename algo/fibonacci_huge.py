# Uses python3
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
    return n + 1


def get_fibonacci_huge_fast(n, m):
    if n < 2:
        return n
    period = findPeriod(n, m)
    return FiboNumbers[n % period] % m


def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m


if __name__ == '__main__':
    print("input 2 integers (n, m):", end=" ")
    inp = input()
    n, m = map(int, inp.split())
    print(get_fibonacci_huge_fast(n, m))
    print(get_fibonacci_huge_naive(n, m))
