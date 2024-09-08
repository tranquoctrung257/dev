# Đọc file 
with open("GAME.INP") as fi:
    chuoi = fi.read().strip()

d = 0  # Đếm số lần Đức thắng
n = 0  # Đếm số lần Nhi thắng
h = 0  # Đếm số lần hòa

# Xử lý chuỗi
for i in chuoi:
    if i == "D":
        d += 1
    elif i == "N":
        n += 1
    elif i == "H":
        h += 1

# Ghi file
with open("GAME.OUT", "w") as f_out:
    print(d, n, file=f_out)