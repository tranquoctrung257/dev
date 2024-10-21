# Bài 1. Viết chương trình cho phép người dùng nhập một số nguyên dương N từ bàn phím rồi in ra số có nhiều ước số nhất trong các số nhỏ hơn N


def uoc(n):
    count = 0
    for i in range(1,n+1):
        if n % i == 0:
            count += 1
    return count

def main(N):
    max_ = 0
    result = 1
    for i in range(1,N):
        n = uoc(i)
        if n > max_:
            max_ = n 
            result = i

    return result,max_

# n = input("nhập N: ")
n = 10
if n <= 1:print("n phải lớn hơn 1!")
else: print("số có nhiều ước nhất là:",main(n)[0],"và có số ước là:",main(n)[-1])
