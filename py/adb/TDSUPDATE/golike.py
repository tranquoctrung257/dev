import requests,time

def gl(auth):
    url = "https://gateway.golike.net/api/statistics/report"
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "authorization": f"{auth}",
        "cache-control": "no-cache",
        "content-type": "application/json;charset=utf-8",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "t": "VFZSamVFOVVUVE5PZWtVelRtYzlQUT09",
        "Referer": "https://app.golike.net/",
        "Referrer-Policy": "strict-origin-when-cross-origin"
    }
    p = requests.get(url=url,headers=headers).json()
    xu_da_duyet = p['current_coin']
    xu_chua_duyet_tiktok = p['tiktok']['pending_coin']
    xu_chua_duyet_facebook = p['facebook']['pending_coin']
    xu_chua_duyet_instagram = p['instagram']['pending_coin']
    xu_chua_duyet_youtube = p['youtube']['pending_coin']
    xu_chua_duyet_twitter = p['twitter']['pending_coin']
    xu_chua_duyet_shopee = p['shopee']['pending_coin']
    xu_chua_duyet_lazada = p['lazada']['pending_coin']
    xu_chua_duyet_review = p['review']['pending_coin']
    xu_chua_duyet_traffic = p['traffic']['pending_coin']
    xu_chua_duyet_threads = p['threads']['pending_coin']
    xu_chua_duyet_linkedin = p['linkedin']['pending_coin']

    tong = xu_da_duyet + xu_chua_duyet_tiktok + xu_chua_duyet_facebook + xu_chua_duyet_instagram + xu_chua_duyet_youtube + xu_chua_duyet_twitter + xu_chua_duyet_shopee + xu_chua_duyet_lazada + xu_chua_duyet_review + xu_chua_duyet_traffic + xu_chua_duyet_threads + xu_chua_duyet_linkedin

    # thông tin tk
    url = "https://gateway.golike.net/api/users/me"
    p1 = requests.get(url=url,headers=headers).json()
    return p1['data']['username'],tong
def add_tk(auth):
    with open('tkgl.txt','a') as file:
        file.write(f'|{auth}')
    return 0


with open(file='tkgl.txt') as file:
    fi = (file.read().split("|"))

sum = 0
for i in fi:
    print(gl(i))
    sum+=int(gl(i)[-1])
print(sum)