import requests


headers = {
    'accept': 'application/json',
    'accept-language': 'vi,en;q=0.9',
    'bx-v': '2.5.31',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'origin': 'https://www.lazada.vn',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.lazada.vn/shop/skincarebeautysaigon',
    'sec-ch-ua': '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
    'cookie': '__wpkreporterwid_=8f75711a-6a7c-4aa1-8198-aeba5f113d29; miidlaz=miidgjnlv11ivftudial399; t_fv=1751807637388; t_uid=08uXzG3NMWc9vLCleuovLNsUzR9QQKst; __itrace_wid=c535d660-9b60-4946-37fa-e9251b6c3692; lzd_cid=b94defed-6894-4238-9b91-599433ac6e9c; lwrid=AgGX399zf7t5jCDXsA%2FxX39uIxoL; pdp_sfo=1; G_ENABLED_IDPS=google; lzd_login_lastlogintype=GOOGLE; hng=VN|vi|VND|704; hng.sig=EmlYr96z9MQGc5b9Jyf9txw1yLZDt_q0EWkckef954s; lzd_click_id=clk5lnq0q1j24v3f1cbtvs; t_sid=QSVdLJTY0WI5AKbB1cwHBpKVEe8ra4c5; utm_channel=NA; lzd_sid=174f748b7bcd6d1430c42daf50e0dc08; _tb_token_=f9488bd76eb57; _m_h5_tk=165950f234111c265bb7c18d68e5c967_1755863084694; _m_h5_tk_enc=94b0f89ebf83e277dda7d0e781340293; lwrtk=AAIEaKim7JBTW6bh0VftRDh5CAMmVY7eCgEDJjDh3ibOUXIaUJGpW5E=; _bl_uid=9mmg4ehgm37mw1e7anbqkd5dCwFt; isg=BCUlA76EoYylEsUS4R_U6EUYNOFfYtn06fLZJCcLkdxrPkSw7rMVxHyYyLpIPvGs; tfstk=gRurm6idxULze36XPxUFQSFPlH48fyJ_E2wQtXc3N82lPa6n0xHFOQpp2mSn3-QSdzaI3JDoUkgW2k_UYAMFVws7Fy8EIxEILXd8tJDnLJiWcFG-wyUHL2865bFoABtjU74hiBVUtTAbq1CggcaHCdTXAIGEOyDIIW2Tmj2YTabuZv20iWe0Z_qnK-q0s5_u-yDHg-V36gXuxwc0i5w0KyqoKjA4O-Vu-yDniIPKwJcotZP_qIvzZ532RcEzIb2V7A30ZTy6W-bneqFu42cu3oZju7PzQkv4rH3ohX0SyoKRVyhjbvonIKs7EcPZ3liyQakZeWD0iYOCvSoEtVU826QKQzkUj4qVtNlgr0U4iVACX-g4Fv0zmC_aAr0_jzmXDLZQz5knyY5F-Acj14Ex8dW0p0NToWupsMyUxgRApSmaD2nPKMruMSy6gIy46jmLUTfPNMILmPF4CQN5vMEuMSy6gISdvoVTgRO7N; epssw=10*I1yss6HsZuB5zWXQUNxetT39mRokxCuLumARFas3sssssmD6sCFJQkRWO-J0UCssb-D6exDtBpJfcapdDppW102Rc4-f1SopkROQsdxKasssRhFOtyFiNKnsbrdeznxHVJ9cXR8uy4rtTz7BE85BPlXJQ-tPMGxC1NHCOP2nXluncf87bJwgeAvJP5F8X7MQksncBJ8T-Ot_uCKV53bTNoHHPycr58_ZUoPwO-OabRFe3GpzF2G1sssK6RrQiwWaF-aFiHyV6REv2Bf36T70gAS5AzL1xhlLvMwXIPEBMYgQQRHddP26QWcudba4I66tqrA_zTRIA7d.',
}

json_data = {
    'shopId': 4995883,
}

response = requests.post('https://www.lazada.vn/shop/site/api/followup/follow', headers=headers, json=json_data).json()
print(response)


# hmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm