# 25 return value 

# def add_one(number):
#     number = number+1
#     # truyền cái gì vào trong hàm nó sẽ tạo 1 phiên bản copy của con số ấy nên ở trường hợp này sẽ ko trả về số 3

# x = 2 
# add_one(x)

def add_one(number):
    number+=1
    return number

x = 2
new_number = add_one(x)
print(new_number)