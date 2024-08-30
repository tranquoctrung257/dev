## 9. Bài tập
# 1. In các số từ 1 đến 100 trên cùng một hàng
for i in range(1,101):
    print(i,end=" ")

# 2. In 100 lần dòng chữ "Hello World!"
for i in range(1,101):
    print(i,"Hello Word")

# 3. In ra các số chia hết cho 3 trong đoạn [1, 1000]
for i in range(1,1001):
    if i % 3 == 0:
        print(i,end=" ")

# 4. Đếm số lượng số nguyên tố trong [1, 100]
count = 0
for j in range(2,101):
    for i in range(2,int(j**0.5)+1):
        if j % i == 0:
            break
    else:
        count+=1
print(count)
# 5. Nhập vào một số nguyên dương n tính tổng các chữ số của n. Ví dụ: n = 4312 => S = 4 + 3 + 1 + 2 = 10
count = 0
n = 4312
last = n %10
count+=last
n//=10
last = n%10
count+=last
n//=10
last = n%10
count+=last
n//=10
last = n%10
count+=last
print(count)

# hoặc
n = int(input("n = "))

while n <= 0:
    print("n phải là số nguyên dương")
    n = int(input("n = "))
    
S = 0

while n > 0:
    last = n % 10
    S += last
    n //= 10
    
print(S)

# 6. Nhập vào một số nguyên dương n. Đếm số lượng số chẵn và lẻ trong đoạn [0, n]
n = int(input("nhập vào số nguyên dương n: "))
le = 0
chan = 0
for i in range(1,n+1):
    if i % 2 == 0:
        chan+=1
    else:
        le+=1
print(f"chẵn: {chan}")
print(f"lẻ: {le}")

class Student:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year
        
    def get_age(self):
        return 2023 - self.birth_year
    
    def __str__(self):
        return f"Name: {self.name}, age: {self.get_age()}"