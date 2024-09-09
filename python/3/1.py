s = input()

for i in s:
    if (i >= chr(65) and i <= chr(90)) or (i >= chr(97) and i <= chr(122)):
        print(i,end='')

