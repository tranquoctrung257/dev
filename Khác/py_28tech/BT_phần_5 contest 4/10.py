def S(n):
    if n == 0:
        return 0
    return 1/n +S(n-1)

if __name__ == "__main__":
    n = int(input())
    print("%.3f"%(S(n)))