
# Hướng Dẫn Code Tool Từ A-Z - Livestream #1

'''
cơ bản

# biến ok
# toán tử ok  
print("D"+"E")

# if else 
# if đk 1 đúng:
    # code (đk đúng)
# elif đk 2 đúng:
    # code (đk đúng)
# else: 
    # code (đk còn lại nếu 2 đk trên ko đúng)

# vòng lặp (for,while)

for i in range(10):
    print(i,end=" ")
# chạy từ 0 đến 10

lst = ["sv1","sv2","sv3"]
print()
for i in lst:
    print(i)

'''

# làm tool
from colorama import Fore
# from colorama import * #* đây là lấy tất cả các hư viện nhỏ từ thư viện lớn. 

import colorama 
# nếu import như này thì phải gọi dài dòng giống như này
colorama.Fore.BLACK

# còn nếu như đầu thì 
Fore.BLACK

# khi sử dụng thư viện nào đó thì phải import nó vào
import requests
# nếu chưa cài thì vào cmd gõ pip install requests


# sử dụng công cụ https://curlconverter.com/ để copy nhanh hơn requests
# chuôt phải vào api cần làm rồi vào copy rồi tiếp copy as curl bash

# ví dụ giờ sẽ làm tool trao đổi sub ig sương sương 
token_tds = "TDS9JyNyVmdlNnI6IiclZXZzJCLicDMyUjM0FHViojIyV2c1Jye"
def dat_cau_hinh_nick(token,id_ig):
    req = requests.get(f"https://traodoisub.com/api/?fields=instagram_run&id={id_ig}&access_token={token}").text
    return req

# print(dat_cau_hinh_nick(token=token_tds,id_ig="anhhiu7329"))

def get_nv_ig(token,type):
    url = f"https://traodoisub.com/api/?fields={type}&access_token={token}"
    req = requests.get(url).json()
    return(req)

ds = get_nv_ig(token_tds,"instagram_like")
print()
for i in range(len(ds['data'])):
    print(ds['data'][i]["id"],ds['data'][i]["link"])