def fib(a):
    if a <= 0:
        return []
    elif a == 1:
        return [0]

    res = [0, 1]
    for i in range(a - 2):
        res.append(res[-1] + res[-2])
    return res
