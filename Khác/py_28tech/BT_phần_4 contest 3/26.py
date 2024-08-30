if __name__ == "__main__":
    n = int(input())
    if n == 1:
        print(1)
    elif n == 2:
        print("1\n1")
    else:
        print("1\n1")
        fn1,fn2 = 1,1
        for i in range(3,n+1):
            fn = fn1 + fn2
            print(fn)
            fn2,fn1 = fn1,fn
