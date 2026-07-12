class Video():
    def __init__(self,title,link):
        self.title = title
        self.link = link

def read_video(): # nhập vào 1 video
    title = input("Enter title: ")
    link = input("Enter link: ")
    video = Video(title,link) # gọi lên class video
    return video
def print_video(video):
    print("video title:", video.title,end="")
    print("video link:", video.link,end="")

def read_videos():
    videos = []
    total_video = int(input("Enter how videos: "))
    for i in range(total_video):
        print("Enter video ",i+1)
        vid = read_video()
        videos.append(vid)
    return videos

def print_videos(videos):
    for i in range(len(videos)):
        print_video(videos[i])

def write_video_text(video,file):
    file.write(video.title +"\n")
    file.write(video.link +"\n")

def write_videos_text(videos):
    total = len(videos)
    with open("data.txt","w") as file:
        file.write(str(total)+"\n")
        for i in range(total):
            write_video_text(videos[i],file)

def read_videos_from_txt(file):
    title = file.readline()
    link = file.readline()
    video = Video(title,link)
    return video
def read_video_from_text():
    videos = []
    with open("data.txt","r") as file:
        total = file.readline() # đọc dòng đầu tiên nếu chạy lần nữa sẽ trả vè dòng tiếp theo
        for i in range(int(total)):
            video = read_videos_from_txt(file)
            videos.append(video)
    return videos

def main():
    videos = read_videos()
    write_videos_text(videos)
    videos = read_video_from_text()
    print_videos(videos)

main()


