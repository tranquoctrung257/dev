# operators:toán tử

# +, =, *, /, //, **, %

print(1+2)
print(1-2)
print(1*2)
print(1/2) #float
print(1//2) # int
print(2 ** 5) #2^5
print(4%3) # chia lấy phần dư 

# toán tử so sánh
# <, >, <=, >=, == !=
# bool True/False
print(1>2)
print(3.0 == 3)
print("a"!= "a")

# and or not
# kết hợp 2 hay nhiều biểu thức điều kiện vs nhau

print(True and True) #True
print(True and False) #False
print(False and False) #False
print(False and True) #False

print(True or True) #True
print(True or False) #True
print(False or False) #False
print(False or True) #True 

print(not True)

print(bool(0))
print(bool(1))

# and và or dựa vào giá trị thứ nhất để xác định kết quả 

# toán tử and nếu đúng số thứ nhất sẽ trả về phần tử thứ 2
print(1 and 2) # True and True ==> 2

print(1 and 0 ) # ==>0

# toán tử and nếu sai phần tử thứ nhất sẽ trả về phần tử thứ nhất
print(0 and 2) # F and T ==> 0

print(0 or 1) # False or True ==> giá trị thứ 2 ==> 1

print(1 or 0) # True or False ==> giá trị thứ nhất

print(not 1) # False

# falsy: 0, 0.0, 0j, None: no value
# list: []
# bool(falsy) = False
print(bool(0))
print(bool([]))

# += -= *= /= //= %= *=

x = 5
x = x + 10
print("x =",x)

x = 5
x += 10
print("x =",x)

print(.5 > 1) # False
# print(1/0) # error

# f_strings
age = 43
print("I am",age)
print("I am "+ str(age))
print(f"I am {age}")
print("I am {}".format(age))

s = "Hello Word"
s = s.upper()
print(s)
s = s.lower()
print(s)
s = s.title()
print(s)
s = s.capitalize()
print(s)

# hàm split()

lst = s.split()
print(lst) 
