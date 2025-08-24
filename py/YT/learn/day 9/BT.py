# ## 9. Bài tập
# 1. In các số từ 1 đến 100 trên cùng một hàng
for _ in range(1,101):
    print(_,end=" ")
print()
print("-"*50)
# 2. In 100 lần dòng chữ "Hello World!"
for _ in range(1,101):
    print(f"{_}.Hello World!")

print("-"*50)
# 3. In ra các số chia hết cho 3 trong đoạn [1, 1000]
for i in range(1,1001):
    if i % 3 == 0:
        print(i,end=" ")
else:print()

# 4. Đếm số lượng số nguyên tố trong [1, 100]
dem = 0
for i in range(1,101):
    for j in range(2,int(i**0,5)+1):
        if i % j == 0:
            break
    else:
        dem+=1
# 5. Nhập vào một số nguyên dương n tính tổng các chữ số của n. Ví dụ: n = 4312 => S = 4 + 3 + 1 + 2 = 10
n = int(input("Nhập vào một số nguyên dương n: "))
while n <= 0:
    n = int(input("Nhập vào một số nguyên dương n phải lớn hơn 0: "))
s = 0
while n > 0:
    last = n % 10
    s += last
    n//=10
print(s)
# 6. Nhập vào một số nguyên dương n. Đếm số lượng số chẵn và lẻ trong đoạn [0, n]

chan = 0
lẻ = 0
for i in range(1,n+1):
    if n % 2 == 0:
        chan+=1
    else: le+=1
print(f"có {chan} số chẵn")
print(f"có {le} số le")