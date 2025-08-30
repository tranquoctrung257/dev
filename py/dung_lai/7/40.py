color = ["red","green","blue"]

# để in theo từng vị trí bắt đầu từ 0
print(color[1])

# để hiện thị độ dài
print(len(color))

# để thêm phần tử vào cuối list 

color.append("yellow")

print(color[-1])

for i in range(4):
    print(color[i])

# để in ra vị trí cuối cùng  
last_index = len(color) -1
print(color[last_index])

# hoặc
print(color[-1])