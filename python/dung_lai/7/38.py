# FILE IO

file = open("data.txt","r")

# file.write("quoctrung\n")
# file.write("aaa")
# "w" writting nếu chưa có thì tạo và ghi nội dung nếu có rồi thì xóa file cũ thêm nội dung 
# "r" reading mở file 
# "a" writting append thêm vào cuối file

data = file.read()

print(data)