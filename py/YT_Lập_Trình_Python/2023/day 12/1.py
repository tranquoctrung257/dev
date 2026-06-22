def removes():
    global lst 
    lst = [x for x in lst if x != "a"]

lst = ["a","b","a","z"]
removes()
print(lst)