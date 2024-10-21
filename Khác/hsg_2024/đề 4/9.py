# Bài 9. Viết chương trình sinh tất cả các số hex (hệ đếm 16) có 3 chỉ số 

for i in range(0, 4096):
    
    hex_number = format(i, '03X')  
    # format(i, '03X'): Chuyển số i thành hệ hex:
    # 03: Đảm bảo luôn có 3 chữ số, thêm số 0 ở đầu nếu cần.
    # X: Chuyển đổi số thành dạng hệ 16 với chữ in hoa (A-F).
    print(hex_number)