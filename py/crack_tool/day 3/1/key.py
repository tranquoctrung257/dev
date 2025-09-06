import marshal,base64

code = """from curl_cffi import requests

key = input("nhập key: ")

key_tool= requests.get("https://raw.githubusercontent.com/trung2570/key/refs/heads/main/key.json").json()["key"]
# print(key_tool)
try:
    if int(key) == key_tool:
        print("tool chạy")
    else:
        print("sai key r ku")
except:
    exit()
"""

def enc(c):
    code = compile(c,"<string>","exec")
    code = marshal.dumps(code)
    code = base64.a85encode(code)
    return f"""import base64,marshal;exec(marshal.loads(base64.a85decode({code})))""".encode()

for i in range(10):
    code = enc(code)
    
open("cc.py","wb").write(code)