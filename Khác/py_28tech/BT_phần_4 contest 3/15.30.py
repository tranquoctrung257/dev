import math

def check(n):
    donvi = n % 10
    while n != 0:
        if n % 10 > donvi:
            return False
        n //= 10
    return True


def nt(n):
    if n < 2 :return False
    for i in range(2,math.isqrt(n)+1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    n = int(input())
    dem = 0
    for i in range(1,n+1):
        if check(i) and nt(i):
            print(i,end=" ")
            dem +=1
    print("\n",dem,sep="")