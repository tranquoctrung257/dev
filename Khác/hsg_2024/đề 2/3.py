# Bài 3. Giả sử cần lưu dãy các bước chuyển của bài toán Tháp Hà Nội vào một danh sách để có thể sử dụng lại về sau. Mỗi bước chuyển dạng k: i → j sẽ được lưu trong một bộ ba số (k, i, j). Viết chương trình giải bài toán Tháp Hà Nội tổng quát Hanoi(n, i, j, k) chuyển n đĩa từ cọc i sang cọc j lấy cọc k làm trung gian với yêu cầu lưu tất cả các bước chuyển vào một danh sách (list). Như vậy, hàm Hanoi(n, i, j, k) sẽ trả về một danh sách bao gồm các bộ ba số dạng như đã mô tả ở trên.
# Gợi ý bài 3: Để giải bài toán Tháp Hà Nội và lưu các bước chuyển vào một danh sách, ta có thể sử dụng thuật toán đệ quy. Trong mỗi lần đệ quy, ta sẽ chuyển n-1 đĩa từ cọc ban đầu sang cọc trung gian, sau đó chuyển đĩa lớn nhất từ cọc ban đầu sang cọc đích và cuối cùng chuyển n-1 đĩa từ cọc trung gian sang cọc đích.


def thap_ha_noi(n, i, j, k):
    arr = []

    if n == 1:
        arr.append((i, j)) 
    else:
        arr += thap_ha_noi(n - 1, i, k, j)
        arr.append((i, j))
        arr += thap_ha_noi(n - 1, k, j, i)
    
    return arr

so_dia = 3
cac_buoc = thap_ha_noi(so_dia, 'A', 'C', 'B')
print(cac_buoc)