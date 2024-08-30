# 1 Đếm số chẵn và lẻ trong đoạn [0, 1000] theo 2 cách: thông thường và list comprehension

count_c = 0
count_l = 0
for i in range(1000):
    if i % 2 == 0:
        count_c +=1
    else:
        count_l+=1
print(count_c)
print(count_l)


lst_even = [n for n in range(1000) if n % 2 == 0]
lst_odd = [n for n in range(1000) if n % 2 != 0]

print(f"cac số lẻ {len(lst_odd)}")
print(f"cac số chẵn {len(lst_even)}")

# 2.Nhập vào một danh sách những số nguyên và hiển thị gấp đôi của các số trong danh sách sử dụng list comprehension

lst = map(int,input("nhập số nguyên: ").split())
new_lst = [n**2 for n in lst]
print(new_lst)

'''3.Cho dict như sau:
people = {
  "Emma": 71,
  "Jack": 45,
  "Amy": 15,
  "Ben": 29
}
a. In ra người già nhất
b. Tạo ra một dict mới dựa vào people dict với tuổi của mỗi người tăng gấp đôi
c. In ra enumerate các key trong people dict
d. Sử dụng hàm dict để biến enumerate bên trên trở thành dict
'''

people = {
  "Emma": 71,
  "Jack": 45,
  "Amy": 15,
  "Ben": 29
}

# a.
max_age = 0
name_max = ""
for name,age in people.items():
    if age > max_age:
        max_age = age
        name_max = name
print(name_max)

# hoặc 
print(max(people,key=people.get))
# b.
new_dict = {
    name: age*2
    for name,age in people.items()
}
print(new_dict)

# c.
print(list(enumerate(people)))

# d.
print(dict(enumerate(people)))

'''4.Sử dụng zip function để tạo 2 lists sau trở thành một dict
fruits = ["banana", "apple", "kiwi", "mango", "cherry", "orange"]
amounts = [12, 34, 90, 100, 300, 45, 60, 70, 678]
'''
fruits = ["banana", "apple", "kiwi", "mango", "cherry", "orange"]
amounts = [12, 34, 90, 100, 300, 45, 60, 70, 678]
print(dict(zip(fruits,amounts)))
