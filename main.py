from pytube import YouTube
import ffmpeg
import PySimpleGUI as sg
import os
sg.theme('DarkPurple6')


url = 'https://youtu.be/rUWxSEwctFU'

layout = [  [sg.Text('YouTube URL: '), sg.InputText(key='-URL-')],
            [sg.Text('Video itag: '), sg.InputText(key='-VID-'),
                sg.Text('Audio itag: '), sg.InputText(key='-AUD-')],
            [sg.Button('Show itags'), sg.Button('Download'), sg.CloseButton('Exit')],
            [sg.Output(size=(100, 60), key='-DISPLAY-')]  ]       #displays any printed text in GUI

window = sg.Window('YouTube Downloader', layout)


while True:
    event, values = window.read()

    if event is (None):
        break

    if event is ('Show itags'):
        yt = YouTube(values['-URL-'])
        streams = yt.streams.all()

        for i in streams:
            print(i)

        window['-DISPLAY-'].update()

    if event is ('Download'):
        yt = YouTube(values['-URL-'])
        video = yt.streams.get_by_itag(values['-VID-'])
        audio = yt.streams.get_by_itag(values['-AUD-'])
        video_file = video.download()
        os.rename(video_file, 'video_file')
        audio_file = audio.download()
        os.rename(audio_file, 'audio_file')

        video_stream = ffmpeg.input('video_file')
        audio_stream = ffmpeg.input('audio_file')
        ffmpeg.output(audio_stream, video_stream, 'combined.webm').run()
