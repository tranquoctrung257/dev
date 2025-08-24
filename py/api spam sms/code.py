import requests
def fpt_shop(sdt):
    headers = {
        'accept': '*/*',
        'accept-language': 'vi,en;q=0.9',
        'apptenantid': 'E6770008-4AEA-4EE6-AEDE-691FD22F5C14',
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        'order-channel': '1',
        'origin': 'https://fptshop.com.vn',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://fptshop.com.vn/',
        'sec-ch-ua': '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
    }
    json_data = {'fromSys': 'WEBKHICT','otpType': '0','phoneNumber': sdt
    }
    return requests.post('https://papi.fptshop.com.vn/gw/is/user/new-send-verification', headers=headers, json=json_data)

def viettel(phone):
    import requests

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi,en;q=0.9',
        'cache-control': 'no-cache',
        # 'content-length': '0',
        'origin': 'https://viettel.vn',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://viettel.vn/',
        'sec-ch-ua': '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
    }

    response = requests.post(
        'https://apigami.viettel.vn/mvt-api/myviettel.php/getOTPCommon?lang=vi&phone=sdt&actionCode=myviettel:%2F%2Flogin_mobile&typeCode=DI_DONG&type=otp_login&isResetOtp=false'.replace("sdt",phone),
        headers=headers,
    )
    return response.json()
