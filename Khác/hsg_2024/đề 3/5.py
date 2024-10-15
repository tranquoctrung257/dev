# Bài 5. Thiết lập thuật toán chia để trị để giải bài toán sau: Cho trước dãy A gồm n phần tử đã được sắp xếp theo thứ tự tăng dần, ví dụ:
# A= [1, 2, 3, 3, 4, 4, 4, 5, 6, 6]
# Cho trước giá trị K, cần tìm ra vùng chỉ số gồm các phần tử bằng K. Chương trình cần trả về hai chỉ số start, end là vị trí bắt đầu và kết thúc gồm toàn các giá trị K. Nếu không tìm thấy K thì phải trả về -1, -1.
# Trong ví dụ trên, nếu K = 4 thì cần trả về hai chỉ số 4, 6.

def find_start_end(A, K):
    n = len(A)
    start, end = -1, -1

    left, right = 0, n - 1
    while left <= right:
        mid = left + (right - left) // 2
        if A[mid] < K:
            left = mid + 1
        elif A[mid] > K:
            right = mid - 1
        else:
            start = mid  
            right = mid - 1  


    left, right = 0, n - 1
    while left <= right:
        mid = left + (right - left) // 2
        if A[mid] < K:
            left = mid + 1
        elif A[mid] > K:
            right = mid - 1
        else:
            end = mid  
            left = mid + 1  

    if start == -1:
        return -1, -1  
    return start, end  


A = [1, 2, 3, 3, 4, 4, 4, 5, 6, 6]
K = 4
result = find_start_end(A, K)
print(f"Bắt đâu ở vụ trí: {result[0]}, Kết thúc ở vị trí: {result[1]}")
