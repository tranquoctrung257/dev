file = open("data.txt","w")
file.write("dung lai \n")
file.write("dung lai lap trinh")
file.close() # nếu không có dòng này sẽ bị báo lỗi

file = open("data.txt","w")
file.write("a \n")
file.write("b \n")
file.close()

# hoặc sử dụng hàm with thì không cần close

with open("data.txt","w") as file:
    file.write("a \n")
    file.write("b \n")
    file.write("c \n")
    file.write("d \n")

