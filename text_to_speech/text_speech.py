from gtts import gTTS
import os


fh = open("test.txt", "r")
thisText = fh.read().replace("\n", " ")

language = 'en'

output = gTTS(text=thisText, lang=language, slow=False)

output.save("output.mp3")
fh.close()
os.system("start output.mp3")