# 1. Nhập vào từ bàn phím hai số thực number1, number2. Hãy in ra tổng, hiệu, tích, thương, chia nguyên, chia lấy dư, lũy thừa của hai số đó

number1 = float(input("nhập number1: "))
number2 = float(input("nhập number2: "))

print(f"{number1} + {number2} = ",number1+number2)
print(f"{number1} - {number2} = ",number1-number2)
print(f"{number1} * {number2} = ",number1*number2)
print(f"{number1} / {number2} = ",number1/number2)
print(f"{number1} // {number2} = ",number1//number2)
print(f"{number1} % {number2} = ",number1%number2)
print(f"{number1} ** {number2} = ",number1**number2)


# 2. Dự đoán kết quả của các biểu thức so sánh sau:
# + 'a' > 'b' False  97 > 98 False
print(ord("a"))
print(ord("b"))
# + 3.0 > 3 False
# + '' <= ' ' True
# + .5 > 1 False


# 3. Dự đoán kết quả của các biểu thức logic sau:
# + 0 and 1 ==> 0
# + '' or None ==> ''
# + 3 and 4 or 0 ==> 4
# + 'a' or '1' ==> "a"
# + not None ==> True
# + not 0 ==> True



# 4. Nhập vào số nguyên n. Hãy thực hiện các công việc sau:
# + tăng n lên 10 đơn vị
# + gấp 3 lần n
# + giảm n đi 9 đơn vị
# - Cuối cùng in ra n

n = int(input("nhập số nguyên n: "))
n+=10
n*=3
n-=9
print("n = "+str(n))
print(f"n = {n}") 
print("n = {}".format(n))