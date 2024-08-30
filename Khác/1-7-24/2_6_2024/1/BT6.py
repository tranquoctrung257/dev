# Nhập vào một số nguyên n. Kiểm tra và in ra n là số chẵn hay lẻ
n = int(input("nhập vào số nguyên n: "))
print(f"{n} là số chẵn" if n % 2 == 0 else f"{n} là số lẻ")

# Nhập vào một năm bất kỳ. Kiểm tra xem năm đó có phải là năm nhuận hay không ?
n = int(input("nhập vào năm: "))
if n % 400 == 0 and n % 4 == 0 or n % 100 != 0:
    print(f"{n} là năm nhuận")
else:
    print(f"{n} không phải là năm nhuận")

# Nhập hai số a và b từ bàn phím. In ra số lớn nhất và nhỏ nhất trong hai số
a = int(input("nhập vào số nguyên a: "))
b = int(input("nhập vào số nguyên b: "))
print(f"số lớn nhât là {max(a,b)}")
print(f"số lớn bé là {min(a,b)}")

# Giải và biện luận phương trình bậc nhất một ẩn ax + b = 0 (ẩn x, a và b là hai số cho trước)
a = float(input('a = '))
b = float(input('b = '))

if a == 0:
    if b == 0:
        print("Phương trình có vô số nghiệm")
    else:
        print("Phương trình vô nghiệm")
else:
    print("Phương trình có nghiệm duy nhất x =", -b/a)


# Giải và biện luận phương trình bậc nhất một hai ax^2 + bx + c = 0 (ẩn x, a, b, c là ba số cho trước)

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
        print("Phương trình có nghiệm duy nhất x =", -c / b)
else:
    denta = b ** 2 - 4 * a * c

    if denta > 0:
        x1 = (-b + denta ** 0.5) / (2 * a)
        x2 = (-b - denta ** 0.5) / (2 * a)

        print("Phương trình có 2 nghiệm phân biệt:", x1, x2)
    elif denta == 0:
        print("Phương trình có nghiệm kép:", -b / (2 * a))
    else:
        print("Phương trình vô nghiệm")