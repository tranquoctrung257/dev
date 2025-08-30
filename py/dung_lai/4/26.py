# 26 hàm main, global variable biến sử dụng toàn chương trình,local variable biến sử dụng trong hàm.

def print_hocsinh_A():
    print("Học sinh A")
    print("Toan: 9")
    print("Văn: 6")
def print_hocsinh_B():
    print("Học sinh B")
    print("Toan: 5")
    print("Văn: 7")

def main():
    print_hocsinh_A()
    print_hocsinh_B()
    # cả chương trình sẽ gọi đúng 1 hàm main thôi 
main()

print_hocsinh_A()
print_hocsinh_B()
# nếu gọi hàm trước khi tạo hàm sẽ lỗi

def print_hocsinh_A():
    print("Học sinh A")
    print("Toan: 9")
    print("Văn: 6")
def print_hocsinh_B():
    print("Học sinh B")
    print("Toan: 5")
    print("Văn: 7")


def main():
    print_hocsinh_A()
    print_hocsinh_B()
    # nếu để hàm main lên trên cùng thì vẫn chạy

def print_hocsinh_A():
    print("Học sinh A")
    print("Toan: 9")
    print("Văn: 6")
def print_hocsinh_B():
    print("Học sinh B")
    print("Toan: 5")
    print("Văn: 7")

main()    