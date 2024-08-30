import math

def check(n):
    temp = n
    rev = 0
    tong = 0
    ok = False
    while n != 0:
        rev = rev * 10 + n % 10
        if n % 10 == 6:
            ok = True
        tong += n % 10
        n //=10
    return ok and (temp == rev) and (tong % 10 == 8)

if __name__ == "__main__":
    a,b = map(int,input().split())
    for i in range(a,b+1):
        if check(i):
            print(i,end=" ")
    