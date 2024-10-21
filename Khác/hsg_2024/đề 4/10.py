# Bài 10. Viết chương trình sinh xâu nhị phân thực sự có độ dài n, tức là kết quả in ra phải là các xâu kí tự chứ không phải là danh sách (list) như trong các chương trình trên

def sinh_nhi_phan(n, str_=""):
    if n == 0:
        print(str_)
    else:
        sinh_nhi_phan(n-1, str_ + "0")
        sinh_nhi_phan(n-1, str_ + "1")


n = int(input("Nhập độ dài xâu nhị phân n: "))
sinh_nhi_phan(n)