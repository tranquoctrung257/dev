import math

def nt(n):
    if n < 2:
        return False
    for i in range(2,math.isqrt(n)+1):
        if n % i == 0:
            return False
    return True

def check(n):
    tong = 0
    while n != 0:
        r = n % 10
        if r != 2 and r != 3 and r != 5 and r != 7:
            return False
        tong += r
        n //= 10
    return nt(tong)

if __name__ == "__main__":
    a,b = map(int,input().split())
    dem = 0
    for i in range(a,b+1):
        if check(i) and nt(i):
            dem +=1
    print(dem)