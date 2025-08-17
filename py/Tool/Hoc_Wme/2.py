# Hướng Dẫn Code Tool Từ A-Z - Livestream #2

import requests
# mbasic.facebook.com bị bỏ rùi
# www.facebooke.com

# hàm splip


# proxy trong requests

proxy = {
    "http":'http://yknorahi-rotate:o8ey40xw607g@p.webshare.io:80',
    "https":'https://yknorahi-rotate:o8ey40xw607g@p.webshare.io:80'

}

req = requests.get("http://ip-api.com/json",proxies=proxy).json()
country = req["country"]
regionName = req["regionName"]
city = req["city"]
timezone = req["timezone"]
isp = req["isp"]
IP = req["query"]
print(IP)


