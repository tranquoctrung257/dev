# Bài 3. Cho trước dãy n số nguyên. Viết chương trình đếm và liệt kê tất cả các bộ 3 phần tử liền nhau của dãy thoả mãn điều kiện ba số này là 3 số nguyên liên tiếp (có thể tăng dần hoặc giảm dần).

def check(a,b,c):
    return (a == b - 1 and b == c - 1) or (a == b + 1 and b == c+1)

def find_(arr):
    lst = []
    for i in range(len(arr)-2):
        if check(arr[i],arr[i+1],arr[i+2]):
            lst.append((arr[i],arr[i+1],arr[i+2]))
    return lst

arr = list(map(int, input("Nhập dãy các số nguyên, cách nhau bởi dấu cách: ").split()))
s = find_(arr)
if s:
    print(f"Các bộ 3 số nguyên liên tiếp là: {s}")
    print(f"Số lượng các bộ 3 là: {len(s)}")
else:
    print("Không có bộ 3 số nguyên liên tiếp nào trong dãy.")