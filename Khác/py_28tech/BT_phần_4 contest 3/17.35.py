import math

# def gcd(m,n):
#     while m != n:
#         if m > n:
#             m = m - n
#         else:
#             n = n - m
#     return m

def _gcd(a,b):
    while b != 0:
        a,b = b, a%b
    return a

if __name__ == "__main__":
    a,b = map(int,input().split())
    print(_gcd(a,b),a * b // _gcd(a,b))