import requests
import json


def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.Spvoice")
    speak.GetVoices("Name=Microsoft Zira")
    speak.speak(str)

if __name__ == '__main__':
    speak("twinkle how are you")
    url = ""
    news = requests.get(url).text
    news = json.load(news)
    print(news)

# import win32com.client as wincl
# speak = wincl.Dispatch("SAPI.SpVoice")
# speak.Speak("Hello World")