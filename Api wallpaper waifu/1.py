import requests

def img():
    s = requests.get("https://api.waifu.pics/sfw/waifu")
    
    img = s.json()['url']
    
    name = img.split("/")[-1].split('.')[0]
    
    img_response = requests.get(img)
    with open(f"{name}.jpg",mode="wb") as file:
        file.write(img_response.content)
    print(f"lưu thành công{name}.jpg")

for i in range(10000):
    print(i)
    img()