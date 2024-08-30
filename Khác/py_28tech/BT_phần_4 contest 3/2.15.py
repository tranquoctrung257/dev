import math

def spenic(n):
    cnt = 0
    for i in range(2,math.isqrt(n)+1):
        if n % i == 0:
            mu = 0
            while n % i == 0:
                mu+=1
                n//= i
            if mu >= 2:
                return False
            cnt += 1
    if cnt > 1:
        cnt += 1
    return cnt == 3

if __name__ == "__main__":
    n = int(input())
    if spenic(n):
        print("1")
    else:
        print("0")