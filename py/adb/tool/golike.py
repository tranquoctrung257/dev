import colorama
from colorama import Fore, Style
import requests,os,sys, time
from random import choice, randint, shuffle
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from os.path import isfile
from bs4 import BeautifulSoup
from datetime import datetime
import re,requests,os,sys
from time import sleep 
from datetime import date
import requests, random
import requests
import base64, json,os
from datetime import date
from datetime import datetime
from time import sleep,strftime
from bs4 import BeautifulSoup
from datetime import datetime
import re,requests,os,sys
from time import sleep
from datetime import date
import requests, random
import uuid, re
from pystyle import Write,Colors
from bs4 import BeautifulSoup
import socket
from datetime import datetime
import threading,base64
import os,time,re,json,random
from datetime import datetime
from time import sleep,strftime
import requests
import os, sys
import random
try:
  from faker import Faker
  from requests import session
  from colorama import Fore, Style
  import requests, random, re
  from random import randint
  import requests,pystyle
except:
  os.system("pip install faker")
  os.system("pip install requests")
  os.system("pip install colorama")
  os.system('pip install requests && pip install bs4 && pip install pystyle')
  os.system("pip install termcolor")
  print('__Vui Lòng Chạy Lại Tool__')
from time import sleep
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
    
from datetime import datetime
from time import sleep,strftime
time=datetime.now().strftime("%H:%M:%S")
import socket
from pystyle import *
#màu
luc = "\033[1;32m"
trang = "\033[1;37m"
do = "\033[1;31m"
vang = "\033[0;93m"
hong = "\033[1;35m"
xduong = "\033[1;34m"
xnhac = "\033[1;36m"
red='\u001b[31;1m'
yellow='\u001b[33;1m'
green='\u001b[32;1m'
blue='\u001b[34;1m'
tim='\033[1;35m'
xanhlam='\033[1;36m'
xam='\033[1;30m'
black='\033[1;19m'
#Đánh Dấu Bản Quyền
hhoang_tool = trang + " " + trang + "[" + do + "●" + trang + "] " + trang + "=> "
hdang = trang + " " + trang + "[" + do + "●" + trang + "] " + trang + "=> "
thanh = trang + "-------------------------------------------------------------------------"

#today nand clear
os.system('cls')
data_machine = []
today = date.today()
os.system('clear')
#daystime
now = datetime.now()
thu = now.strftime("%A")
ngay_hom_nay = now.strftime("%d")
thang_nay = now.strftime("%m")
nam_ = now.strftime("%Y")

def get_ip_from_url(url):
    response = requests.get(url)
    ip_address = socket.gethostbyname(response.text.strip())
    return ip_address
url = "http://kiemtraip.com/raw.php"
ip = get_ip_from_url(url)
a = " \033[1;97m[\033[1;31m+_+\033[1;97m] => "
def logo():
    os.system("cls" if os.name == "nt" else "clear")
    logo=f"""
\x1b[38;5;226m╔═════════════════════════════════════════════════════════════════╗
\x1b[38;5;226m║\x1b[38;5;207m██╗░░██╗██████╗░████████╗░░░░░░████████╗░█████╗░░█████╗░██╗░░░░░ \x1b[38;5;226m║
\x1b[38;5;226m║\x1b[38;5;226m██║░░██║██╔══██╗╚══██╔══╝░░░░░░╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░ \x1b[38;5;226m║
\x1b[38;5;226m║\033[38;5;99m███████║██║░░██║░░░██║░░░█████╗░░░██║░░░██║░░██║██║░░██║██║░░░░░ \x1b[38;5;226m║
\x1b[38;5;226m║\x1b[38;5;46m██╔══██║██║░░██║░░░██║░░░╚════╝░░░██║░░░██║░░██║██║░░██║██║░░░░░ \x1b[38;5;226m║
\x1b[38;5;226m║\033[38;5;51m██║░░██║██████╔╝░░░██║░░░░░░░░░░░░██║░░░╚█████╔╝╚█████╔╝███████╗ \x1b[38;5;226m║
\x1b[38;5;226m║\x1b[38;5;208m╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░░░░░░░░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝ \x1b[38;5;226m║
\x1b[38;5;226m╠═════════════════════════════════════════════════════════════════╣
\x1b[38;5;226m║\x1b[38;5;46m▶ Nhóm Zalo  : \x1b[38;5;207mhttps://zalo.me/g/bprmyn080                       \x1b[38;5;226m║
\x1b[38;5;226m║\x1b[38;5;46m▶ Website Share Tool  : \x1b[38;5;207mhttps://linkbio.co/sharetool            \x1b[38;5;226m ║
\x1b[38;5;226m╚═════════════════════════════════════════════════════════════════╝
\x1b[38;5;46m-------- \033[38;5;99mTOOL GOLIKE VIP\x1b[38;5;46m --------
  """

    print(logo)


# ======================== [ HOME TOOL ] ========================
os.system("cls" if os.name == "nt" else "clear")
logo()

def skipjob(token,user_agent,account_id,ads_id,object_id,type):
  headers = {
    'authority': 'sv5.golike.net',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'authorization': f'Bearer {token}',
    'content-type': 'application/json;charset=UTF-8',
    'origin': 'https://app.golike.net',
    'referer': 'https://app.golike.net/',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    't': 'VFZSWk5VMUVSVEZQVkdjMFRXYzlQUT09',
    'user-agent': user_agent,
}
  json_data = {
    'ads_id': ads_id,
    'object_id': object_id,
    'account_id': account_id,
    'type': type,
}
  try:
    response = requests.post('https://sv5.golike.net/api/advertising/publishers/tiktok/skip-jobs', headers=headers, json=json_data).json()
    if response['status'] == 200:
      skip=response['message']
      print(f'\033[38;5;99mđang bỏ qua job',skip)
  except:
    print("\033[38;5;51mSkip Job thất bại")

def nxu(token,account_id,user_agent,ads_id,object_id,type):
  headers = {
    'authority': 'sv5.golike.net',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'authorization': f'Bearer {token}',
    'content-type': 'application/json;charset=UTF-8',
    'origin': 'https://app.golike.net',
    'referer': 'https://app.golike.net/',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    't': 'VFZSWk5VMUVSWGxPUkZVMFRVRTlQUT09',
    'user-agent': user_agent,
}
  json_data = {
    'ads_id': ads_id,
    'account_id': account_id,
    'async': True,
    'data': None,
    
}
  while True:
    try:
      response = requests.post(
    'https://sv5.golike.net/api/advertising/publishers/tiktok/complete-jobs',
    headers=headers,
    json=json_data,
)
      sleep(5)
      x = response.json()
      if x['status'] == 200:
        if x['message'] == "Hoàn thành job thành công":
          print("\033[38;5;99m Hoàn thành job lần thứ 2 thành công")    
          break
        ms = x['message']
        prices=x['data']['prices']
        print(f"=> \033[38;5;99mBáo cáo lần 2 thành công")
        break
      if x['status'] == 400:
        headers = {
    'authority': 'sv5.golike.net',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'authorization': f'Bearer {token}',
    'content-type': 'application/json;charset=UTF-8',
    'origin': 'https://app.golike.net',
    'referer': 'https://app.golike.net/',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    't': 'VFZSWk5VMUVSWGxPUkZVMFRVRTlQUT09',
    'user-agent': user_agent,
}
        json_data = {
    'ads_id': ads_id,
    'account_id': account_id,
    'async': True,
    'data': None,
    
}
        while True:
          try:
            response = requests.post(
    'https://sv5.golike.net/api/advertising/publishers/tiktok/complete-jobs',
    headers=headers,
    json=json_data,
)
            sleep(5)
            x = response.json()
            if x['status'] == 200:
              if x['message'] == "Hoàn thành job thành công":
                print("\033[38;5;51mHoàn thành lần thứ 2 thành công")
                break
              ms = x['message']
              prices=x['data']['prices']  
              print(f"+{price} đồng")       
              break
            if x['status'] == 400:
              skipjob(token,user_agent,account_id,ads_id,object_id,type)
              break
          except:
            continue
      if x['status'] == 422:
        skipjob(token,user_agent,account_id,ads_id,object_id,type)
        break
    except:
      continue
       
          
  


def getjob(account_id,token,user_agent,delay):
  os.system('clear')
  headers = {
    'authority': 'sv5.golike.net',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'authorization': f'Bearer {token}',
    'content-type': 'application/json;charset=utf-8',
    'origin': 'https://app.golike.net',
    'referer': 'https://app.golike.net/',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    't': 'VFZSWk5VMUVSWGxOZWxsNlRrRTlQUT09',
    'user-agent': user_agent,
}
  params = {
    'account_id': account_id,
    'data': 'null',
}
  while True:
    try:
      response = requests.get('https://sv5.golike.net/api/advertising/publishers/tiktok/jobs', params=params, headers=headers).json()
      sleep(0.1)
      if response['status'] == 200:
        link = response['data']['link']
        type=response['lock']['type']
        ads_id=response['lock']['ads_id']
        object_id=response['lock']['object_id']
        os.system(f"termux-open-url {link}")
        print(f'\x1b[38;5;207m| {link} | {type} \x1b[38;5;208m| {ads_id} \x1b[38;5;46m|')
        nxu(token,account_id,user_agent,ads_id,object_id,type)
      if response['status'] == 400:
        print("\033[1;33m Đang tìm job để làm, đợi xíu",end="  \r")
        continue
    except:
      print("\033[1;31m Nhận job thất bại")

def login(token,user_agent):
  os.system('clear')
  headers = {
    'authority': 'sv5.golike.net',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'authorization': f'Bearer {token}',
    'content-type': 'application/json;charset=utf-8',
    'origin': 'https://app.golike.net',
    'referer': 'https://app.golike.net/',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    't': 'VFZSWk5VMUVSWGhQVkd0NFRtYzlQUT09',
    'user-agent': user_agent,
}
  try:
    response = requests.get('https://sv5.golike.net/api/tiktok-account', headers=headers).json()
    if response['status'] == 200:
      for i in response['data']:
        nickname=i.get('nickname')
        accid=i.get('id')
        print('=> acc:' ,nickname ,'|' ,'ID:' ,accid)
      account_id=input("\x1b[38;5;207mNhập id acc muốn chạy: ")
      getjob(account_id,token,user_agent,delay)
  except:
    print("\033[1;31m KHÔNG ĐÚNG")

def slow_print(text, delay):
    for char in text:
        color_code = random.choice(["red", "green", "yellow", "blue", "magenta", "cyan", "white"])
        colored_char = colored(char, color_code)
        print(colored_char, end='', flush=True)
        time.sleep(0.1)
    print()
token = input("\x1b[38;5;207mNHẬP TOKEN: ")
user_agent = input("\x1b[38;5;208mNHẬP USER_AGENT: ")
delay = float(input("\x1b[38;5;46mNhập DELAY: "))
login(token, user_agent)