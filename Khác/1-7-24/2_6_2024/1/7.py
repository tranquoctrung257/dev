import random
a = [1,2,3]

new_list = []

# for x in a:
#     new_list.append(x*2)
# print(new_list)

# hoặc
print([i*2 for i in a])
# để random 1 số lượng phần tử nhất định | k là số lượng phần tử cần radom ra
a = random.sample(range(1,100),k= 50)
print(a)

# để tính số giây chương trình chạy
import time

start = time.perf_counter()
print([i*2 for i in a])
stop = time.perf_counter()

print(f"{stop-start}s")

# nén 2 phần tử lại thành 1 tuple
# hàm zip
a = [1,2,3]
b = list("abcd")

print(list(zip(a,b)))

# hoặc 
from itertools import zip_longest
print(list(zip_longest(a,b,fillvalue=1000)))

# enumerate

a = [1,2,3,4,5]
print(list(enumerate(a)))
print(list(enumerate(a,start=100)))

for index,value in enumerate(a):
    print(index,value)

##
for i in range(len(a)):
    print(i,a[i])
print("x"*45)
for index,value in enumerate(a):
    print(index,value)

# funtion: hàm
    
# def tên_hàm(tham số):
#     code
# tên_hàm(đối số)
    
# đối số mặc định luôn ở cuối cùng
# inf vô cùng
# -inf âm vô cùng
# mũ không(lũy thừa 0) của số nào cũng ra chính nó