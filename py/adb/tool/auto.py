import os
import time

while True:
	os.system("adb -s 192.168.43.144:5555 shell input tap 252 965")
	time.sleep(4)
	exit()