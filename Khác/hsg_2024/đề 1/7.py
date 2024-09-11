def giaiThua(n):
    if n == 1:
        return 1
    return n * giaiThua(n-1)

print(giaiThua(5))