# python3


def slow_max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                              numbers[first] * numbers[second])
    return max_product


def fast_max_pairwise_product(numbers):
    max1 = 0
    max2 = 0
    for i in numbers:
        if max1 < i:
            max2 = max1
            max1 = i
        elif max2 < i:
            max2 = i
    return max1*max2


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(fast_max_pairwise_product(input_numbers))
