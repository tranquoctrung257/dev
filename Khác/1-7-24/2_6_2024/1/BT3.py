# 1. Nhập vào từ bàn phím hai số thực number1, number2. Hãy in ra tổng, hiệu, tích, thương, chia nguyên, chia lấy dư, lũy thừa của hai số đó

num1 = int(input("nhập vào number1"))
num2 = int(input("nhập vào number2"))
print(f"num1 + num2 = {num1+num2}")
print(f"num1 - num2 = {num1-num2}")
print(f"num1 * num2 = {num1*num2}")
print(f"num1 / num2 = {num1/num2}")
print(f"num1 // num2 = {num1//num2}")
print(f"num1 % num2 = {num1%num2}")
print(f"num1 ** num2 = {num1%num2}")

# 2. Dự đoán kết quả của các biểu thức so sánh sau:
# + 'a' > 'b'==> False
# + 3.0 > 3 ==> False
# + '' <= ' ' ==> True
# + .5 > 1 ==> False
# 3. Dự đoán kết quả của các biểu thức logic sau:
# + 0 and 1 ==> 0
# + '' or None ==> None
# + 3 and 4 or 0   ==> 4
# + 'a' or '1' ==> "a"
# + not None ==> True
# + not 0 ==> False
# 4. Nhập vào số nguyên n. Hãy thực hiện các công việc sau:
# + tăng n lên 10 đơn vị
# + gấp 3 lần n
# + giảm n đi 9 đơn vị
# - Cuối cùng in ra n

n = int(input("nhập vào số nguyên n: "))
n+=10
n*=3
n-=9
print(n)

