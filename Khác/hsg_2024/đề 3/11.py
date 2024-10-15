# Bài 11. Cho dãy số A, cần tìm phần tử mốt (mode) của A. Phần tử mốt là phần tử có số lần xuất hiện nhiều nhất trong A. Nếu tồn tại nhiều thì chỉ yêu cầu tìm ra một phần tử mốt. Yêu cầu sử dụng kĩ thuật chia để trị.

def slxh(arr,num,t,p):
    cout = 0
    for i in range(t, p + 1):
        if arr[i] == num:
            cout +=1
    return cout
def find_mode(arr, left, right):
    if left == right:
        return arr[left]
    mid = (left+right)//2
    l_m = find_mode(arr, left, mid)
    r_m = find_mode(arr, mid + 1, right)

    if l_m == r_m:
        return l_m
    p_cout  = slxh(arr, l_m, left, right)
    t_cout = slxh(arr, r_m, left, right)
    if p_cout > t_cout:
        return l_m
    return r_m

arr = [2, 2, 1, 1,1,1, 1, 2, 2,4]
mode = find_mode(arr, 0, len(arr) - 1)
print(f'Phần tử mốt là: {mode}')
