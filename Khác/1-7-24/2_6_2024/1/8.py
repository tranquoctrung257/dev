# globals

friends = []
def add_friend(name):
    friends.append(name)
    print(friends)
add_friend("john")

# có thể bị lỗi do tham chiếu
def func(lst):
    lst.append("1")

l = []
func(l)
print(l)

# các khác phuc
def func1(lst):
    lst.append("1")

l1 = []
k = l1[:]
func(k)
print(l1)

b = [2,4,5,6,7]
a = b
a.append(1)
print(b)

# để truyền vào nhiều tham số
def add(*args):
    print(sum(args))
add(1,4,5,6,7,8,9,6,7)

def add1(**kwargs):
    print(type(kwargs))
    print(kwargs)
add1(a = 10,b = 100,d = 190234)

# 55p