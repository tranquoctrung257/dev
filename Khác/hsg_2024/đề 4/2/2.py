# Bài 2. Phân tích và viết chương trình để thực hiện các yêu cầu sau:
# a) Tìm học sinh có điểm Toán bằng 8.9.
# b) Tìm một học sinh có tổng điểm ba môn Toán, Vật lí, Hoá học lớn hơn 26.5.
# c) Tìm học sinh có tổng điểm ba môn Toán, Vật lí, Hoá học nhỏ nhất.


# đữ liệu vào là file data.in gồm tên,điểm_môn_toán,điểm_môn_lý,điểm_môn_hóa


lst = []
with open("data.in",encoding="utf8") as file:
    for i in file:
        line = i.strip().split()
        name = line[0]
        numbers = [float(num.replace(',', '.')) for num in line[1:]]
        lst.extend([[name,numbers]])
# a)
for ds in lst:
    for i in ds[1]:
        if i == 8.9:
            print("bạn có điểm 8.9 là bạn:",ds[0])
        else:break
# b)
for ds in lst:
    sum = 0
    for i in ds[1]:
        sum+=i
    if sum >= 26.5:
        print("bạn học sinh có tổng điểm ba môn Toán, Vật lí, Hoá học lớn hơn 26.5 là:",ds[0])

# c)
lst_ = []
for ds in lst:
    lst_.append([ds[0], sum(ds[1])]) 

min_ = min(lst_, key=lambda person: person[1])
print("bạn học sinh có điểm thấp nhất là:",min_[0])

