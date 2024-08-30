"""
+ set : tạo bởi dấu ngoặc nhọn và trong set không được chứa phần tử trùng lặp, set không có thứ tự
+ tuple : tạo bởi dấu ngoặc tròn, giống list nhưng khác là không thể thay đổi giá trị trong nó
"""

tup1 = 3,2,4,2
tup2 = (3,2,44,3)
tup3 = 3,
tup4 = (2,)

print(type(tup1))
print(type(tup2))
print(type(tup3))
print(type(tup4))

tup5 = 3,3,5,2,6,8,9,3,1

# để in ra phần tử thì cũng giống list

print(tup5[4])
print(tup5[-1])

# tup[0] = 3324
# tuple không cho phép thay đổi giá trị trong nó
# tup5.append(3)

# để thêm phần tử vào tupple
tup5 += 1,3,5,6
print(tup5)

# set: là 1 cấu trúc dữ liệu bên trong 1 biến duy nhất mà set không thể chứa những phần tử trùng lặp, set không có thứ tự.

set1 = set()
print(len(set1))

# để thêm phần tử vào set
set1.add(43)
set1.add(43)
set1.add(43)

# set không chứa phần tử lặp lại

set1.add(2)
set1.add(4)
# set không có thứ tự

print(set1)

# để thêm nhiều phần tử vào set
set1.update([3,2,5,7,0])

print(set1)

# để xóa phần tử trong set
set1.remove(4)
print(set1)

# để copy ra biến mới dùng copy
set2= set1.copy()
print(set1 is set2)
print(set1 == set2)

# để xóa tất cả phần tử trong set1
set1.clear()
print(set1)

# không thể thêm giá trị của list vào set được
# set1.add([33,23,])

# set không có chỉ số 
# print(set1[2])

# để xóa giá trị bất kì và lưu lại ta dùng pop()
set3 = {32,3,7,5,1}
set4 = set3.pop()
print(set3)
print(set4)

# để tạo một thư mục riêng biệt thì gõ trong terminal: python -m venv venv
# để chọn thì tắt terminal và mở lại thì sẽ vào lại môi trường
# phím tắt để mở terminal ctrl j
# để hiện thị các thư viện bên ngoài thì gõ pip free
# để cài đặt các thử viện từ 1 file nào đó gõ: pip install -r .file tên thư viện cần cài đặt

friends = [
    ("Bob",23),
    ("Anna",35),
    ("Herry",34)
]

print(friends[0][1])
print(friends[-1])

# lấy ra list 2 3
lst = [[1,[2,3]],(2,5)]
print(lst[0][-1])
# lấy giá trị 2
print(lst[0][-1][0])
# để thêm 1 phần tử vào list 2 3
lst[0][-1].append(100)
print(lst) 
# để append vào list bên ngoài
lst.append(19)
print(lst)
# để copy list
lst1 = lst[:]

lst[0][1].append(33)
# biến sau khi copy vẫn bị append bởi 33

print(lst)
print(lst1)
print(lst1 is lst)
print(lst1 == lst)

# để kiểm tra code của 1 hàm nào đó nhấn vào hàm đó và nhấn phím ctrl 

# ord để chuyển 1 kí tự nào đó sang bẳng mã ascii

# dùng !r để in ra dấu nháy bao quanh của một chuỗi

t = "a"
print(f"{t!r}")