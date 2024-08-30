# 1.cho danh sách list friends = ["Jen","jack","Kenny","Jelly","Bob","Henry","Anne"]

# yêu cầu
# a lấy ra 4 người đầu tiên của friends
# b lấy ra 4 người cuối cùng của friends
# c đảo ngược danh sách friends
# d lấy ra người bạn từ vị trí 1 đến hết
# e copy danh sách ban đầu thành một danh sách mới
# f lấy ra những người bạn từ vị trí 2 đến sát cuối

friends = ["Jen","jack","Kenny","Jelly","Bob","Henry","Anne"]

# a
print("4 người đầu tiên của friends là : ",friends[:4])

# b
print("4 người cuối cùng của friends là : ",friends[-4:])

# c
print("Danh sách friends bị đảo ngược là: ",friends[::-1])

# d

print("người bạn từ vị trí 1 đến hết: ",friends[1:])

# e
friends3 = friends[:]
print("danh sách sau copy là: ",friends3)
print(friends3 is friends)
print(friends3 == friends)

# f 
print("những người bạn từ vị trí 2 đến sát cuối là :",friends[1:-1])

# 2.cho sanh sách các sinh viên chứa thông tin của mỗi sinh viên "ID:{id,tên,tuổi}" như sau
# studens = [["SV001","Bob",23],["SV002","Kenny",34],["SV003","Henry",45]]
# yêu cầu
# a.lấy ra thông tin của sinh viên thứ nhất và in ra định dạng "ID:{id},name{name}-age{age}"
# b.lấy ra tuổi của sinh viên thứ hai
# c.lấy ra thông tin hai sinh viên cuối cùng
# d. lấy ra id của sinh viên thứ 3

studens = [["SV001","Bob",23],["SV002","Kenny",34],["SV003","Henry",45]]

# a.
print("""thông tin của sinh viên thứ nhất là: ID:{} ,
                                     Name:{} - age:{}""".format((studens[0][0]),(studens[0][1]),(studens[0][2])))

# b.
print("tuổi của sinh viên thứ hai là:",studens[1][2])

# c.
print("thông tin hai sinh viên cuối cùng là: ", studens[1],studens[-1])

# d.
print(f"id của sinh viên thứ 3:{studens[-1][0]}")
print(f"id của sinh viên thứ 3:{studens[2][0]}")