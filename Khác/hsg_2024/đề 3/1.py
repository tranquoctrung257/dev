# Bài 1. Viết chương trình hoàn chỉnh nhập một dãy số đơn điệu tăng từ bàn phím, các số cách nhau bởi dấu cách. Sau đó, nhập số K bất kì từ bàn phím và thực hiện việc tìm kiếm số K trong dãy trên. Nếu tìm thấy thì trả lại chỉ số của phần tử có giá trị K, ngược lại trả về – 1

arr = list(map(int,input().split()))

K = int(input())

for i in range(len(arr)):
    if K == arr[i]:
        print(K)
        break
else:print(-1)