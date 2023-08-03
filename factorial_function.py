def factorial_by_recursion(a):
    if a < 2:
        return 1
    else:
        return a * factorial_by_recursion(a - 1)


def factorial_by_loop(a):
    result = 1
    if a < 2:
        return 1
    else:
        while a > 1:
            result *= a
            a -= 1
        return result


