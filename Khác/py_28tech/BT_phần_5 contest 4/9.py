import math

def binpow(a,b):
    if b == 0:
        return 1
    # đi tính a^b//2
    x = binpow(a,b // 2)
    if b % 2 == 1:
        return x * x * a % (10 ** 9 +7)
    else:
        return x * x % (10 ** 9 +7)

if __name__ == "__main__":
    a,b = map(int,input().split())
    print(binpow(a,b))