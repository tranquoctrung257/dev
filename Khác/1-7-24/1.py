# cách setup vscode

# bật auto save
# ở góc trái màn hình vào file sau đó chọn auto_save

# các extension cần thiết
# 1.python
# 2.codeRunner
# 3.codeSnap
# 4.VSCode Great Icons

# cách setting 
# ctr + ,
# vào mục extension kiểm mục run code configuration
# tích vào mục Clear Previous Output # mỗi lần chạy lại nó sẽ xóa terminal cũ
# bỏ tích Compact Folders
# bỏ tích Run In Terminal
# tích vào mục Execute In File Dir
# tích vào Format On Save
# vào mục Executor Map rồi cho dòng python như thế này "python": "set PYTHONIOENCODING=utf8 && python -u",

# để chụp hình bằng code runner thì bôi đên code rồi ấn ctrl+shift+p hoặc ấn chuột phải chọn code snap

# để di chuyển một dòng nào đó ta ấn phím art + phím xuông hoặc lên

# ctrl shift L để chọn nhiều từ từ 1 từ mình mới bôi đen

# ctrl F để tìm kiếm

# ctrl + j mở terminal

# win + . để mở hộp thoại stick

# để nhân bản 1 dòng nhấn shift art mũi tên xuống

# để tìm 1 từ nào đó trong cả file nhấn ctrl shift L

# để tìm 1 từ nào đó giống từ mình đang bôi đen thì nhấn ctrl D

# để kiểm tra phiên bản python hiện tại nhấn python -V

# để kiểm tra trong mấy có bao nhiêu phiên bản python nhấn: py -0p

# để hiện thị tất cả đường dẫn python nhấn where python 

# hàm print
print("hello word",end="")
# ,end="" dùng để xóa kí tự xuống dòng của hàm print tiếp theo vì vậy nó sẽ in cùng dòng với hàm print tiếp

print(1,3,4,5,6,7,8,9,sep="#")
# ,sep ="#" nó sẽ ngăn các các 

a = "xin chào"
print(a.upper()) # viết hoa tất cả 
print(a.lower()) # viết thường tất cả
print(a.title()) # viết hoa chữ cái đầu tiên của mỗi chữ
print(a.capitalize()) # viết hoa chữ cái đầu

# cách ép kiểu
age = 34

print(f"I am {age}")
print("I am",age)
print("I am " + str(age))
print("I am {}".format(age))


# để nhập dữ liệu từ bàn phím ta dùng hàm input

z = input("nhập tuổi của bạn: ")
print("tuổi của bạn là {}".format(z))

# chú ý
print(float("nan"))  # ==> nan
print(float("inf"))
print(float("-inf"))

# chuyển đổi đươc mà sẽ không ra lỗi

# để mở lại các thư mục vừa mở thì nhấn file chọn open recent