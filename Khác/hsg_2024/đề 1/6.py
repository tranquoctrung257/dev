a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def s(lst,index = 0):
    if index == len(lst) :
        return
    print(lst[index],end=" ")
    s(a,index+1)
a.reverse()
s(a)