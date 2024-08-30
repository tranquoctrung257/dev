# list
#chỉ số 0 1 2 3 4
#      -5-4-3-2-1
nums = [1,2,3,4,5]

print(type(nums))
print(nums[-1])
print(nums[0])
print(len(nums))
print(nums[-len(nums)]) # luôn trả về giá trị đầu tiên theo chỉ số âm

# để thêm phần tử vào cuối
nums.append(100)
print(nums)

# để thêm 1 list vào 1 list hiện có dùng
nums.extend([1,4,64,23,112])
print(nums)

# để đảo ngược 1 list ta dùng
nums.reverse()
print(nums)

# xóa và trả về giá trị cuối cùng của list ta dùng
n = nums.pop()
print(n)
print(nums)

# để xóa đi phân tử đầu tiên tìm thấy của 1 list
nums.remove(4)
print(nums)

# để tìm số lần suât hiện của 1 phần tử trong list
number = nums.count(100)
print(number)

# để tìm vị trí của 1 phần tử nào đó trong list
print(nums.index(112))

# để sắp sếp từ bé đến lớn ta dùng
nums.sort()
print(nums)

# hoặc từ lớn đến bé
nums.sort(reverse=True)
print(nums)

# dể chèn 1 phần tử vào 1 list theo vị trí
nums.insert(1,120)
print(nums)

# để copy 1 list
num = nums.copy()
print(num)
print(num is nums)
print(num == nums)

# để xóa phần tử tại vị trí
nums.pop(3)
print(nums)

del nums[2]
print(nums)

# list slsing
# list[từ,đến,bước nhảy]
new_nums = nums[0:-1]
print(new_nums)
new_nums = nums[0:3]
print(new_nums)

# tạo 1 danh sách mới nhưng ngược lại của danh sách ban đầu
print(nums[::-1])
print(new_nums is num)

# [] - list

friends = [
    ["John",12],
    ["Mảy",23],
    ["Mark",33]
]
# để lấy phần tủ của 1 list in list
print(friends[0][1])

# để thêm 1 giá trị
friends[0].append("senior")
print(friends)

# để tính tổng ta dùng hàm sum
print(sum([1,34,5,6,7]))

# để copy 1 list sử dụng
lst = nums[:]
print(lst)

#để copy giá trị của list mà ko bị thay đổi
lst = [[31],[12],[423]]
lst1 = lst.copy()
lst[0].append(2)
print(lst1)

from copy import deepcopy

lst = [[31],[12],[423]]
lst1 = deepcopy(lst)
lst[0].append(2)
print(lst1)

# vd in ra đẹp
import pprint
n = [
    "12312iohuowerwer",
    "23423afjoahoewif2321",
    "2342io3h423opijr23r"
]
pprint.pprint(n)

# để tắt jupyter mình nhấn ctrl c để tắt