# Bài 5. Cho trước dãy số A = A[0], A[1], ...., A[n - 1]. Cặp phần tử (A[i], A[j]) được gọi là nghịch đảo nếu i < j nhưng A[i] > A[j]. Viết chương trình đếm số các cặp phần tử nghịch đảo của dãy A
# a) Viết chương trình không đệ quy.


def dem_nghich_dao(A):
    count = 0  
    n = len(A) 
    
    for i in range(n):
        for j in range(i + 1, n):
            if A[i] > A[j]:
                count += 1  
    
    return count

A = [2, 4, 1, 3, 5]
so_cac_cap_nghich_dao = dem_nghich_dao(A)
print(f"Số cặp nghịch đảo trong dãy A là: {so_cac_cap_nghich_dao}")