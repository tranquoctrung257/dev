"""
tuple() giống list nhưng không thể sửa phần tử trong nó
set ko thể trùng lặp, không thể truy cập chỉ số không có thứ tự
dict
"""
t = (1,)
print(type(t))
t = 1,
print(type(t))
t = type([2,4,5,7,5])
print(type(t))
t = tuple("abc")
print(t)
z = 34.423,6,3,6,7,2
# để thêm phần tử vào tuple
z+= 1,4,6,7
print(z)
# đê đếm 1 phần tử suất hiện bao nhiêu lần
print(z.count(6))

# để tìm vị trí của phần tử đầu tiên của 1 set
print(z.index(3))

s = {1,2,1,1,1,1,1}
print(s)
print(type(s))
# để gọi 1 set trống
s = set()
print(type(s))
# để thêm phần tử vào set
s.add(3)
s.add(5)
s.add(7)
s.add(9)
print(s)

# set nâng cao
s1 = {1,2,3,7,10}
s2 = {2,3,5,6,1}
# để tìm phần tử chung của 2 set
print(s1.intersection(s2))

# để tìm phần tử trong set 1 mà không có trong set2
print(s1.difference(s2))

# để gộp chung 2 set
print(s1.union(s2))

# để gộp 2 set nhưng khoog chứa phần chung
print(s1.symmetric_difference(s2))

d = {}
print(type(d))

d = {
    "a":1,
    "b":2,
    "c":3
}
print(d["a"])
print(d.get("b"))

# để thay đổi giá trị trong list
d["a"] = 100
print(d)

# để cập nhật 1 dict
d.update({
    "e":100,
    "d":2100
})
print(d)

# để xóa phần tử dùng pop