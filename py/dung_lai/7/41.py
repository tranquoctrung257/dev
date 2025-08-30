color = ["red","green","blue","yellow"]

print(color)

color.remove("green")

print(color)

# để xóa đi phần tử cuối cùng dùng hàm pop

color.pop()

# để thêm 1 phần tử ở vị trí bất kì 

color.insert(0,"black")

print(color)

color.insert(1,"purple")

print(color)

# để tìm vị trí của một phần tử nào đó

print(color.index("red"))

# trong 1 list có nhiều thằng red thì có cách nào để tìm vị trí xuất hiện của nó

color = ["red","green","blue","yellow","red"]

red_index = []

for i in range(len(color)):
    if color[i] == "red":
        red_index.append(i)

print(red_index)

# số lần xuất hiện của red
print(color.count("red"))

# để sắp xếp list 
a = [1,2,3,4,5,432,42,3,234,2]
a.sort()
print(a)

# để sửa 1 phần tử trong list

a[0] = "trung"

print(a)