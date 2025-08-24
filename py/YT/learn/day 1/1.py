# hàm print (in giá trị ra màn hình)


print(5,4,7)
# print mặc định ngăn cách bằng dấu cách 
# để sửa dấu đó ta có thể sử dụng tham số sep trong hàm print()
print(5,4,7,sep="__")

# tham số end giúp chúng ta thay đổi kí tự xuống dòng của hàm print bằng kí tự ta thích mặc định nếu ta không thêm nó là \n
print(5,end=" ")
print(6)

# Biến.

x = 5
print(type(x)) # int
print((x)) # 5

y = 6.7
print(type(y)) # float
print(y) # 6.7

z = "xin chào"
print(type(z)) # str
print(z) # xin chào

# toán tử so sánh and or not
print(1 > 2) # False

print(3 == 3.0) # True

print(5 != 6) # True

print(1 > 2 and 4 < 4) # False and False ==> False

# 0 False 
# 1 True

# hàm and nếu giá trị đầu tiên là True thì sẽ trả về giá trị thứ hai và ngượi lại.
print(1 and 2) # 2
print(0 and 1) # 0

# hàm or sẽ ngược lại với hàm and nếu giá trị đầu tiên là False thì sẽ trả về giá trị thứ 2 và ngược lại.

print(1 or 0) # 1
print(0 or 3) # 3

print(not True)
print(not 3)

# xử lý chuỗi trong python
s = "Hello World"

print(s.upper()) # in hoa tất cả
print(s.title()) # in hoa chữ đầu tiên của mỗi từ.
print(s.lower()) # in thường tất cả
print(s.capitalize()) # in hoa chữ cái đầu còn tất cả các từ còn lại in thường.

# f-string

age = 18
print(f"I am {age}")
print("I am", age)
print("I am "+ str(age))
print("I am {}".format(age))