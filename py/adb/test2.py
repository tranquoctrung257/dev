import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "Hieu.exe",
            message = "máy tính của trung bị hack rồi!!!",
            timeout = 10
        )
        time.sleep(3600)
