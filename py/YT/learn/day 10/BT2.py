# 2. Nhập vào một danh sách những số nguyên và hiển thị gấp đôi của các số trong danh sách sử dụng list comprehension
lst = map(int,input("nhập số nguyên cách nhau bởi dấu cách: ").split())

lst_new = [x * 2 for x in lst]
print(lst_new)