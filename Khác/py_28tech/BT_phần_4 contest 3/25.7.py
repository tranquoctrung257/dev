import math

if __name__ == "__main__":
    a,b = map(int,input().split())
    for i in range(a,b):
        for j in range(i+1,b+1):
            if math.gcd(i,j):
                print("(",i,",",j,")",sep="")