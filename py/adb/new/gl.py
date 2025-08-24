import requests,time

LIST_TK = []
object_id = []
id_Tk = []
unique_username = []
nickName = []
def headers(authorization):
    headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'vi,en;q=0.9,vi-VN;q=0.8',
            'authorization': authorization,
            'cache-control': 'no-cache',
            'content-type': 'application/json;charset=utf-8',
            'origin': 'https://app.golike.net',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://app.golike.net/',
            'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            't': 'VFZSamVVNXFSWGhPYW1jeFQwRTlQUT09',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
        }
    return headers
def getJob(account_id,headers):
    headers = headers
    data = {
        'account_id': str(account_id),
        'data': 'null',
    }
    
    response = requests.get(f'https://gateway.golike.net/api/advertising/publishers/tiktok/jobs?account_id={str(account_id)}&data=null', data=data, headers=headers).json()
    object_id.append(response["data"]["object_id"])
    try:
        return response["data"]["type"],response["data"]["id"],response["data"]["link"]
    except:
        print(response)

# def complete_job(account_id,headers,ads_id):
#     headers = headers
#     json_data = {
#     'ads_id': str(ads_id),
#     'account_id': str(account_id),
#     'async': True,
#     'data': None}

#     response = requests.post(
#         'https://gateway.golike.net/api/advertising/publishers/tiktok/complete-jobs',
#         headers=headers,
#         json=json_data,
#     )
#     # if "'status': 400" in response.text
#     return response.json()

def skip_job(ads_id,object_id,account_id):
    json_data = {
    'ads_id': ads_id,
    'object_id': object_id,
    'account_id': account_id,
    'type': 'follow',
    }

    response = requests.post(
        'https://gateway.golike.net/api/advertising/publishers/tiktok/skip-jobs',
        headers=headers,
        json=json_data,
    )
def get_acc(headers):
    headers = headers
    response = requests.get('https://gateway.golike.net/api/tiktok-account', headers=headers).json()["data"]

    for i in response:
        LIST_TK.append([i['id'],i['unique_username'],i["nickname"]])


def main():
    with open("auth.txt","r",encoding="utf8") as f:
        auth = f.read().strip()
    Headers = headers(authorization=auth)
    get_acc(headers=Headers)
    
    for i in range(len(LIST_TK)):
        acc = LIST_TK[i] 
        id = acc[0]
        userN = acc[1]
        nickN = acc[-1]
        id_Tk.append(id)
        unique_username.append(userN)
        nickName.append(nickN)
        print(f"{i+1}: | id: {id} |{userN}:{nickN}")
    chon = int(input("chọn acc chạy: "))-1
    id_acc = id_Tk[chon]
    job = getJob(account_id=id_acc,headers=Headers)
    

    # if "status': 200" in Job:
    #     print(Job)
    # elif "Hệ thống kiểm tra bạn chưa thực hiện thao tác follow !" in Job:
    #     print("XXXX")
    #     print(Job)
# # print(LIST_TK)
# print(s)
# print(object_id)
main()