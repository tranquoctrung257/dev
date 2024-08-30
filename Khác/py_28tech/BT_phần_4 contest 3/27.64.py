

def check(n):
    if n == 0 or n == 1:
        return True
    fn1,fn2 = 1,0
    for i in range(2,100):
        fn = fn1+fn2
        if fn == n:
            return True
        fn2,fn1 = fn1,fn
    return False
if __name__ == "__main__":
    n = int(input())
    if check(n):
        print("YES")
    else:print("NO")
    