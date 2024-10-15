# Bài 6. Cho một dãy số bất kì (chưa được sắp xếp) và một số K, hãy tìm số lần xuất hiện của K trong dãy số trên. Yêu cầu sử dụng phương pháp chia để trị.

arr = [423,432,3,4,234,452,45,43,43,5,34,534,5,34,5,34]
K = 5

def find_(arr,k):
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return 1 if arr[0] == K else 0
    mid = len(arr) // 2
    left_count = find_(arr[:mid], K)
    right_count = find_(arr[mid:], K)
    return left_count + right_count
print(find_(arr,K))