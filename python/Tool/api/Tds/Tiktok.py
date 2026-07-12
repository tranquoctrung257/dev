from curl_cffi import requests
import time
import os
id_nick = "minh.bo92"
token_tds = "TDS0nIxEjclZXZzJiOiIXZ2V2ciwiI2MDdhhmbo5WQiojIyV2c1Jye"

def cau_hinh(id_nick,token_tds):
    link = f"https://traodoisub.com/api/?fields=tiktok_run&id={id_nick}&access_token={token_tds}"
    try:
        return requests.get(link).json()
    except:
        return "lỗi không xác định"
    
def get_nv(type,token):
    # type Bao gồm: tiktok_like, tiktok_follow, tiktok_comment
    link = f"https://traodoisub.com/api/?fields={type}&access_token={token}"
    try:
        return requests.get(link).json()
    except:
        pass

def gui_nv(type_nv,id_job,token):
    # type Bao gồm: TIKTOK_LIKE_CACHE, TIKTOK_FOLLOW_CACHE
    link = f"https://traodoisub.com/api/coin/?type={type_nv}&id={id_job}&access_token={token}"
    try:
        return requests.get(link).json()
    except:
        pass

def get_xu(type,id_job,token):
    link = f"https://traodoisub.com/api/coin/?type={type}&id={id_job}&access_token={token}"
    try:
        return requests.get(link).json()
    except:
        pass  

# print(get_nv("tiktok_follow",token_tds))
# print(cau_hinh("vuanhngoc6264",token))
# print(gui_nv("TIKTOK_FOLLOW_CACHE","7536964299123754002_YGZZJBRP1OU6CHHJGXU6",token))


def main():
    for values in get_nv("tiktok_follow",token_tds)["data"]:
        os.system(f"adb shell am start -a android.intent.action.VIEW -d {values['link']}")
        time.sleep(4)
        print(gui_nv(type_nv="TIKTOK_FOLLOW_CACHE",id_job=values["id"],token=token_tds))
# main()
print(get_xu("TIKTOK_FOLLOW","TIKTOK_FOLLOW_API",token_tds))

