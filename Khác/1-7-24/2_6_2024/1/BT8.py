# 1. Định nghĩa 4 hàm add, subtract, divide, multiply (+, -, /, *). Mỗi hàm nhận vào hai tham số thực hiện lần lượt các phép toán cộng, trừ, chia, nhân. Lưu ý hàm nên trả về thay vì in ra.

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def divide(a, b):
    if b != 0:
        return a / b
    return float("inf")
    # return float("-inf")


def multiply(a, b):
    return a * b


# print(add(1,10))
# print(subtract(1,10))
# print(divide(1,10))
# print(multiply(1,10))

assert add(1, 10) == 11, "error"
print("true")

# 2.Định nghĩa một hàm được gọi là print_show_info nhận vào một tham số duy nhất đó là một dict, lúc gọi thì sử dụng dict như sau:

# Hàm nên in ra một chuỗi có định dạng như sau:
# Breaking Bad (2008) - 5 seasons
tv_show = {
    "title": "Breaking Bad",
    "seasons": 5,
    "initial_release": 2008
}


def print_show_info(info):
    print("{0} ({1}) - {2} seasons".format(info["title"], info["initial_release"], info["seasons"]))


print_show_info(tv_show)
