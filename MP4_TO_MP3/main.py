from moviepy.editor import *
from art import *
import tkinter.filedialog as fd
import tkinter.messagebox as msgb

def MP4_TO_MP3():
    MP4 = AudioFileClip(file_path)
    MP4.write_audiofile(audio_path)
    MP4.close()

def openfile():
    global file_path

    try:
        of = fd.askopenfile(
            title="OPEN FILE",
            filetypes=(("Video File","*.mp4 .wav"),),
        )
        file_path = of.name
    except:
        msgb.showerror("ERROR","You need to choose a MP4 file to continue the operation !")
        quit()

def save_file():
    global audio_path
    try:
        sf = fd.asksaveasfile(
            title="Enter Audio File Path",
            filetypes=(("Audio Files","*.mp3"),),
        )
        audio_path = sf.name
    except:
        msgb.showerror("ERROR","You need to choose the MP3 saving file path to continue the operation !")
        quit()

tprint("MP4 To MP3")

input("Press Enter For Continue >>> ")
openfile()
save_file()
MP4_TO_MP3()