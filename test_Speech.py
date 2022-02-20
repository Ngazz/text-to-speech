from gtts import gTTS
import os

textToConvert = gTTS(text="This is Joseph; Joseph is coding python with Lux Academy East Africa", lang='en')
textToConvert.save("Computer_voice.mp3")

os.system("start Computer_voice.mp3")#to output the speech