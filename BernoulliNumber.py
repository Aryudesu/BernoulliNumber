import math
import combination


def inputNum(mes="InputNum > "):
    while True:
        try:
            print(mes, end="")
            return int(input())
        except:
            print('Input "Num" Please')


def calcBernoulli(num):
    res = [[1, 1]]
    for i in range(1, num + 1):
        numer, denom = res[0][0] * combination.combination(i + 1, 0), res[0][1]
        for j in range(1, i):
            numer = numer * res[j][1] + denom * res[j][0] * combination.combination(
                i + 1, j
            )
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


num = inputNum()
ber = calcBernoulli(num)
for idx in range(num + 1):
    if ber[idx][0]:
        print(f"B_{idx} = {ber[idx][0]} / {ber[idx][1]}")
    else:
        print(f"B_{idx} = 0")
