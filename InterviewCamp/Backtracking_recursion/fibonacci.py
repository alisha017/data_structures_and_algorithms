# 1,1,2,3,5,8,13,21,34,55
def get_fibonacci(num):

    # edge case
    if num < 1:
        return -1
    # base case
    if num == 1 or num == 2:
        return 1
    else:
        # recursion expression
        return get_fibonacci(num - 1) + get_fibonacci(num - 2)


def get_fibonacci_memoized(num, fib_map):
    if num < 1:
        return -1
    if num == 1 or num == 2:
        return 1
    if fib_map.get(num) is not None:
        return fib_map[num]

    result = get_fibonacci_memoized(num-1, fib_map) + get_fibonacci_memoized(num-2, fib_map)
    fib_map[num] = result
    return result


if __name__ == '__main__':
    print(get_fibonacci(7))
    print(get_fibonacci_memoized(16, {}))

