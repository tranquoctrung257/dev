"""
if-elif-else
"""

"""
if {đk}:
    câu lệnh thực hiện
elif {đk}:
    câu lệnh thực hiện
else:
    câu lệnh thực hiện

đk ở đây là điều kiện so sánh toán nếu ra True thì sẽ chạy nếu False thì sẽ chạy câu lệnh tiếp theo 
"""

n = int(input("n = "))
if n > 0:
    print("số dương")
elif n < 0 :
    print("số âm")
else:
    print("số 0")


if n % 3 == 0:
    print("n chia hết cho 3")
else:
    print("n không chia hết cho 3")

# lệnh if ngắn gọn
print("n chia hết cho 3"if n % 3 == 0 else "n không chia hết cho 3")


a = int(input("a = "))
b = int(input("b = "))

# if a > b:
#     print(a)
# else:
#     print(b)

# hoặc if ngắn gọn
print(a if a>b else b)

# hoặc ngắn gọn hơn

m = a 
if b > a:
    m = b
print(m)

# để truyền vào mà có dấu cách

a,b = map(int,input("nhập số a và b cùng dòng: ").split())
print(a if a>b else b)

# eval: cộng các số trong 1 chuỗi

print(eval("4*45"))

lst = list(map(eval,input("nhập số cách nhau bằng dấu cách").split()))
print(lst)

# để phá vỡ ngoặc vuông không cần chuyển về tuple
lst = [3,4,5,6]
print(lst)
print(*lst)
print(*lst,sep=" % ")

# eval
a = 2
print(eval("a"))

# round(): làm làm tròn giá trị

x = 3.453
print(round(x))

y = 2.543
print(round(y,2))
# round(số cần làm tròn,làm tròn đến mấy số sau dấu ,)

# sorted() sắp xếp list từ bé đến lớn
lst = [3,5,6,83,2]
new_lst = sorted(lst)
print(new_lst)

# để sắp xếp từ lớn đến bé
new_lst = sorted(lst,reverse=True)
print(new_lst)

# để chuyển đổi kí tự thường sang bảng mã ascii
# ord chr
ascii_code = "a"
print(ord(ascii_code))
print(chr(97))