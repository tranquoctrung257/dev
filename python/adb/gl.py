
import requests,sys,os,time,cv2
import numpy as np
from datetime import date
from datetime import datetime
xanh= "\033[1;96m"
xlacay ="\033[0;32m"
den="\033[1;90m"
do="\033[1;91m"
luc="\033[1;92m"
vang="\033[1;93m"
xduong="\033[1;94m"
hong="\033[1;95m"
trang="\033[1;97m"
vang="\033[1;93m"
syan="\033[1;36m"

class ADB:
    def __init__(self,handle):
        self.handle = handle
    def screen_capture(self,name):
        os.system(f"adb -s {self.handle} exec-out screencap -p > {name}.png ")
    def click(self,x,y):
        os.system(f"adb -s {self.handle} shell input tap {x} {y}")
    def find(self,img='',template_pic_name=False,threshold=0.99):
        if template_pic_name == False:
            self.screen_capture(self.handle)
            template_pic_name = self.handle+'.png'
        else:
            self.screen_capture(template_pic_name)
        img = cv2.imread(img)
        img2 = cv2.imread(template_pic_name)
        result = cv2.matchTemplate(img,img2,cv2.TM_CCOEFF_NORMED)
        loc = np.where(result >= threshold)
        test_data = list(zip(*loc[::-1]))
        return test_data

def cc(title):
    for i in title:
        print(i,end='')
        time.sleep(0.02)
def login(author,t):
    head_login = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "Authorization": author,
        "Content-Type": "application/json;charset=utf-8",
        "Origin": "https://app.golike.net",
        "Referer": "https://app.golike.net/",
        # 'Sec-Ch-Ua':'"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
        # 'Sec-Ch-Ua-Mobile':'?0',
        # 'Sec-Ch-Ua-Platform':'"Windows"',
        # 'Sec-Fetch-Dest':'empty',
        # 'Sec-Fetch-Mode':'cors',
        # 'Sec-Fetch-Site':'same-site',
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
        "T": t
    }
    try:
        account = requests.get("https://sv5.golike.net/api/tiktok-account",headers=head_login).json()
        if (account['status'] == 200):
            print(xlacay+"LOGIN THÀNH CÔNG                              ")
            f = open("taikhoan.txt","w+")
            f.write(author+"|"+t)
            f.close()
            time.sleep(1)
            os.system('clear')
            return account
        else:
            print(do+"LOGIN THẤT BẠI VUI LÒNG XEM LẠI             ")
            quit()
    except:
        print(do+"GOLIKE ĐANG LỖI, VUI LÒNG QUAY LẠI SAU!!!           ")

os.system("clear")
dau="\033[1;31m[\033[1;37m×.×\033[1;31m] \033[1;37m➩"
def banner():
        os.system("cls" if os.name == "nt" else "clear")
        banner = f'''
{do}██╗░░██╗██╗███████╗██╗░░░██╗ {luc}████████╗░█████╗░░█████╗░██╗░░░░░
{luc}██║░░██║██║██╔════╝██║░░░██║ {trang}╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░
{do}███████║██║█████╗░░██║░░░██║ {luc}░░░██║░░░██║░░██║██║░░██║██║░░░░░
{luc}██╔══██║██║██╔══╝░░██║░░░██║ {trang}░░░██║░░░██║░░██║██║░░██║██║░░░░░
{do}██║░░██║██║███████╗╚██████╔╝ {luc}░░░██║░░░╚█████╔╝╚█████╔╝███████╗
{luc}╚═╝░░╚═╝╚═╝╚══════╝░╚═════╝░ {trang}░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝
                    \033[1;33mTOOL GOLIKE V3 DELAY 0S
                                      \033[1;36mCopyright By: HIẾU_TOOL
\033[1;35m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = \n'''
        for i in banner:
          sys.stdout.write(i)
          sys.stdout.flush()
banner()

print("\n")
print(syan+"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print(trang+"["+vang+"1"+trang+"]. Đăng nhập tài khoản GOLIKE lần trước   ")
print(trang+"["+vang+"2"+trang+"]. Đăng nhập tài khoản GOLIKE mới         ")
print(syan+"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
select = int(input(vang+"Nhập :  "+trang))
banner()
if (select == 2):
    authorization = input(syan+"Nhập Authorization: "+trang)
    t = input(syan+"Nhập T: "+trang)
    account = login(authorization,t)
    head_login = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "Authorization": authorization,
        "Content-Type": "application/json;charset=utf-8",
        "Origin": "https://app.golike.net",
        "Referer": "https://app.golike.net/",
        'Sec-Ch-Ua':'"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
        'Sec-Ch-Ua-Mobile':'?0',
        'Sec-Ch-Ua-Platform':'"Windows"',
        'Sec-Fetch-Dest':'empty',
        'Sec-Fetch-Mode':'cors',
        'Sec-Fetch-Site':'same-site',
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
        "T": t
    }
elif (select == 1):
    f = open("taikhoan.txt","r")
    tam = f.readline()
    authorization = tam.split("|")[0]
    t = tam.split("|")[1]
    head_login = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "Authorization": authorization,
        "Content-Type": "application/json;charset=utf-8",
        "Origin": "https://app.golike.net",
        "Referer": "https://app.golike.net/",
        'Sec-Ch-Ua':'"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
        'Sec-Ch-Ua-Mobile':'?0',
        'Sec-Ch-Ua-Platform':'"Windows"',
        'Sec-Fetch-Dest':'empty',
        'Sec-Fetch-Mode':'cors',
        'Sec-Fetch-Site':'same-site',
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
        "T": t
    }
    account = login(authorization,t)
banner()
listid = []
listname = []
for i in range(len(account['data'])):
    id = account['data'][i]['id']
    listid.append(id)
    user_id = account['data'][i]['user_id']
    unique_username = account['data'][i]['unique_username']
    listname.append(unique_username)
    print(xlacay+"["+do+str(i)+syan+"]"+xduong+"   =>   "+vang+"ID: "+trang+str(id)+xduong+"   =>   "+trang+unique_username+xlacay+"["+hong+str(i)+syan+"]")

stt = int(input(syan+"Chọn tài khoản để auto: "+vang))
os.system('clear')
banner()
print(syan+"NICK ĐANG CHẠY: "+trang+listname[stt]+"=> "+syan+"ID:"+trang+str(listid[stt]))
print(xlacay+"=====================================================================")
tong = 0
while True:
    time.sleep(0)
    print(syan+'ĐANG LẤY NHIỆM VỤ TIKTOK                        ',end="\r")
    while True:
        try:
            getjob = requests.get("https://sv5.golike.net/api/advertising/publishers/tiktok/jobs?account_id="+str(listid[stt])+"&data=null",headers=head_login).json()
            link = getjob['data']['link']
            break
        except:
            continue
    success = 0
    id_job = getjob['data']['id']
    type_acction = getjob['data']['type']
    object_id = getjob['data']['object_id']
    os.system(f'adb -s BH901UNSCR shell am start -a android.intent.action.VIEW -d {link}')
    # os.system('start '+link)
    for i in range(5,0,-1):
        if (type_acction == "follow"):
            print(syan+'VUI LÒNG THỰC HIỆN FOLLOW TRONG '+trang+str(i)+syan+' GIÂY                                  ',end= "\r")
        elif (type_acction == "like"):
            print(syan+'VUI lÒNG THỰC HIỆN THẢ TIM TRONG '+trang+str(i)+syan+' giây                                 ',end= "\r")
        time.sleep(1)
    for i in range(6,-1,-1):
        print()
        d = ADB('BH901UNSCR')
        time.sleep(1)
        point = d.find('fl1.png')
        try:
            d.click(point[0][0],point[0][1])
            print(point)
            print("==> Thành công")
            break
        
        except:
            os.system("adb -s BH901UNSCR shell input tap 995 924")
            break
            
    hd = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "Authorization": authorization,
        "Content-Type": "application/json;charset=UTF-8",
        "referer": "https://app.golike.net/",
        "origin": "https://app.golike.net",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
        "T": t
    }
    dt = f'{{"account_id": "{str(listid[stt])}","ads_id": "{str(id_job)}","async": true,"data": null}}'
    print(syan+"ĐANG NHẬN TIỀN                                                         ",end = "\r")
    getxu = requests.post('https://sv5.golike.net/api/advertising/publishers/tiktok/complete-jobs',data=dt,headers=hd).json()
    if (getxu['status'] != 200):
        getxu1 = requests.post('https://sv5.golike.net/api/advertising/publishers/tiktok/complete-jobs',data=dt,headers=hd).json()
        if (getxu1['status'] == 200):
            success = 1
            xu =  getxu1['data']['prices']
        else:
            success = 0
    else:
        success = 1
        xu =  getxu['data']['prices']
    if (success == 1):
        tong = tong + 1 
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        title = trang+"HIẾU-TOOL"+do+" 🍀  "+trang+current_time+do+" 🍀  "+vang+type_acction+do+" 🍀  "+vang+str(id_job)+do+" 🍀  "+trang+"+"+str(xu)+xduong+" ⇒  "+syan+"["+do+str(tong)+syan+"]              \n"
        cc(title)
    elif (success == 0):
        print(do+"JOB LỖI, BỎ QUA NHIỆM VỤ                                    ",end = "\r")
        dt1 = f'{{"account_id": "{str(listid[stt])}","ads_id": "{str(id_job)}","type": "{type_acction}","object_id": "{object_id}"}}'
        skipjob = requests.post('https://sv5.golike.net/api/advertising/publishers/tiktok/skip-jobs',data=dt1,headers=hd).json()
        if (skipjob['status'] == 200):
            print(do+"BÁO LỖI THÀNH CÔNG                                     ",end="\r")