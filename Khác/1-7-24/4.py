# list
        # 0 1 2  3 
#        -4-3-2 -1
number = [1,2,4,4.5]
print(type(number))
print(number)
print(number[0])
print(number[-1])
print(number[3])

# để thêm phần tử vào 1 list thì dùng append()
number.append(43)
print(number)

# để xóa 1 phần tử trong 1 list
# remove chỉ xóa phần tử tìm thấy đầu tiên trong list
number.remove(4)
print(number)

# dể xóa đi giá trị cuối và lưu lại ta dùng pop() 
last_value = number.pop()
print(number)
print(last_value)

# để thêm 1 list mới và 1 list cũ ta dùng extend([])
number.extend([2,3,4,5,11.3,44,3,444.22,1,1])
print(number)

# để thay đổi 1 phần tử ta truy cập vào vị trí phần tử đó và thay đổi
number[0] = 8.6
print(number)

# để tính số lượng của 1 phần tử nào đó trong list ta dùng count()
amount = number.count(1)
print(amount)

# để xem chiều dài của list là bao nhiêu ta dùng len()
print(len(number)) 

# để chèn 1 phần tử vào 1 vị trí nào đó ta dùng insert(vị trí,giá trị)
number.insert(3,1000)
print(number)

# để ti,f 2 vị trí phần tử nào đó ta dùng index()
print(number.index(4.5))

# để đảo ngược 1 list ta dùng reverse()
number.reverse()
print(number)

# để sắp sếp theo thứ tự tăng dần của list ta dùng sort()
number.sort()
print(number)

# để sắp sếp theo thứ tự từ giảm dần của list ta dùng sort(reverse=True)
number.sort(reverse=True)
print(number)

# để xóa 1 phần tử trong list theo phần tử
del number[1]
print(number)

# để tìm 1 số lớn nhất trong 1 list
print(max(number))

# để tìm 1 số bé nhất trong 1 list
print(min(number))

# để xóa tất cả 1 list ta dùng clear()
number.clear()
print(number)

# để xem tất cả phương thức của list ta vào idle gõ dir(list)

