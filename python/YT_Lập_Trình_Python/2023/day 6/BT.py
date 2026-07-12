# ## 3. Bài tập
# #### 1. Cho một list chứa các tuple như sau: friends = [("Bob", "Male"), ("Anna", "Female"), ("Max", "Male")]
friends = [("Bob", "Male"), ("Anna", "Female"), ("Max", "Male")]

# + a. Cho biết chiều dài của friends
print(f"biết chiều dài của friends là: {len(friends)}")

# + b. Lấy ra phần tử đầu, cuối và giữa và kiểm tra kiểu của chúng
first = friends[0]
mid = friends[1]
last = friends[-1]

print(f"phần tử đầu là: {first}")
print(f"kiểu của phần tử đầu là {type(first)}")
print(f"phần tử giữa là: {mid}")
print(f"kiểu của phần tử giữa là {type(mid)}")
print(f"phần tử cuối là: {last}")
print(f"kiểu của phần tử cuối là {type(last)}")

# + c. Nhập vào tên (name) và giới tính (gender) của một người bạn sau đó append vào friends tuple gồm hai giá trị (name, gender)
name = input("nhập vào tên: ")
gender = (input("nhập giới tính: "))
friends_update = (name,gender)
friends.append(friends_update)   
print(friends)

#### 2. Tạo một set trống có tên là set_a

set_a = set()

# + a. Thêm 'Anna' vào set_a
set_a.add("Anna")
print("set 1 sau khi Anna: ",set_a)
# + b. Thêm một tuple ('Kenny', 'Jen', 'Danny')

set_a.update(('Kenny', 'Jen', 'Danny')) ###########################

# + c. In ra set_a và tính chiều dài của nó
print(set_a)
print(len(set_a))
# + d. Xóa 'Jen' ra khỏi set_a
set_a.remove("Jen")
print("set_a sau khi xóa Jen",set_a)
# + e. Xóa tất cả các giá trị từ set_a
set_a.clear()
print("set_a sau khi Xóa tất cả các giá trị là: ",set_a)