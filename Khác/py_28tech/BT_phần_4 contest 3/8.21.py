import math
if __name__ == "__main__":
    a,b = map(int,input().split())
    can1,can2 = math.isqrt(a),math.isqrt(b)
    if can1 * can1  != a:
        can1+=1
    for i in range(can1,can2+1):
        print(i**2,end=" ")