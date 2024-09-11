

def pprint_number(n):
    if n == 100:
        print(100)
    else:
        print(n,sep=" ",end=" ")
        pprint_number(n+1)
pprint_number(1)