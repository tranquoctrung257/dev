a,b = map(int,input().split())

temp = a
a = b
b = temp

print(128 * a + 97 * b + 1000)