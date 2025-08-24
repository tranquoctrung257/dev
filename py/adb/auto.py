import os
import time
i = 0
while True:
	os.system("adb -s 192.168.43.144:5555 shell input tap 276 950")
	time.sleep(3)
	i +=1
	print(i)