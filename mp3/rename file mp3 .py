# lấy tiêu đề của bài nhạc

from mutagen.easyid3 import EasyID3
import os

import re
def clean_filename(name):
    # Thay các ký tự cấm bằng dấu "_"
    return re.sub(r'[\\/*?:"<>|]', "_", name)
def main():
    for mp3 in os.listdir(path='.'):
        if ".mp3" in mp3:
            audio = EasyID3(mp3)
            print(audio.get("title")[0])
            safe_name = clean_filename(audio.get("title")[0]) + ".mp3"
            os.rename(mp3,safe_name)


