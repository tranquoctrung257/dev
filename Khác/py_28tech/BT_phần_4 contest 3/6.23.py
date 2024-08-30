import math

def tong_uoc(n):
    tong = 0
    for i in range(1,math.isqrt(n)+1):
        if n % i == 0:
            tong += i
            if i != n//i:
                tong += n //i
    return tong

if __name__ == "__main__":
    n = int(input())
    print(tong_uoc(n)) 