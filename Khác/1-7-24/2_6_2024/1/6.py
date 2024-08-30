# có thể kiểm tra chẵn lẻ bằng &
print(3 & 1)
print(5 & 1)
print(2 & 1)
print(6 & 1)
n = 6
if (n & 1) == 0:
    print("chẵn")
else:
    print("lẻ")
##
a = 0
b = 3
c = 100
print(b / 2 * a)
# print(b/(2*a)) lỗi vì không thể nhân 2 với 0

# range(start,stop,step)
for i in range(4):
    print(i, end="\t")

lst = [1, 2, 3, 4]
for x in lst:
    print(x)

dict.fromkeys(lst, "a")

# berak thoát hoàn toàn ra khỏi vòng lặp
# continue bỏ qua lần lặp hiện tại và thực hiện lần lặp mới

for i in range(20):
    if i < 5:
        continue
    print(i, end=" ")

for j in range(20):
    if j == 5:
        break
    print(j, end=" ")
# while lặp lại số lần không biết trước
# while True:
#     print("hello ")

# for else
# số nguyên tố
n = 6
for i in range(2, int(n ** 0.5)+1):
    if n % i == 0:
        print("no")
        break
else:
    print("y")

##
n = int(int(input("n = ")))
for x in range(1,21):
    print(f"{n} x {x} = {n*x} " )

# bảng cửu chương từ 1 đến 100
for i in range(1,101):
    for j in range(1,11):
        print(i*j,end=" ")
    print()
##
# kiểm tra số chẵn
n = 100
for num in range(2,n+1,2):
    print(num,end=" ")

# kiểm tra số từ và số chữ
##
n = input("nhập vào kí tự: ")
print(len(n.split()))
count = 0
for char in n:
    if char != " ":
        count+=1
print(count)

## đảo ngược chuỗi vừa nhập vào
n = input("> ")
s = ("")
for char in str(n)[::-1]:
    s+=char
print(s)

## hoặc
n = int(input("> "))
while n > 0:
    print(n%10,end="")
    n//=10