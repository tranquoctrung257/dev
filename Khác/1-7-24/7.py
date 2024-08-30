"""
+ advavced set
+ Dictionary
+ sum, len, min, max, join
"""

set1 = {1, 4, 3, 2}
set2 = {2, 3, 10, -10}

# để tìm phần tử chung của 2 set 
set3 = set1.intersection(set2)
print(set3)

# intersection: giao , intersection không bắt 2 biến cùng kiểu dữ liệu

# hoặc 

print(set1 & set2)
# bắt buộc 2 biến cùng kiểu dữ liệu

# để tìm phần tử có trong set1 mà không có trong set2

set4 = set1.difference(set2)
print(set4)

# hoặc

print(set1 - set2 )

# để tìm ngược lại thì đảo ngược
print(set2 - set1 )

# lấy ra tất cả phần tử trong set1 và set2
set5 = set1.union(set2)
print(set5)

# hoặc

print(set1 | set2)

# có thể sử dụng trong nhiều set
set6 = {3,52,234,67}
set7 = set1.union(set2).union(set6)
print(set7)
# hoặc 
print(set1 | set2 | set7)

# để lấy tất cả nhưng chừa đi phần chung của 2 set
set8 = set1.symmetric_difference(set2)
print(set8)

# hoặc

print(set1 ^ set2)

# + Dictionary: key:value
# vd

# để in ra chuỗi json đẹp hơn ta sử dụng modun json
import json

studens = {
    "Name":"Bob",
    "age" : 23,
    "grades" : [23,432,66,766,22]
}

print(json.dumps(studens,indent=4))

# cách 1
# để lấy ra một biến trong dict
value = studens["Name"]
print(value)

# cách 2 
# get nếu truyền vào giá trị đã có trong dict thì nó sẽ in ra 
# nếu không nhập một giá trị không tồn tại thì nó vẫn chạy và trả về None 
# get cũng dùng để nhập dữ liệu vào dict vd studens.get("key_new","value_new")
value1 = studens.get("id","SV001")
print(value1)

# để thêm 1 key và value trong dict 

studens["id"] = "SV001"
print(studens)

# để đổi một giá trị trong dict
studens["Name"] = "Jack"
print(studens)

# để thêm nhiều cặp key:value vào dict
studens.update(id = "SV002",gender = "male")
print(studens)

# hoặc để đưa key:value bằng 1 biến
info = {
    "id":"SV001",
    "gender":"male",
    "key":"value"
}
studens.update(info)
print(studens)

# hoặc để đưa key:value bằng 1 biến list tuple
info1 = [
    ("MHS","SV001"),
    ("class","male")
]
studens.update(info1)
print(studens)

# để xóa 1 phần tử trong dict
value3 = studens.pop('age')
print(studens)
print(value3)

# hoặc

del studens["grades"]
print(studens)

# để xóa đi phần tử cuối và lưu lại dưới dạng tuple

tup = studens.popitem()
print(tup)
print(studens)

# để lấy ra tất cả key trong dict và biến nó thành list
keys = list(studens)
print(keys)

# để lấy ra giá trị trong tưng key
value = list(studens.values())
print(value)

# để lấy ra cả key:value
items = list(studens.items())
print(items)

# để xóa tất cả dict
studens.clear()
print(studens)

# để cộng tất cả giá trị trong 1 biến
lst = [2,4,6,2,23,66]
total = sum(lst)
print(total)

lst = [2,4,6,2,23,66]
total = sum(lst,107)
print(total)

# len

lst = ["3","33"]
print(len(lst))

# để tìm một số nhỏ nhất trong list
total = min(lst)
print(total)

# để tìm một số lớn nhất trong list
total = max(lst)
print(total)

# json
# map(kiểu dữ liệu cần chuyển,biến cần chuyển)

lst = [4,6,7,84]
# phần tử trong list là int nên không sử dụng được join nên ta sẽ ép kiểu bằng hàm map
s = '  '.join(map(str,lst))
s1 = ' - '.join(map(str,lst))
print(s)
print(s1)