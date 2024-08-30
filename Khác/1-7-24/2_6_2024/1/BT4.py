# Bài 1
# 1. Tạo một movies list chứa tên các bộ phim đã xem

movies_list = ["trảng quỳnh","Naruto","Fairy Tail","gió","Fairy Tail"]
# 2. Sử dụng hàm input để nhập vào một bộ phim khác không có trong movies list
movies = input("nhập vào một bộ phim khác không có trong movies list: ")

# 3. Thêm bộ phim vừa nhập vào cuối của danh sách movies
movies_list.append(movies)
print(f"danh sách sau khi thay đổi là: {movies_list}")

# 4. In ra bộ phim đầu tiên, cuối cùng và ở giữa movies list
print(f"Bộ phim đầu tiên {movies_list[0]}")
print(f"Bộ phim cuối cùng {movies_list[-1]}")
print(f"Bộ phim ở giữa {movies_list[len(movies_list)//2]}")

# 5. Tính tổng bộ phim có trong movies
print(f"tổng bộ phim có trong movies: {len(movies_list)}")

# 6. Xóa bộ phim đầu và cuối trong movies
del movies_list[0]
del movies_list[-1]
print(f"danh sách movies sau khi thêm là {movies_list}")

# 7. Lấy ra và xóa bộ phim cuối cùng trong movies
movies_ = movies_list.pop()
print(f"Bộ phim cuối cùng: {movies_}")
print(f"danh sách movies hiện tại là: {movies_list}")

# 8. Chèn một bộ phim bất kỳ vào đầu danh sách movies
movies_list.insert(1,"One Piece")
print(movies_list)

# 9. Đếm số bộ phim có tiêu đề là "One Piece"
count = movies_list.count("One Piece")
print(f"số bộ phim có tiêu đề là One Piece là: {count}")

# 10. Tìm vị trí của bộ phim có tên là "gió"
print(f'vị trí của bộ phim có tên là "gió" là {movies_list.index("gió")}')

# 11. Thêm một danh sách bộ phim khác vào cuối danh sách movies ban đầu
new_movies = ["Pokemon","Bleach"]
movies_list.extend(new_movies)
print(f"danh sách sau khi thêm là: {movies_list}")

# 12. Xóa tất cả các bộ phim có trong danh sách
movies_list.clear()
print(f"danh sách sau khi xóa là: {movies_list}")

## bài 2
friends = ["Jen", "Jack", "Kenny", "Jelly", "Bob", "Henry", "Anne"]

#a Lấy ra 4 người bạn đầu tiên trong friends
print(f"4 người bạn đầu tiên trong friends là: {friends[:4]}")

#b Lấy ra 4 người bạn cuối trong friends
print(f"4 người bạn cuối trong friends là {friends[3:]}")

#c Đảo ngược danh sách friends
reversed_lst = friends[::-1]
print(f"danh sách sau khi Đảo ngược friends là {reversed_lst}")

#e Copy danh sách ban đầu thành một danh sách mới
lst_copy = friends.copy()
print(friends is lst_copy)
print(friends == lst_copy)

#f Lấy ra những người bạn từ vị trí 2 đến sát cuối
print(f"những người bạn từ vị trí 2 đến sát cuối{friends[2:-1]}")

##
#            0          1      2
students = [
            ["SV001", "Bob", 23],     #    0
            ["SV002", "Kenny", 34],   #    1
            ["SV003", "Henry", 45]    #    2
]

#a Lấy ra thông tin của sinh viên thứ nhất và in ra định dạng "ID: {id}, name: {name} - age: {age}"

print(f"ID: {students[0][0]}, name: {students[0][1]} - age: {students[0][-1]}")

#b Lấy ra tuổi của sinh viên thứ hai
print(students[1][-1])

#c Lấy ra thông tin hai sinh viên cuối cùng
print(f"ID: {students[1][0]}, name: {students[1][1]} - age: {students[1][-1]}")
print(f"ID: {students[-1][0]}, name: {students[-1][1]} - age: {students[-1][-1]}")

#d Lấy ra id của sinh viên thứ ba
print(f"ID: {students[-1][0]}")
