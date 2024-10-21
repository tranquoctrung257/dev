def tim_hoan_hao(N):
    for num in range(2, N):
        tong_uoc = 0
        for i in range(1, num):
            if num % i == 0:
                tong_uoc += i
        if tong_uoc == num:
            print(num)


N = int(input("Nhập một số nguyên dương N: "))
print(f"Các số hoàn hảo nhỏ hơn {N} là:")
tim_hoan_hao(N)