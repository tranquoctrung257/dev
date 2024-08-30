import math

def tn(n):
    temp = n
    rev = 0
    while n != 0:
        rev = rev * 10 + n % 10
        n //= 10
    return rev == temp

def check(n):
    dem = 0
    for i in range(2,math.isqrt(n)+1):
        if n % i == 0:
            dem +=1
            while n % i == 0:
                n //= i
    if n != 1:
        dem +=1
    return dem >=3

if __name__ == "__main__":
    a,b = map(int,input().split())
    dem = 0
    for i in range(a,b+1):
        if tn(i) and check(i):
            print(i,end=" ")
            dem+=1
    if dem == 0:
        print(-1)