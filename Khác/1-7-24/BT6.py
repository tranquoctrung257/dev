# Bài1
# cho một list có chứa tuple như sau: friends = [("Bob","Male"),("Anna","Female"),("Max","Male")]
# a. cho biết chiều dài của frieds
# b. lấy ra phần tử đầu, cuối và giữa và kiểm tra kiểu của chúng
# c. nhập vào tên (name) và giới tính (grender) của người bạn sau đó append vào friends tuple

friends = [("Bob","Male"),("Anna","Female"),("Max","Male")]
# a.
print("Chiều dài của friends là:",len(friends))

# b.
dau = friends[0]
giua = friends[1]
cuoi = friends[-1]
print(f"""
phần tử đầu của {friends} : {dau}
và kiểu dữ liệu của phần tử đầu là {type(dau)}
phần tử giữa của {friends} : {giua}
và kiểu dữ liệu của phần tử giữa là {type(giua)}
phần tử cuối của {friends} : {cuoi}
và kiểu dữ liệu của phần tử cuối là {type(cuoi)}
""")

# c.
name = input("nhập vào tên người bạn: ")
grender = input("nhập vào giới tính người bạn: ")

friends_tuple = (name,grender)
print(friends_tuple)
friends.append((friends_tuple))

print("danh sách hiện có là: ",friends)

print("-"*30)

# 2. tạo 1 set trống có tên là set_a

# set_a = {}
set_a = set()

print(set_a)

# a. thêm Anna vào set_a
set_a.add("Anna")
print(set_a)

# b. thêm 1 tuple {("Kenny","Jen","Danny")}
set_a.update(("Kenny","Jen","Danny"))
print(set_a)

# c. in ra set_a, và tính chiều dài của nó
print(set_a)
print(f"Chiều dài của {set_a} là :",len(set_a))

# d. xóa Jen ra khỏi set_a
set_a.remove("Jen")
print(set_a)

# e. xóa tất cả giá trị của set_a
set_a.clear()
print(set_a)