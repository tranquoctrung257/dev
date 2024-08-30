

def check(n):
    fn1,fn2 = 1,0
    for i in range(2,100):
        fn = fn1+fn2
        if fn >= n:

            return fn
        fn2,fn1 = fn1,fn
    return -1
if __name__ == "__main__":
    n = int(input())
    print(check(n))
    