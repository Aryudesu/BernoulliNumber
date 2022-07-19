import math


def combination(a, b):
    n, m = a, b
    if n < 2 * m:
        m = n - m
    if n == m or m == 0:
        return 1
    tmp = [n - i for i in range(m)]
    for i in range(1, m + 1):
        for j in range(m):
            if not tmp[j] % i:
                tmp[j] //= i
                break
    result = 1
    for i in tmp:
        result *= i
    return result


def calcBernoulli(num):
    res = [[1, 1]]
    for i in range(1, num + 1):
        numer, denom = res[0][0] * combination(i + 1, 0), res[0][1]
        for j in range(1, i):
            numer = numer * res[j][1] + denom * res[j][0] * combination(i + 1, j)
            denom = denom * res[j][1]
            if numer:
                g = math.gcd(numer, denom)
                numer //= g
                denom //= g
        numer *= -1
        denom *= i + 1
        if (numer < 0 and denom < 0) or (numer > 0 and denom < 0):
            numer = -numer
            denom = -denom
        if not numer:
            denom = 1
        else:
            g = math.gcd(abs(numer), abs(denom))
            numer //= g
            denom //= g
        res.append([numer, denom])
    return res


num = 10
ber = calcBernoulli(num + 1)
for idx in range(num + 2):
    print(f"B_{idx} = {ber[idx][0]} / {ber[idx][1]}")
