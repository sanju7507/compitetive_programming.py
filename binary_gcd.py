A, B = map(int, input().split())

gcd = 1

while A != B:
    if A % 2 == 0 and B % 2 == 0:
        gcd *= 2
        A //= 2
        B //= 2
    elif A % 2 == 0:
        A //= 2
    elif B % 2 == 0:
        B //= 2
    elif A > B:
        A = (A - B) // 2
    else:
        B = (B - A) // 2

print(gcd * A)
