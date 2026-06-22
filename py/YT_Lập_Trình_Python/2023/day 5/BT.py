# ## 4. Bài tập
# 1. Cho danh sách (list) friends = ["Jen", "Jack", "Kenny", "Jelly", "Bob", "Henry", "Anne"]
friends = ["Jen", "Jack", "Kenny", "Jelly", "Bob", "Henry", "Anne"]

# + Yêu cầu:
# + a. Lấy ra 4 người bạn đầu tiên trong friends
print(friends[:4])

# + b. Lấy ra 4 người bạn cuối trong friends
print(friends[-4:])
# + c. Đảo ngược danh sách friends
print(friends[::-1])

# + d. Lấy ra những người bạn từ vị trí 1 đến hết
print(friends[1:])

# + e. Copy danh sách ban đầu thành một danh sách mới
friends_new = friends[:]
print(friends is friends_new)
print(friends == friends_new)

# + f. Lấy ra những người bạn từ vị trí 2 đến sát cuối

################
print(friends[2:-1])
################


# 2. Cho danh sách các sinh viên chứa thông tin của mỗi sinh viên [id, tên, tuổi] như sau: 

# + students = [["SV001", "Bob", 23], ["SV002", "Kenny", 34], ["SV003", "Henry", 45]]

students = [["SV001", "Bob", 23], ["SV002", "Kenny", 34], ["SV003", "Henry", 45]]
# + Yêu cầu:
# + a. Lấy ra thông tin của sinh viên thứ nhất và in ra định dạng "ID: {id}, name: {name} - age: {age}"
print(f"ID: {students[0][0]}, name: {students[0][1]} - age: {students[0][2]}")

# + b. Lấy ra tuổi của sinh viên thứ hai
print(f"tuổi của sinh viên thứ 2 là: {students[1][2]}")
# + c. Lấy ra thông tin hai sinh viên cuối cùng
print(students[1:])
# + d. Lấy ra id của sinh viên thứ ba
print(students[-1][0])