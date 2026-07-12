# ## 7. Bài tập
# 1. Định nghĩa 4 hàm add, subtract, divide, multiply (+, -, /, *). Mỗi hàm nhận vào hai tham số thực hiện lần lượt các phép toán cộng, trừ, chia, nhân. Lưu ý hàm nên trả về thay vì in ra.
def add(x,y):
    return x+y 


def subtract(x,y):
    return x-y


def divide(x,y):
    return x/y

def multiply(x,y):
    return x*y 

print(add(1,2))
print(subtract(1,2))
print(divide(1,2))
print(multiply(1,2))

# 2. Định nghĩa một hàm được gọi là print_show_info nhận vào một tham số duy nhất đó là một dict, lúc gọi thì sử dụng dict như sau:

def print_show_info(tv_show):
    print(f"{tv_show['title']} {tv_show['initial_release']} - {tv_show['seasons']} seasons")
tv_show = {
    "title": "Breaking Bad",
    "seasons": 5,
    "initial_release": 2008
}
print_show_info(tv_show)
# + Hàm nên in ra một chuỗi có định dạng như sau:
# + Breaking Bad (2008) - 5 seasons