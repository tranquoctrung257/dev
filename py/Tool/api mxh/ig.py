from curl_cffi import requests
import re


def get_headers(cookies):
    csrftoken = cookies.split("csrftoken=")[1].split(";")[0]
    headers = {
        'accept': '*/*',
        'accept-language': 'vi,en-US;q=0.9,en;q=0.8,pl;q=0.7',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://www.instagram.com',
        'priority': 'u=1, i',
        'referer': 'https://www.instagram.com/ttartisanofficial/',
        'sec-ch-prefers-color-scheme': 'dark',
        'sec-ch-ua': '"Not;A=Brand";v="99", "Microsoft Edge";v="139", "Chromium";v="139"',
        'sec-ch-ua-full-version-list': '"Not;A=Brand";v="99.0.0.0", "Microsoft Edge";v="139.0.3405.111", "Chromium";v="139.0.7258.139"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"19.0.0"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36 Edg/139.0.0.0',
        'x-asbd-id': '359341',
        'x-bloks-version-id': '91b4f3c0d432ef4a2d4f3ad30ae9fc795041a95a6c6b9a2a8f230816c480d891',
        'x-csrftoken': csrftoken,
        'x-fb-friendly-name': 'usePolarisFollowMutation',
        'x-fb-lsd': '1FjmcBMkfv7-sMAcVdCZWH',
        'x-ig-app-id': '936619743392459',
        'x-root-field-name': 'xdt_create_friendship',
        'cookie': ck,
    }
    return headers

def get_data(headers):
    res = requests.get("https://www.instagram.com/",headers=headers).text
    avID = re.findall('"actorID":".*?"',res)[0].split('"actorID":"')[-1].split('"')[0]
    dtsgID = re.findall('dtsg":.*?,',res)[0].split(':"')[1].split('",')[0]
    return avID,dtsgID


def follow(headers,avID,dtsgID,targetID):

    data = {
        'av': avID,
        'fb_dtsg':dtsgID,
        'fb_api_caller_class': 'RelayModern',
        'fb_api_req_friendly_name': 'usePolarisFollowMutation',
        'variables': '{"target_user_id":"'+targetID+'","container_module":"profile","nav_chain":"PolarisProfilePostsTabRoot:profilePage:1:via_cold_start"}',
        'server_timestamps': 'true',
        'doc_id': '9740159112729312',
    }

    response = requests.post('https://www.instagram.com/graphql/query',  headers=headers, data=data).json()
    if response['data']['xdt_create_friendship']["friendship_status"]['following'] == True and response["status"] == "ok" and response['extensions']['is_final'] == True:
        return True
    else:return False

# chưa test ổn
def like(headers,avID,dtsgID,targetID):
    data = {
    'av': avID,
    'fb_dtsg': dtsgID,
    'fb_api_caller_class': 'RelayModern',
    'fb_api_req_friendly_name': 'usePolarisLikeMediaLikeMutation',
    'variables': '{"media_id":"'+targetID+'","container_module":"feed_timeline"}',
    'server_timestamps': 'true',
    'doc_id': '23951234354462179',
    }

    response = requests.post('https://www.instagram.com/graphql/query', headers=headers, data=data).json()
    return response


ck = 'datr=_nitaIqGOT3Y9ssDfrNdiHEB; ig_did=B5F4A28D-764C-49E0-8053-5A2723BA2A84; mid=aK14_gALAAE5eudCy5rNAx3k3OF9; ig_nrcb=1; csrftoken=k1Ux7fymOPNpCbQJ6wfiR2RT7FOStlMY; ds_user_id=76848411135; ps_l=1; ps_n=1; sessionid=76848411135%3AOeeFzSxxY9EUVq%3A23%3AAYcX2ZsHyRwlzbsCuEyRga0FsidHMKvH8gCCC3FHMA; wd=1233x957; rur="CCO\05476848411135\0541787836951:01fe544f16fdda372cc1b2a06a0f346100dd6bb658eb37d5559b3f90b7572b289b4148e4"'

def get_target_id(url,hd):
    return requests.get(url,headers=hd).text.split('"target_id":"')[2].split('"')[0]
hd = get_headers(ck)
data = get_data(hd)
fl = follow(hd,data[0],data[1],get_target_id("https://www.instagram.com/cafe_.206/#",hd))
print(fl)

