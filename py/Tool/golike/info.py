from curl_cffi import requests
authorization = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC9nYXRld2F5LmdvbGlrZS5uZXRcL2FwaVwvbG9naW4iLCJpYXQiOjE3NTQ4MDUzNjksImV4cCI6MTc4NjM0MTM2OSwibmJmIjoxNzU0ODA1MzY5LCJqdGkiOiJlaUdYTDc2RFlMSVdqVlNDIiwic3ViIjoyMTAyMDY4LCJwcnYiOiJiOTEyNzk5NzhmMTFhYTdiYzU2NzA0ODdmZmYwMWUyMjgyNTNmZTQ4In0.5_6YBqngJnBS9fnwMx2Qctv_j_sXFWOd-B1Ij4YntRo'
def me(athu):
    headers = {
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

    response = requests.get('https://gateway.golike.net/api/users/me', headers=headers,impersonate="safari_ios",)
    try:
        if response.json()["status"] == 200:
            return response.json()
    except:
        return "lỗi không xác định"



data_id = me(authorization)["data"]["id"]
data_name = me(authorization)["data"]["name"]
data_email = me(authorization)["data"]["email"]
data_username = me(authorization)["data"]["username"]
data_coin = me(authorization)["data"]["coin"]
data_phone_number = me(authorization)["data"]["phone_number"]
print(data_id)
""" 
print("ID nick: "data_id)
print(data_name)
print(data_email)
print(data_username)
print(data_coin)
print(data_phone_number)
 """

def report(auth):
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi,en;q=0.9',
        'authorization': auth,
        'cache-control': 'no-cache',
        'content-type': 'application/json;charset=utf-8',
        'origin': 'https://app.golike.net',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        't': 'VFZSak1VNVVTVEpOZW1kNlRWRTlQUT09',
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
    }

    response = requests.get('https://gateway.golike.net/api/statistics/report', headers=headers,impersonate="safari260_ios")
    return response.json()

