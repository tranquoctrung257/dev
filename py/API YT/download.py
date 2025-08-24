from pytubefix import YouTube
from pytubefix.cli import on_progress

url = 'https://www.youtube.com/watch?v=7YLA3_QIeA0&list=RD7YLA3_QIeA0&index=1'
yt = YouTube(url, on_progress_callback=on_progress)


def itags(resolution='1080p'):
    max_audio = 0
    audio_value = 0
    for audio_stream in yt.streams.filter(only_audio=True):
        abr = int(audio_stream.abr.replace('kbps', ''))
        if abr > max_audio:
            max_audio = abr
            audio_value = audio_stream.itag
    streams = yt.streams
    try:
        video_tag = streams.filter(res=resolution, fps=60)[0].itag
        print('60 FPS')
    except IndexError:
        video_tag = streams.filter(res=resolution, fps=30)
        if video_tag:
            video_tag = video_tag[0].itag
            print('30 FPS')
        else:
            video_tag = streams.filter(res=resolution, fps=24)[0].itag
            print('24 FPS')
    return audio_value, video_tag


audio, video = itags('1080p') # specify the resolution    
yt.streams.get_by_itag(audio).download() # downloads audio
yt.streams.get_by_itag(video).download() # downloads video