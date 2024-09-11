def pell(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return 2 *pell(n-1) + pell(n-2)
    
print(pell(10))