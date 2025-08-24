import os,time, sys

try:
    import numpy as np 
except:
    os.system("pip install numpy")
    os.system("pip install cv2")
    os.system("pip install opencv-python")
import numpy as np
import cv2

class ADB:
    def __init__(self,handle):
        self.handle = handle
    def screen_capture(self,name):
        os.system(f"adb -s {self.handle} exec-out screencap -p > {name}.png ")
    def click(self,x,y):
        os.system(f"adb -s {self.handle} shell input tap {x} {y}")
    def find(self,img='',template_pic_name=False,threshold=0.99):
        if template_pic_name == False:
            self.screen_capture(self.handle)
            template_pic_name = self.handle+'.png'
        else:
            self.screen_capture(template_pic_name)
        img = cv2.imread(img)
        img2 = cv2.imread(template_pic_name)
        result = cv2.matchTemplate(img,img2,cv2.TM_CCOEFF_NORMED)
        loc = np.where(result >= threshold)
        test_data = list(zip(*loc[::-1]))
        return test_data


d = ADB('BH901UNSCR')
while True:
    for i in range(2,-1,-1): time.sleep(1);print(i,end="\r")
    point = d.find('fl1.png')
    try:
        d.click(point[0][0],point[0][1])
        print(point)
        print("==> Thành công")
    except:
        print('-.-[không tìm thấy hình ảnh]')