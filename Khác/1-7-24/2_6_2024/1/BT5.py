# Bài tập 1

# #### 1. Cho một list chứa các tuple như sau: friends = [("Bob", "Male"), ("Anna", "Female"), ("Max", "Male")]

friends = [("Bob", "Male"), ("Anna", "Female"), ("Max", "Male")]
# + a. Cho biết chiều dài của friends
print(f"chiều dài của friends là {len(friends)}")

# + b. Lấy ra phần tử đầu, cuối và giữa và kiểm tra kiểu của chúng
dau = friends[0]
print(dau)
print(type(dau))

cuoi = friends[-1]
print(cuoi)
print(type(cuoi))

# + c. Nhập vào tên (name) và giới tính (gender) của một người bạn sau đó append vào friends tuple gồm hai giá trị (name, gender)

name = input("nhập vào tên: ")
gender = input("nhập vào giói tính: " )

friends.append((name,gender))

print(friends)

#### Bài 2. Tạo một set trống có tên là set_a
set_a = set()
# + a. Thêm 'Anna' vào set_a
set_a.add("Anna")
print(set_a)

# + b. Thêm một tuple ('Kenny', 'Jen', 'Danny')
set_a.update(('Kenny', 'Jen', 'Danny'))
print(set_a)

# + c. In ra set_a và tính chiều dài của nó
print(f"chiều dài của set_a {len(set_a)}")

# + d. Xóa 'Jen' ra khỏi set_a
set_a.remove("Jen")
print(set_a)

# + e. Xóa tất cả các giá trị từ set_a
set_a.clear()
print(set_a)