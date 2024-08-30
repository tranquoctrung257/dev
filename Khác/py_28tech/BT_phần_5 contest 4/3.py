def S(n):
    if n == 0:return 0
    return n ** 3 + S(n-1)

if __name__ == "__main__":
    n = int(input())
    print(S(n))