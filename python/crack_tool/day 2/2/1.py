import base64


code = """print('xin chào ae')""".encode()

def enc(c):
    code = base64.a85encode(c)
    return f"""import base64;exec(base64.a85decode({code}))""".encode()

for i in range(10):
    code = enc(code)
open("cc.py","wb").write(code)