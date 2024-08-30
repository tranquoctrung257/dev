'''
1. Cho hai tập hợp (set)
art_students = {"John", "Max", "Anna", "Bob", "Obito"}
math_students = {"Max", "Mery", "David", "Anna", "Naruto", "John"}
a. Tìm những người bạn học cả vẽ lẫn toán
b. Tìm những người bạn học vẽ nhưng không học toán
c. Tìm những người bạn học toán nhưng không học vẽ
d. Tìm những người bạn học vẽ hay toán không phải cả hai
e. Tìm tất cả những người bạn
'''

art_students = {"John", "Max", "Anna", "Bob", "Obito"}
math_students = {"Max", "Mery", "David", "Anna", "Naruto", "John"}

# a.
art_math = art_students.intersection(math_students)
print(f"những người bạn học cả vẽ lẫn toán là: {art_students}")

# b.
art_math1 = art_students.difference(math_students)
print(f"những người bạn học vẽ nhưng không học toán: {art_math1}")

# c.
art_math2 = math_students.difference(art_students)
print(f"những người bạn học vẽ nhưng không học toán: {art_math2}")

# d.
art_math3 = math_students.symmetric_difference(art_students)
print(f"những người bạn học vẽ hay toán không phải cả hai: {art_math3}")

# e.
art_math_all = math_students.union(art_students)
print(f"tất cả những người bạn: {art_math_all}")

import json
'''
Cho dict sau:
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
Yêu cầu:
a. Lấy ra giá trị của các key sau: album_name, release_year bằng hai cách
b. Thay đổi giá trị của key: release_year từ 1973 thành 1971
c. Xóa phần tử với key là track_list
d. Thêm một key mới là amount = 2000 bằng hai cách
e. Làm trống dict: album_info
'''

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
# a.
# c1
print("giá trị của album_name là: ",album_info["album_name"])

# c2
print("giá trị của album_name là: ",album_info.get("album_name"))

# b.
album_info["release_year"] = 1971
print("giá trị sau thay đổi là: ",json.dumps(album_info,indent=4))

# c.
del album_info["track_list"]
print("giá trị hiện tại là:",json.dumps(album_info,indent=4))

# d.
# c1
info = {"amount":2000}
# album_info.update(info)

# c2
album_info["amount"] = 2000
print("giá trị sau thay dổi là: ",json.dumps(album_info,indent=4))

# e.
album_info.clear()
print("giá trị sau khi làm trống là:",album_info)