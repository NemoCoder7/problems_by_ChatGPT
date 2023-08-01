from math import sqrt


def prime_num(a):
    for i in range(2, round(sqrt(a))):
        if a % i == 0:
            return False
        else:
            return True