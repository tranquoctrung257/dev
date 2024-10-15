# Bài 7. Cho một dãy số nguyên được sắp xếp theo thứ tự tăng dần, hãy tìm một vị trí thứ i trong dãy sao cho phần tử thứ i có giá trị bằng i.

arr = [1,2,3,4,5,6,7,8,9,10]
i_ = 5
for i in range(len(arr)):
    if arr[i] == i_:
        print(True)
        break
    else:print(False);break
