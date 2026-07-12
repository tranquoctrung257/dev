# 1. Cho biết kiểu của các giá trị sau: -50, 1.456, False, 0.0, .5, 4+5j
'''
-50 ==> int
1.456 ==> float
False ==> bool 
0.0 ==> float 
.5 ==> float 
4+5j ==> complex
'''

# 2. Định nghĩa hai biến num1, num2 có cùng giá trị

num1 = num2 = 4
print(num1,num2)

# 3. Định nghĩa hai biến number1, number2 tích của chúng bằng 49
number1 = number2 = 7
print(num1*num2)

# 4. Nhập vào tên và tuổi của bạn và in ra tên và tuổi của bạn trên cùng một hàng cách nhau bởi dấu | (xổ)

name = input("nhập tên của bạn: ")
age = int(input("nhập tuổi của bạn: "))
print(name,age,sep="|")

# 5. Nhập vào một số nguyên n, số thực z, chuỗi s và in các giá trị của chúng trên các dòng riêng biệt

n = int(input("nhập số nguyên n: "))
z = float(input("nhập số thực z: "))
s = input("nhập chuỗi s: ")
print(f"số nguyên n là: {n}")
print(f"số thực z là: {z}")
print(f"chuỗi s là: {s}")