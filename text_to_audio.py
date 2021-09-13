from gtts import gTTS
import os
from playsound import playsound

audio = "speech.mp3"
language = 'en'
sp = gTTS(text = "enter your text which you want to convert into audio file ",
          lang = language, slow = False)

sp.save(audio)
playsound(audio)


# import win32com.client
# tts = pyTTS.Create()
# tts.SetVoiceByName('MSSam')
# tts.Speak("Hello, fellow Python prog
# speaker = win32com.client.Dispatch("SAPI.SpVoice")
# speaker.Speak("Hello, it works!")

# import pyTTSrammer")
