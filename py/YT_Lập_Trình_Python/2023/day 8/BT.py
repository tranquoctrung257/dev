# ## 3. Bài tập
# 1. Nhập vào một số nguyên n. Kiểm tra và in ra n là số chẵn hay lẻ

n = int(input("nhập vào số nguyên n: "))
if n % 2 == 0:print(f"{n} chia hết cho 2.")
else: print(f"{n} không chia hết cho 2.")

# hoặc cách ngắn gọn hơn
s = "số chia hết cho 2"
if n % 2 != 0:
    s = "số không chia hết cho 2"
print(s)

# 2. Nhập vào một năm bất kỳ. Kiểm tra xem năm đó có phải là năm nhuận hay không ?
nam = int(input("nhập vào năm: "))

if nam % 400 == 0 or (nam % 4 == 0 and nam % 100 != 0):
    print(nam,"là năm nhuận")
else:print(nam,"không phải năm nhuận.")

# 3. Nhập hai số a và b từ bàn phím. In ra số lớn nhất và nhỏ nhất trong hai số
a,b = map(int,input("nhập số a và b: ").split())
if a > b:
    print("số lớn nhất là: ",a)
    print("số lớn bé là: ",b)
elif a == b:
    print("hai số bằng nhau.") 
else:
    print("số lớn nhất là: ",b)
    print("số lớn bé là: ",a)

# 4. Giải và biện luận phương trình bậc nhất một ẩn ax + b = 0 (ẩn x, a và b là hai số cho trước)
a = float(input("nhập số nguyên a: "))
b = float(input("nhập số nguyên b: "))
if a==0:
    if b == 0:
        print("phương trình có vô số nghiệm.")
    else:
        print("phương trình vô nghiệm")
else:
    print("nghiệm của phương trình là: x =",-b/a)
# 5. Giải và biện luận phương trình bậc nhất một hai ax^2 + bx + c = 0 (ẩn x, a, b, c là ba số cho trước)

# 5. Giải và biện luận phương trình bậc nhất một hai ax^2 + bx + c = 0 (ẩn x, a, b, c là ba số cho trước)
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

if a == 0:
    if b == 0:
        if c == 0:
            print("Phương trình có vô số nghiệm")
        else:
            print("Phương trình vô nghiệm")
    else:
        print("Phương trình có nghiệm duy nhất x =", -c/b)
else:
    denta = b**2 - 4*a*c
    
    if denta > 0:
        x1 = (-b + denta**0.5) / (2*a)
        x2 = (-b - denta**0.5) / (2*a)
        
        print("Phương trình có 2 nghiệm phân biệt:", x1, x2)
    elif denta == 0:
        print("Phương trình có nghiệm kép:", -b/(2*a))
    else:
        print("Phương trình vô nghiệm")