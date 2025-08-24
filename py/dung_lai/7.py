# input() hàm có sẵn built-in function có tác dụng nhập từ bàn phím.

CURRENT_YEAR = 2025

firstName = input("your firstname: ")
lastname = input("your last name: ")
year_born = int(input("when you were born: "))

# nếu không ép kiểu sẽ có lỗi này TypeError: unsupported operand type(s) for -: 'int' and 'str'
# lỗi này có nghĩa là không hỗ trợ trừ cho kiểu int và kiểu str
age = CURRENT_YEAR - year_born

print("Your name is "+ firstName + " " + lastname)
print("You are " + str(age) + " years old in" + str(CURRENT_YEAR))