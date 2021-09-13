import pyttsx3
# import win32com.client as wincl
# import isapi

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)
# engine.say("whtaever you want")


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

if __name__ == '__main__':
    speak("murat is a good boy")