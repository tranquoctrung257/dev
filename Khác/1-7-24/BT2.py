# bài 1: cho biết kiểu của giá trị sau: -50,1.456,False,0.0,5
print(type(-50)) # int
print(type(1.456)) # float
print(type(False)) #Bool
print(type(0.0)) # float
print(type(5)) # int

# bài 2: định nghĩa 2 biến mun1 và mun2 có cùng giá trị
num1 = 3423
num2 = num1
print(num1)
print(num2 )

# bài 3: định nghĩa 2 biến number1, number2 tích của chúng bằng 49  
number1 = 9.8
number2 = 5
print(number1*number2)

# bài 4: nhập tên và tuổi của bạn và in ra tên tuổi của bạn trên cùng một hàng và cách nhau bởi dấu |
name = input("nhập tên của bạn: ")
age = int(input("nhập tuổi của bạn: "))
print(f"tên: {name} | tuổi: {age}")

# bài 5: nhập vào số nguyên n, số thực z, chuỗi s và in các giá trị của chúng trên các dòng riêng biệt
print("-"*40)
print("bài5")
n = int(input("nhập vào số nguyên n: "))
z = float(input("nhập vào số thực z: "))
s = input("nhập vào chuỗi s: ")
print(f"""
số nguyên là: {n}
số thực là: {z}
chuỗi s là: {s}
""")