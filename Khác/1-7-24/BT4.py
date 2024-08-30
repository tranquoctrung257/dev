# 1.khởi tạo 1 danh sách phim đã xem
movie_list = ["đế chế diệt vong",
              "trở lại thành thần",
              "về nhà đi con",
              "vị thần của gió"]

# 2.tạo 1 movie chứa các dánh sách phim đã xem
print("phim đã xem: ", movie_list)

# 3.sử dụng hàm input để nhập một bộ phim khác không có trong movie list
list_phim = input("nhập một bộ phim khác không có trong movie list: ")
movie_list.append(list_phim)
print(movie_list)

# 4.in ra bộ phim đầu tiên cuối cùng và giữa của movie_list
count_list = len(movie_list)//2
print(f"""Đầu:{movie_list[0]}
      Cuối:{movie_list[-1]}
      Giưa:{movie_list[count_list]}""")

# 5.tính tổng bộ phim có trong movie list
print("tổng bộ phim của movie_list là: ",len(movie_list))

# 6.xóa bộ phim đầu và cuối trong movie list
movie_list.remove(movie_list[0])
del movie_list[-1]
print("Danh sách hiện tại là: ",movie_list)

# 7.lấy ra và xóa phim cuối cùng của movie list
movie_list_new = movie_list.pop()
print("Bộ phim cuối cùng được xóa là",movie_list_new)
print("Danh sách hiện tại sau khi xóa phần tử cuối cùng là: ",movie_list)

# 8.chèn một bộ phim bất kì vào đầu movie list
movie_list.insert(0,input("nhập bộ phim mới vào movie_list: "))
print('danh sách hiện tại sau khi thêm là: ',movie_list)

# 9.Đếm số bộ phim có tiêu đề là trở lại thành thần
amuont = movie_list.count("trở lại thành thần")
print("số bộ phim có tiêu đề trở lại thành thần là :",amuont)

# 10.tìm vị trí của bộ phim về nhà đi con
index_of_ve_nha_di_con = movie_list.index("về nhà đi con")
print("vị trí của bộ phim về nhà đi con là: ",index_of_ve_nha_di_con)

# 11.thêm một danh sách bộ phim khác vào cuối danh sách phim ban đầu
movie_list.extend(["Harry Potter","ánh sáng cuối chân trời"])
print("Danh sách sau khi thêm là {}".format(movie_list))

# 12.xóa tất cả bộ phim trong danh sách
movie_list.clear()
print("danh sách cuối cùng là: ",movie_list)