import os
from mutagen.mp3 import MP3

path = r'J:\dejavu\music'
ml=0.0

filenames = os.listdir(path)
for filename in filenames:
    audio = MP3("music/"+filename)
    ml=ml+audio.info.length

print("min:", round(ml/60,2))
print("sec:", round(ml,2))