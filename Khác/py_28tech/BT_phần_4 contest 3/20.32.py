import math

def solve(n,k):
    dem = 0
    for i in range(2,math.isqrt(n)+1):
        if n % i == 0:
            while n % i == 0:
                dem += 1
                if dem == k:
                    return i
                n //= i
    if n != 1:
        dem +=1
    if dem == k:
        return n
    return -1
if __name__ == "__main__":
    n,k = map(int,input().split())
    print(solve(n,k))