# 1.Nhập vào một số nguyên n. Kiểm tra và in ra n là số chẵn hay lẻ

n = int(input("Nhập vào một số nguyên n: "))
print(f"{n} là số chẵn"if n % 2 == 0 else f"{n} là số lẻ")

# 2.Nhập vào một năm bất kỳ. Kiểm tra xem năm đó có phải là năm nhuận hay không ?

year = int(input('nhập vào năm bất kỳ:'))
if (year % 4 == 0) and (year % 100 != 0):
    print('năm:', year, 'là năm nhuận')
elif (year % 100 == 0) and (year % 400 == 0):
    print('năm:', year, 'là năm nhuận')
else:
    print('năm:', year, 'không phải năm nhuận')

# 3.Nhập hai số a và b từ bàn phím. In ra số lớn nhất và nhỏ nhất trong hai số

a = int(input("nhập a :"))
b = int(input("nhập b :"))

if a >b:
    print("số lớn nhất là ",a)
    print("số bé nhất là ",b)
else:
    print("số lớn nhất là ",b)
    print("số bé nhất là ",a)
# 4. Giải và biện luận phương trình bậc nhất một ẩn ax + b = 0 (ẩn x, a và b là hai số cho trước)
    
a = float(input('nhập a: '))
b = float(input('nhập b: '))
if a == 0 and b == 0:
    print('pt vô số nghiệm')
elif a == 0 and b != 0:
    print('pt vô nghiệm')
else:
    print('pt có 1 nghiệm:', -b/a)

# 5.Giải và biện luận phương trình bậc nhất một hai ax^2 + bx + c = 0 (ẩn x, a, b, c là ba số cho trước)
    
import math
a = float(input('nhập a: '))
b = float(input('nhập b: '))
c = float(input('nhập c: '))
delta = pow(b, 2) - 4*a*c
if delta < 0:
    print('pt vô nghiệm')
elif delta == 0:
    print('pt có nghiệm kép x1 = x2:', -b/2*a)
else:
    print(f'pt có 2 nghiệm phân biệt x1 = {(-8+math.sqrt(delta)/2*a)} và x2 =  {(-8-math.sqrt(delta)/2*a)}')
