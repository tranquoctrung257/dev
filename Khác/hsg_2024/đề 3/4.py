# Bài 4. Hãy thiết lập thuật toán và chương trình tính luỹ thừa an với a là số bất kì khác 0, n là số nguyên không âm (dùng đệ quy hoặc chia để trị)

# chia để trị

def n(a,n):
    if n == 0:
        return 1
    half = pow(a,n//2)
    if n % 2== 0:
        return half * half
    else:
        return a * half * half
    

print(n(5,5))