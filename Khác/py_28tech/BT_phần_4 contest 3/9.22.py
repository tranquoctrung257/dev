import math

# if __name__ == "__main__":
#     a,b = map(int,input().split())
#     can1 = math.isqrt(a)
#     can2 = math.isqrt(b)
#     cnt = 0
#     if can1*can1 != a:can1+=1
#     for i in range(can1,can2+1):
#         cnt+=1
#     print(cnt)

# hoặc
if __name__ == "__main__":
    a,b = map(int,input().split())
    can1 = math.isqrt(a)
    can2 = math.isqrt(b)
    cnt = 0
    if can1*can1 != a:can1+=1
    if (can2+1) * (can2+1) == b:can2+1
    print(can2-can1+1)