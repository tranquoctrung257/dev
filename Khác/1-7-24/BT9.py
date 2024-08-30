# 1. In các số từ 1 đến 100 trên cùng một hàng
for i in range(1,101):
    print(i,end=" ")

# 2.In 100 lần dòng chữ "Hello World!"

a = 0
while True:
    a +=1
    if a == 101:
        break
    print(a,"Hello world!")

for i in range(1,101):
    print(i,"hello World")

# 3.In ra các số chia hết cho 3 trong đoạn [1, 1000]
for i in range(1,1001):
    if i % 3 == 0:
        print(i,end=" ")

# 4.Đếm số lượng số nguyên tố trong [1, 100]

count = 0

for n in range(2, 101):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            break
    else:
        count += 1
        
print(count)

# 5.Nhập vào một số nguyên dương n tính tổng các chữ số của n. Ví dụ: n = 4312 => S = 4 + 3 + 2 + 1 = 10
n = int(input("nhập số nguyên dương n: "))
s = 0
while n > 0:
    p = n % 10
    s += p
    n = n //10
print(s)

# 6. Nhập vào một số nguyên dương n. Đếm số lượng số chẵn và lẻ trong đoạn [0, n]
n = int(input("nhập vào số nguyên dương n từ 1 --> n: "))
count_c = 0
count_l = 0
for i in range(1,n):
    if i % 2 == 0:
        count_c +=1
    else:
        count_l +=1
print(count_c)
print(count_l)