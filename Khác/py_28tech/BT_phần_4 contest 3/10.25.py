import math

def cp(n):
    can = math.isqrt(n)
    if can * can == n:
        return True
    else:return False

if __name__ == "__main__":
    n = int(input())
    if cp(n):
        print("YES")
    else:print("NO")