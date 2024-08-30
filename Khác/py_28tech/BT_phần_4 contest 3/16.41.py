import math

def tn(n):
    rev = 0
    temp = n 
    while n != 0:
        rev = rev * 10 + n % 10
        n //= 10
    return temp == rev


def check(n):
    last = n % 10
    m = 0
    n //= 10
    while n >= 10:
        m = m * 10 + n % 10
        n //= 10
    return ((last * 2 == n) or (n * 2 == last)) and tn(m)

if __name__ == "__main__":
    n = int(input())
    if check(n):
        print("YES")
    else:
        print("NO")