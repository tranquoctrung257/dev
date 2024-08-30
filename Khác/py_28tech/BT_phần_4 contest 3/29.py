import math

def nt(n):
    if n < 2:
        return False
    for i in range(2,math.isqrt(n)+1):
        if n % i == 0:return False
    return True

def check_fibo(n):
    if n == 1:
        return True
    fn1,fn2 = 1,1
    for i in range(2,20):
        fn = fn1 + fn2
        if fn == n:
            return True
        fn2,fn1 = fn1,fn
    return False
def tong(n):
    s = 0
    while n != 0:
        s += n % 10
        n //= 10
    return s

if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        if nt(i) and check_fibo(tong(i)):
            print(i,end=" ")