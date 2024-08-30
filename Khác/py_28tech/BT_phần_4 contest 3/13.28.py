import math

def check(n):
    while n != 0:
        r = n % 10
        if r != 0 and r != 6 and r != 8:
            return False
        n //=10
    return True
if __name__ == "__main__":
    n = int(input())
    if check(n):
        print(1)
    else:
        print(0)