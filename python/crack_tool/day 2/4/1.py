# đối vs dạng nhiều lớp

import base64
import marshal

code = """print('xin chào ae')""".encode()

def enc(c):
    code = compile(c,"<string>","exec")
    code = marshal.dumps(code)
    code = base64.a85encode(code)
    return f"""import base64,marshal;exec(marshal.loads(base64.a85decode({code})))""".encode()

for i in range(10):
    code = enc(code)
    
open("cc.py","wb").write(code)