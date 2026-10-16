from math import gcd

def capacity(a, b, t):
    if a == 0 or b == 0:
        return 0

    return 'YES' if t % gcd(a, b) == 0 else 'NO'


a, b, t = map(int, input().split())
print(capacity(a, b, t))
