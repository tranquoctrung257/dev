# ## 4. Bài tập
# 1. Đếm số chẵn và lẻ trong đoạn [0, 1000] theo 2 cách: thông thường và list comprehension

chan = 0
le = 0

for i in range(1,1001):
    if i % 2 == 0:
        chan+=1
    else:le+=1
print(chan)
print(le)

lst = list(range(1,1001))

chan = [1  for i in lst if i % 2 == 0]
le = [1  for i in lst if i % 2 != 0]

print(sum(chan))
print(sum(le))