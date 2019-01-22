# Uses python3
import sys


def findPeriod(n, m):
    global FiboSums
    p = [0, 1, 1]
    s = [0, 1, 2]
    for i in range(0, (n % 60)):
        p[-3], p[-2], p[-1] = p[-2], p[-1], (p[-1]+p[-2])%10
        s[-3], s[-2], s[-1] = p[-3], (p[-3] + p[-2]) % 10, (p[-3] + p[-2] + p[-1]) % 10
    q = list(p)
    t = 0
    for i in range(n, m-2):
        t += 1
        q.append((q[-1] + q[-2]) % 10)
        s.append((s[-1] + q[-1]) % 10)
        if q[-3] == p[-3] and q[-2] == p[-2] and q[-1] == p[-1]:
            FiboSums = s
            return t
    FiboSums = s
    return m-n+1


def fibonacci_partial_sum_fast(from_, to):
    period = findPeriod(from_, to)
    #print(FiboSums)
    return FiboSums[(to - from_) % period]

def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next  = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

    return sum % 10


if __name__ == '__main__':
    inp = input("Two digits separated by a space:");
    from_, to = map(int, inp.split())
    print(fibonacci_partial_sum_fast(from_, to))
    print(fibonacci_partial_sum_naive(from_, to))