lst = ["a","b","c"]

print("-".join(lst))

lst = ["a","b","c",1]
print("-".join(map(str,lst)))

# sum có thể thêm giá trị start giá trị bắt đầu cộng
print(sum([1,2,3,4],start=1)) # sẽ ra là 1 + 1 + 2 + 3 + 4

"""
if
elif - else if
else

if đk:
    code
elif dk:
    code
else:
    code
"""
age = int(input("nhập vào tuổi: "))
if age >= 19:
    print("bạn có thể uống bia")
elif age > 10:
    print("có thể uống nước ngọt")
else:
    print("uống sữa")

# if ngắn gọn
msg = "uống bia" if age > 18 else "uông nước ngọt"
print(msg)
##
a,b,c = 1,2,3

m = a
if b > m:
    m = b
if c > m:
    m = c
print(m)

if 2==4:
    pass
# hoặc
else:
    ...

# để in 1 list không còn dấu ngoặc vuông
lst = [2,3,4,5,67,1]
print(*lst)
print("abcd",end="\b") # in lùi lại 1 kí tự

# print text color python