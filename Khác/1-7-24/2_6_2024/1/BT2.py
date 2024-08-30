# 1. Cho biết kiểu của các giá trị sau: -50, 1.456, False, 0.0, .5, 4+5j
print(type(-50))
print(type(1.456))
print(type(False))
print(type(0.0))
print(type(.5))
print(type(4+5j))

# 2. Định nghĩa hai biến num1, num2 có cùng giá trị
num1 = 5
num2 = num1
print(num1)
print(num2)

# 3. Định nghĩa hai biến number1, number2 tích của chúng bằng 49
num1 = 98
num2 = 2
print(num1/num2)

# 4. Nhập vào tên và tuổi của bạn và in ra tên và tuổi của bạn trên cùng một hàng cách nhau bởi dấu | (xổ
name = input("nhập tên của bạn: ")
age = input("nhập tuổi của bạn: ")
print(name,age,sep="|")