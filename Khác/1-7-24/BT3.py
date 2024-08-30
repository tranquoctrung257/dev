# nhập số nguyên num1 và num2 rồi thực hiện phép tính + - * / // ** %

num1 = int(input("nhập vào số nguyên num1: "))
num2 = int(input("nhập vào số nguyên num2: "))

print(num1,"+",num2,"=",num1+num2)
print(num1,"-",num2,"=",num1-num2)
print(num1,"*",num2,"=",num1*num2)
print(num1,"/",num2,"=",num1/num2)
print(num1,"//",num2,"=",num1//num2)
print(num1,"*",num2,"=",num1*num2)
print(num1,"**",num2,"=",num1+num2)
print(num1,"%",num2,"=",num1%num2)


# so sánh các giá trị sau
print(ord("a"))
print(ord("b"))
print("a" > "b") # False
print(3.0 > 3) # False
print("" <= " ")
print(.5 < 1) # False

# tính các toán tử sau
print(0 and 1) # 0 vì 0 là False nên trả về giá trị đầu tiên
print("" or None) # None
print(3 and 4 or 0) # 4
print(not None) # True
print(not 0 ) # True

# nhập số nguyên n từ bàn phím rồi cộng n cho 10 , tiếp theo nhân n cho 3, và trừ n cho 9
n = int(input("nhập số nguyên n: "))
n += 10
n *= 3
n -= 9
print(f"n = {n}")