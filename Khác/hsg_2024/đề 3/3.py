# Bài 3. Để tính giá trị (số nguyên) gần đúng căn bậc hai của số tự nhiên n cho trước:, người ta đã thiết lập hàm sau với ý tưởng gần tương tự thuật toán tìm kiếm tuần tự như sau: 
 
# Hãy thiết kế lại thuật toán tìm số nguyên lớn nhất không vượt quá căn bậc hai của n bằng kĩ thuật chia để trị.

def n(n):
    if n < 0:
        return False
    if n == 0 or n == 1:
        return n
    
    low, high = 0, n
    result = 0

    while low <= high:
        mid = (low + high) // 2
        if mid * mid == n:
            return mid  
        elif mid * mid < n:
            result = mid  
            low = mid + 1
        else:
            high = mid - 1
    
    return result


print(n(100000000044233423845973498757843))