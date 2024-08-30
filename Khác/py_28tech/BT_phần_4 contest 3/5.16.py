import math

def sum_digit(n):
    tong = 0
    while n != 0:
        tong += n % 10
        n //= 10
    return tong

def check(n):
    sum1 = sum_digit(n)
    sum2 = 0
    tmp = n
    for i in range(2,math.isqrt(n)+1):
        if n % i == 0:
            while n % i == 0:
                sum2 += sum_digit(i)
                n //= i
    if tmp == n:
        return False
    if n > 1:
        sum2 += sum_digit(n)
    return sum1 == sum2

if __name__ == "__main__":
    n = int(input())
    if check(n):
        print("YES")
    else:
        print("NO")