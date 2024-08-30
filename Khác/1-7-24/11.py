"""
python functions
"""
# định nghĩa hàm my_func
def my_func():
    print("hello word")

my_func()

def my_func(msg):
    print(msg)
my_func("hello")

def show_full_name(fname,lname): # tham số 
    print(f"{fname} {lname}")

show_full_name("John","Doe") # đối số 

# đối số phải truyền vào đủ giá trụ của tham số

# có thể gán tham số mặc định trước
def show_full_name(fname,lname="Doe"):
    return f"{fname} {lname}"
    # return chỉ chạy 1 lần trong hàm

print(show_full_name("John"))
full_name = show_full_name("John","wih")
print(full_name)

def get_full_name(fname,lname="Doe"):
    if fname:
        return f"{fname} {lname}"
    return f"Kenny {lname}"
full_name = get_full_name("")
print(full_name)

# có thể truyền vào mà không cần vị trí biết vị trí của tham số
full_name = get_full_name(lname="Jelly",fname="Joe")
print(full_name)

def add(x,y=100):
    return x+y
print(add(y=10,x=5))

# trường hợp tránh khi sử dụng tham số mặc định
def func(lst=[]):
    lst.append(2)
    print(lst)
func()
func()

friends = ["Kenny","Bob","Jen"]

# để sử dụng friends trong hàm thì ta dùng
def my_func():
    # friends nếu không tìm thấy trong hàm sẽ tìm bên ngoài
    f = friends + ["Joe"]
    print(f)

my_func()

# hàm lambda thực hiện những công việc tính toán cơ bản ngắn gọn chỉ trong 1 biếu thức trả về
# thường được dùng trong các hàm như max sort ,...
add = lambda x,y : x+y
print(add(1,2))

def greet(msg):
    return "Hello, ",msg

hello = greet
print(hello("Jen"))

# *args
def add(x,y,z,t):
    return x+y+z+t
print(add(2,3,4,5))


def add(*args):
    print(type(args))
    return sum(args)
# các đối số vị trí là những đối số không có tên
# *args chỉ lấy những đối số không tên
print(add(2,3,4,5))

lst = [2,4,6,7,4]
print(*lst)

lst = [3,10,4,5,6,7]

# để in ra số đầu, giữa , cuối
first, *mid, last = lst
print(first)
print(mid)
print(last)

*first, last = lst
print(first)
print(last)

def add(*lst, operation):
    return operation(lst)

print(add(1,2,3,4,operation=sum))

# ko nên nhân 1 list với 1 số
lst = [[]] * 5
lst[1].append(2)
print(lst)

# để khắc phục 
lst = [[] for _ in range(5)]
lst[1].append(2)
print(lst)

# tham số mặc định phải đứng sau tham số có tên
# def func(a=3,b):
#     pass

def func(b,a=3):
    pass