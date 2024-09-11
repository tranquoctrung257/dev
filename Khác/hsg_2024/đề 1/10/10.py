with open("chieucao.inp",encoding="utf8") as file:
    data = file.readlines()
    

hoc_sinh = []
for line in data:
    try:
        name, height = line.rsplit(' ', 1)  
        height = float(height)  
        hoc_sinh.append((name,height))
    except Exception as e:
        print(e)
def lay_chieu_cao(hs):
    return hs[1]



thap_nhat = min(hoc_sinh, key=lay_chieu_cao)
cao_nhat = max(hoc_sinh, key=lay_chieu_cao)

# file out 
fi = open("ketqua.out","w",encoding="utf8")

print(f"{thap_nhat[0]} {thap_nhat[-1]:.2f}",file=fi)
print(f"{cao_nhat[0]} {cao_nhat[-1]:.2f}",file=fi)

fi.close()
