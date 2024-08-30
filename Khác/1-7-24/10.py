# duyệt từng phần tử list,set,tup
lst = {4,100,3,2}
for value in lst:
    print(value)

d = {
    "a":1,
    "b":2,
    "c":3
}

# để in ra value của 1 dict
for value in d.values():
    print(value)

# để in ra key và value của 1 dict
for value in d.items():
    print(value)

for item in d.items():
    key,value = item
    print(key)
    print(value)
    print("-"*19)

# list comprehensions
lst = [1,2,3,4]

# new_lst = [2,4,6,8]
new_lst = []

for x in lst:
    val = x * 2
    new_lst.append(val)
print(new_lst)

# hoặc
new_lst_1 = [val * 2 for val in lst]
print(new_lst_1)

# biến 1 set trở thành kí tự in hoa
# set comprehensions
set_a = {"a","b","c"}

new_set = {s.upper() for s in set_a}
print(new_set)

# dict comprehensions
d = {
    "a":1,
    "b":2,
    "c":3
}
# k giữ nguyên 
# chỉ v*2
new_d = {
    k: v*2
    for k,v in d.items()
}
print(new_d)

# zip:lấy chỉ số bé nhất rồi in ra từng phần tử theo vị trí đó
lst1 = ["a","b","c"]
lst2 = (1,2,3,4)
lst3 = [2,4,6,7]

print(list(zip(lst1,lst2)))
print(list(zip(lst1,lst2,lst3)))

# enumerate: in ra 1 list tuple thứ tự của list

lst = ["a","b","c"]
print(list(enumerate(lst)))
print(list(enumerate(lst,start=1)))

# để chuyển tup ==> dict

lst1 = ("a","b","c")
lst2 = (1,2,3)

print(list(zip(lst1,lst2)))
print(dict(zip(lst1,lst2)))

lst = [1,2,3,4,45,9]
new_lst = [v*3 for v in lst]

# hoặc

new_lst = []
for x in lst:
    new_lst.append(x*3)

print(new_lst)

number = [32,34,2,4,62,90,43,43]
# lấy ra các con số lẻ rồi cộng lại
new_number = [v for v in number if v%2 != 0]
print(new_number)

# lấy ra các con số lẻ nhân 2 và số chẵn nhân 2
new_lst_2 = [v*2 if v%2 == 0 else v*3 for v in lst]
print(new_lst_2)

# hoặc
new_lst = []
for x in lst:
    if x % 2 == 0:
        new_lst.append(x*2)
    else:
        new_lst.append(x*3)
print(new_lst)

# enumerate ==> tuple (),()
lst = [1,2,3,4]
# {i} - value
for item in enumerate(lst):
    idx,value = item
    print(f"{idx}-{value}")

for idx,value in enumerate(lst,start=1):
    print(f"{idx}-{value}")

print(list(zip(enumerate(lst,start=1))))

lst = [1,2,3,4]
# 4 => range(4) ==> 0,1,2,3
# in ra các số lẻ và chỉ số
for i in range(len(lst)):
    if i % 2 != 0:
        print(i, lst[i])

# hoặc
for i,v in enumerate(lst):
    if i % 2 != 0:
        print(i, v)