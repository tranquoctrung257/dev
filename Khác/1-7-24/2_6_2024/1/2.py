# để chạy pycharm cell mode gõ ##
# các trang web chup code hay
# https://carbon.now.sh/
# ray.so

##
print("xin chào")

# + - * / // ** %
# ** lũy thừa ví dụ a^n
# % chia lấy phần dư
# // chia lấy phần nguyên
# fstring
# format

# lưu ý: mức độ ưu tiên của ** cao hơn - nên phép toán 1 ** 0 sẽ thực hiện trước rồi mới đến - kết quả đó
print(-1 ** 0)
print(-1000 ** 1)
# .1 = 0.1
print(.1 + .4)

# > < >= <= == != ==> True/False
# and or not
##
print(1 and 0)  # and trả về giá trị bên trái and nếu nó sai còn trả về giá trị bên phải nếu nó đúng, luôn dựa vào giá trị đầu tiên
print(0 and 1)  # trả về 0 vì giá tr đầu là sai
print(1 or 0)  # trả về 1 vì dựa vào giá trị đầu tiên nên kq là 1
print(0 or 0)  # trả về 1 vì 0 bên trái là F nên sẽ trả về 0

# += -= *= /= //= **= %=

x = 10
print(x)
x += 10  # x = x + 10
print(x)

##
s = "Hello"
s1 = "Word"
print(s + " " + s1)
# hoặc fstring
print(f"{s} {s1}")
print("{} {}".format(s,s1))
print("%s %s"%(s,s1))

# để trả về 1 giá trị trong bảng mã ascii sử dụng hàm ord()
print(ord("a"))
##
your_name = input()
print(your_name or "John")