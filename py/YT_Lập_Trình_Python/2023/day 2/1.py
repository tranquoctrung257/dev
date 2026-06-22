# cách để chạy được code khi có biểu tượng cảm xúc.
# vào seting vào rồi tìm mục Executor Map sau đó ấn vào edit in seting.json
# tìm đến chỗ python rồi đổi thành như thế này  "python": "set PYTHONIOENCODING=utf8 && python -u",

# Hôm nay ta sẽ học
# Values :giá trị.
# Data Types: Kiểu dữ liệu.
# Hàm input. hàm nhập vào từ bàn phím.

# 1.Values - giá trị và data type - kiểu dữ kiệu.
# các loại giá trị trong python ví dụ như số 1,2,3 thuộc kiểu int, hoặc 1.3,0.0,3.5,.. thuộc Kiểu float hoặc "hello" thuộc kiểu str, hoặc True False thuộc kiểu bool,...

# 2. variable - Biến.
x = 5  # giá trị 5 thuộc kiểu int được gán cho x
print(x)  # để in ra giá trị của x ==> 5
print(type(x))  # để in ra kiểu giá trị của x ==> int

# biến có thể thay đổi giá trị làm giá trị khác.
x = 6
print(x)  # giá trị của x được thay đổi bằng 6

# các quy tắc đặt tên biến
'''
- không được sử dụng dấu cách.
- không được sử dụng dấu.
- không được bắt đầu bằng số. 
- không được sử dụng kí tự đặc biệt.
- chỉ trừ kí tự _
'''


# 2.hàm Input.
# Input ==> luôn trả về str nếu muốn đổi kiểu thì phải ép kiểu.

# input("giá trị thông báo ra màn hình.được đặt trong dấu nháy đơn hoặc nháy kép")
# hàm input luôn được gán với biến nào đó ví dụ.

name = input("Nhập tên của bạn: ")
print(f"Tên của Bạn là:{name}")
print(type(name))  # in ra kiểu dữ liệu ==> int

# để ép kiểu hàm input ta thêm vào kiểu dữ liệu trước hàm input
number = float(input("Nhập số thực bất kì: "))
print("số bạn nhập là: {}".format(number))

# có thể cộng con số đó
print(number+5)
print(number**5)

# Một số lưu ý.
'''
2 ==> int
4.76 ==> float
5+6j ==> complex
"hello" ==> str
True ==> bool

.5 ==> 0.5 ==> Float

quy ước trong python một hằng số không thay đổi thì nên đặt tên biến bằng chữ hoa tất cả 
ví dụ PI = 3.14
'''
