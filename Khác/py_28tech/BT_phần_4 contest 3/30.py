import math


def check_fibo(n):
    if n == 1:
        return True
    fn1,fn2 = 1,1
    for i in range(2,100):
        fn = fn1 + fn2
        if fn == n:
            return True
        fn2,fn1 = fn1,fn

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        if check_fibo(n):
            print("YES")
        else:
            print("NO")
