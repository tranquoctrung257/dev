# để nhập từ bàn phím thì dùng hàm input 

firsname = input("nhập vào tên của bạn: ")

print(firsname)

# có thể nối 2 chuỗi lại với nhau
print("tên của bạn là: " + firsname)

# ví dụ nhập tên của mình máy tính tính tuổi của mình 
nam_hien_tai = 2025

age = int(input("nhập năm sinh của bạn: "))
print("tuổi của bạn là: ", nam_hien_tai - age)

# TypeError: unsupported operand type(s) for -: 'int' and 'str' nếu không ép kiểu sẽ bị lỗ này không hỗ trợ trừ kiểu số nguyên và kiểu chuỗi.