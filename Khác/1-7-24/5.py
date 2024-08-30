# + list in list
# + copy list
# + list slicing

#               0           1           2
friends = [["Bob",23],["Jen",34],["kenny",56]]

print(friends[0][1])


lst1 = [1,4,3]
lst2 = lst1

# is để kiểm tra id có bằng nhau hay không
print(lst1 is lst2)

# == để kiểm tra giá trị của hai biến có băng nhau hay không
print(lst1==lst2)

# để đổi id ta dùng hàm copy 
lst3 = lst1.copy()

print(lst1 is lst3)
print(lst1 == lst3)

# hàm id trả về id duy nhất của 1 cái đối tượng trong bộ nhớ

print(id(lst1),id(lst3))

# + list slicing: lấy ra 1 phần từ 1 list ban đầu
# trả về list mới không cùng id với list cũ

# list_new = list_cũ[start,stop,step]

a = [1,3,3,7,9]
new_lst = a[0:2:1]

print(new_lst is a)
print(new_lst)

# để lấy ra từ vị trí phần tử 1 đến hết
new_lst1 = a[1:]
print(new_lst1)

# để lấy ra 3,3,7
new_lst2 = a[1:-1]
print(new_lst2)

# để copy 1 list từ list ban đầu bằng list_slising
new_lst3 = a[:]
print(new_lst3)
print(new_lst3 is a)
print(new_lst3 == a)

# để đảo ngược chuỗi ở trong list_slising
new_lst4 = a[::-1]
print(new_lst4)