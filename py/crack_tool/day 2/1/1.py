import base64


code = """print('xin chào ae')"""

def enc(c):
    code = base64.a85encode(c.encode())
    return f"""import base64;exec(base64.a85decode({code}))""".encode()


open("cc.py","wb").write(enc(code))