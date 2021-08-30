import moviepy.editor
import tkinter.filedialog

try:
    file = tkinter.filedialog.askopenfilename()
    video = moviepy.editor.VideoFileClip(file)
    list = file.split("/")
    list = list[-1].split(".")
    audio = video.audio
    audio.write_audiofile(f"{list[0]}.mp3")
    print("Completed!")
except:
    print("Please enter a valid video file!")
