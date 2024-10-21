# Bài 8. Viết chương trình sinh tất cả các xâu (hoặc dãy) bao gồm n kí tự dạng “R”, “G” và "B"

def randoms(n,string=""):
    if len(string) == n:
        print(string)
        return
    for char in ["R","G","B"]:
        randoms(n,string+char)

n = int(input("Nhập độ dài của xâu (n): "))

randoms(n)