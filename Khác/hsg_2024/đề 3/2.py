# Bài 2. Cho trước danh sách gồm có tên, điểm thi và được sắp xếp theo thứ tự tăng dần của điểm thi, ví dụ danh sách: [["Bình", 7.5], ["Hoa", 8], ["An", 9], ["Quang", 10]]. Viết chương trình nhập một điểm số và tìm tên học sinh có điểm thi bằng điểm số đã nhập, nếu không tìm thấy thì thông báo "không có".

# dữ liệu vào
arr = [["Bình", 7.5], ["Hoa", 8], ["An", 9], ["Quang", 10]]

# xử lý

D = 8.0

for i in range(len(arr)):
    if arr[i][-1] == D:
        print(arr[i][0])
        break
else:print("không có")