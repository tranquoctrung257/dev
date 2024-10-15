# Bài 1. Viết chương trình đệ quy để tính giá trị H(n) của bài toán Tháp Hà Nội
def hanoi(n):
    if n == 1:
        return 1
    else:
        return 2 * hanoi(n - 1) + 1
    
# ví dụ nhập 3 đĩa
print(hanoi(3))