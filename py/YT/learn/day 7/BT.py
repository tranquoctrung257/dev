# ## 3. Bài tập
# 1. Cho hai tập hợp (set)
# + art_students = {"John", "Max", "Anna", "Bob", "Obito"}
# + math_students = {"Max", "Mery", "David", "Anna", "Naruto", "John"}

art_students = {"John", "Max", "Anna", "Bob", "Obito"}
math_students = {"Max", "Mery", "David", "Anna", "Naruto", "John"}
# + Tìm những người bạn học cả vẽ lẫn toán
print(art_students.intersection(math_students))

# + Tìm những người bạn học vẽ nhưng không học toán
print(art_students.difference(math_students))

# + Tìm những người bạn học toán nhưng không học vẽ
print(math_students.difference(art_students))

# + Tìm những người bạn học vẽ hay toán không phải cả hai
print(art_students.symmetric_difference(math_students)) # lấy cả 2 cái trừ đi phần chung

# + Tìm tất cả những người bạn
print(art_students.union(math_students))



print("_"*19)

# 2. Cho dict sau:
album_info = {
    "album_name": "The Dark Side of the Moon",
    "band": "Pink Floyd",
    "release_year": 1973,
    "track_list": [
        "Speak to Me",
        "Breathe",
        "On the Run",
        "Time",
        "The Great Gig in the Sky",
        "Money",
        "Us and Them",
        "Any Colour You Like",
        "Brain Damage",
        "Eclipse"
    ]
}
# + Yêu cầu:
# + 1. Lấy ra giá trị của các key sau: album_name, release_year bằng hai cách
print("C1")
print(album_info["album_name"])
print(album_info.get("album_name"))
print("C2")

print(album_info["release_year"])
print(album_info.get("release_year"))
# + 2. Thay đổi giá trị của key: release_year từ 1973 thành 1971
album_info["release_year"] = 1971

print(album_info)

# + 3. Xóa phần tử với key là track_list

del album_info["track_list"]
print(album_info)

# + 4. Thêm một key mới là amount = 2000 bằng hai cách
album_info["amount"] = 2000
album_info.update(amount = 2000)

print(album_info)

# + 5. Làm trống dict: album_info

album_info.clear()

print(album_info)