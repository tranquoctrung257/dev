# 27 global variable,local variable

def main():
    Students_A_name = "Dung" # local variable
    Students_B_name = "Nguyen"
    # các biến trên chỉ hoạt động ở trong hàm main thôi chứ gọi ở hàm khác sẽ không được.
    print_Student_A()
    print_student_B()
    # nếu như này sẽ gặp lỗi 

def print_Student_A():
    print("student A")
    print("Toan: 9")
    print("Văn: 6")
def print_student_B():
    print("student B")
    print("Toan: 5")
    print("Văn: 7")
main()


# nếu muốn chạy bth thì phải như thế này 
def main():
    # Students_B_name = "Nguyen"
   
    print_Student_A()
    print_student_B()

def print_Student_A():
    print("student A"+Students_A_name)
    print("Toan: 9")
    print("Văn: 6")
def print_student_B():
    print("student B")
    print("Toan: 5")
    print("Văn: 7")

Students_A_name = "Dung"  # global variable không nên sử dụng

main()

def main():
    Students_A_name = "Dung"
    Students_B_name = "Nguyen"
   
    print_Student_A(Students_A_name)
    print_student_B(Students_B_name)

def print_Student_A(name):
    print("student A: "+name)
    print("Toan: 9")
    print("Văn: 6")
def print_student_B(name):
    print("student B: "+ name)
    print("Toan: 5")
    print("Văn: 7")


main()
