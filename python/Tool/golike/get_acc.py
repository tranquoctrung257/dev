from curl_cffi import requests

def headers_acc(athu):
    headers= {
        'accept': 'application/json, text/plain, */*',
        "authorization":athu,
        'accept-language': 'vi,en;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/json;charset=utf-8',
        'origin': 'https://app.golike.net',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        't': 'VFZSak1VNVVSVFJOUkUwd1RtYzlQUT09',
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
    }
    return headers

authorization = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC9nYXRld2F5LmdvbGlrZS5uZXRcL2FwaVwvbG9naW4iLCJpYXQiOjE3NTQ4MDUzNjksImV4cCI6MTc4NjM0MTM2OSwibmJmIjoxNzU0ODA1MzY5LCJqdGkiOiJlaUdYTDc2RFlMSVdqVlNDIiwic3ViIjoyMTAyMDY4LCJwcnYiOiJiOTEyNzk5NzhmMTFhYTdiYzU2NzA0ODdmZmYwMWUyMjgyNTNmZTQ4In0.5_6YBqngJnBS9fnwMx2Qctv_j_sXFWOd-B1Ij4YntRo'
def acc_tiktok():
    res = requests.get("https://gateway.golike.net/api/tiktok-account",headers=headers_acc(authorization),impersonate="safari18_0_ios").json()
    for acc in range(len(res["data"])):
        list_acc = []
        AccID = res["data"][acc]['id']
        UserID = res["data"][acc]['user_id']
        NickName = res["data"][acc]["nickname"]
        unique_username = res["data"][acc]["unique_username"]
        # print(unique_username)
        list_acc.extend([acc,AccID,unique_username])
        print(list_acc)

acc_tiktok()



