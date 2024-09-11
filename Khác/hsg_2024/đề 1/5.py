def SL(n):
    if n < 1:
        return 0
    elif n % 2 != 0:
        return n + SL(n - 2)
    else:
        return SL(n - 1)

print(SL(10))
