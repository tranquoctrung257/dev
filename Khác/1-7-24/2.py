# value
# data type
# input

# munber (1,23,3,5,2 | int số nguyên),(1.3,4.34,34.2 | float số thực )
# string "33" "hải" 
# boolean: True False

print(type(432)) # int
print(type(3.2)) # float
print(type("")) # str
print(type(True)) # bool

# variable

x = 5 
# biến x được gán giá trị bằng 5
# biết không được bắt đầu bằng số 
# _ cũng là một tên biến hợp lệ

full_name = input("nhập họ và tên của bạn: ")
print(type(full_name))
print(full_name)
# hàm input luôn trả về là str nếu không được ép kiểu

# để ép kiểu 1 số nào đó
numnber = input('nhập số nguyên: ')
numnber_as_int = int(numnber)
print(type(numnber_as_int))
print(numnber_as_int + 43)

# 1 số nằm trong cặp nháy kép mà nhân với 1 số khác sẽ ra 1 chuỗi của số đó nhân lên vd
print("2"*44)

# .5 là 0.5
 