import requests
def info(token):
    url = f"https://traodoisub.com/api/?fields=profile&access_token={token}"
    req = requests.get(url)
    return req.json()

token_tds = "TDS9JyNyVmdlNnI6IiclZXZzJCLicDMyUjM0FHViojIyV2c1Jye"

user_Tds = info(token_tds)['data']["user"]
xu = info(token_tds)['data']["xu"]
xudie = info(token_tds)['data']["xudie"]

print(f"Tài khoản {user_Tds} | {xu} xu | {xudie} Xu Die")

# cách 2 dùng cokies

def info_ck(cookies):

    headers = {
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36',
        "cookie":cookies
    }
    response = requests.get('https://traodoisub.com/scr/user.php', headers=headers).json()
    return response

ck = input("nhập cokies: ")

print(info_ck(ck))