# range(start,stop,step)
for _ in range(5):
    print("hello world!")

print(list(range(10,0,-1)))

for i in range(1,21):
    if i % 2 == 0:
        print(i)

# while luôn chay khi đk so sánh là True và thoát vòng lặp khi là False

s = input("> ")
while s != "q":
    print("hello")
    s = input("> ")

for i in range(5):
    for j in range(3):
        print(i,j,sep="-")

# break: thoát hoàn toàn ra khỏi vòng lặp chứa nó
# continue: bỏ qua những câu lệnh bên dưới nó và chuyển sang 1 vùng lăp mới
        
for i in range(21):
    if i > 5:
        break
    print(i,sep=" _ ")

for i in range(21):
    if i % 2 == 0:
        continue
    print(i,sep=" _ ")