import requests

g = requests.get

def get(*a,**kw):
    print(a)
    return g(*a,**kw)
requests.get = get
