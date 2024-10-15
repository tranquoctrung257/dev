
# Bài 2. Viết chương trình giải bài toán Tháp Hà Nội nhưng với tên các cọc là A, B, C

def thap_ha_noi(n, cot_nguon, cot_trung_gian, cot_dich):
    if n == 1:
        print(f"Chuyển đĩa 1 từ cọc {cot_nguon} sang cọc {cot_dich}")
        return
    thap_ha_noi(n - 1, cot_nguon, cot_dich, cot_trung_gian)
    
    print(f"Chuyển đĩa {n} từ cọc {cot_nguon} sang cọc {cot_dich}")
    
    thap_ha_noi(n - 1, cot_trung_gian, cot_nguon, cot_dich)

so_dia = 3 
thap_ha_noi(so_dia, 'A', 'B', 'C')
