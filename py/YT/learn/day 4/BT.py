# 1. Tạo một movies list chứa tên các bộ phim đã xem
movies_list = ["Doremon",
               "gió",
               "người phán sử",
               "one piece",
               "Pokemon"]

# 2. Sử dụng hàm input để nhập vào một bộ phim khác không có trong movies list
movie = input("Nhập tên Bộ phim khác không có trong movies list: ")

# 3. Thêm bộ phim vừa nhập vào cuối của danh sách movies
movies_list.append(movie)

# 4. In ra bộ phim đầu tiên, cuối cùng và ở giữa movies list
dau = movies_list[0]
cuoi = movies_list[-1]
giua = movies_list[len(movies_list)//2]

print("bộ phim đầu tiên là:", dau)
print("bộ phim giữa là:", giua)
print("bộ phim cuối là:", cuoi)
# 5. Tính tổng bộ phim có trong movies
print("Tổng bộ phim hiện có là: ", len(movies_list))

# 6. Xóa bộ phim đầu và cuối trong movies
del movies_list[0]
del movies_list[-1]
print("danh sách sau khi xóa bộ phim đầu và cuối là: ", movies_list)

# 7. Lấy ra và xóa bộ phim cuối cùng trong movies
last = movies_list.pop()
print("Bộ phim cuối cùng là: ", last)
print("Danh sách còn lại là: ", movies_list)

# 8. Chèn một bộ phim bất kỳ vào đầu danh sách movies
movies_list.insert(1, "One Piece")
print("danh sách phim sau khi chèn là: ", movies_list)

# 9. Đếm số bộ phim có tiêu đề là "One Piece"
print("số lượng bộ phim có tiêu đề One Piece là: ",
      movies_list.count("One Piece"))

# 10. Tìm vị trí của bộ phim có tên là "gió"
print('vị trí của bộ phim có tên "gió" là: ', movies_list.index("gió"))

# 11. Thêm một danh sách bộ phim khác vào cuối danh sách movies ban đầu
movies_list.extend(["thủy hử", "tam quốc diễn nghĩa"])
print("danh sách phim ban sau sau khi thêm danh sách khác là: ", movies_list)

# 12. Xóa tất cả các bộ phim có trong danh sách
movies_list.clear()
print(f"danh sách movies_list sau khi xóa là: {movies_list}")
