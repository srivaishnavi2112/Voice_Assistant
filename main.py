import pyttsx3 as p 
import speech_recognition as sr
from selenium_web import Infow
from youtube import *
from news import *
import randfacts
from joke import *
from weather import *
import datetime
engine=p.init()
rate=engine.getProperty('rate')
engine.setProperty('rate',180)
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
print(voices)
print(rate)
def speak(text):
    engine.say(text)
    engine.runAndWait()
def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        return("morning")
    elif hour>=12 and hour<16:
        return("afternoon")
    else:
        return("evening")
today_date=datetime.datetime.now()
r=sr.Recognizer()
print("Hello. Good "+wishme()+" I am your voice assistant. Today is "+today_date.strftime("%d")+" of "+today_date.strftime("%B")+" and its currently "+(today_date.strftime("%I"))+(today_date.strftime("%M"))+(today_date.strftime("%p")))
speak("Hello. I am your voice assistant. Today is "+today_date.strftime("%d")+" of "+today_date.strftime("%B")+" and its currently "+(today_date.strftime("%I"))+(today_date.strftime("%M"))+(today_date.strftime("%p")))
print("Temperature in Hyderabad is "+str(temp())+" degree celsius and with "+str(des()))
speak("Temperature in Hyderabad is "+str(temp())+" degree celsius and with "+str(des()))
print("Let me start by asking. How are you?")
speak("Let me start by asking. How are you?")
with sr.Microphone() as source:
    r.energy_threshold=10000
    r.adjust_for_ambient_noise(source,1.2)
    print("listening..")
    audio=r.listen(source)
    text=r.recognize_google(audio)
    print(text)
if "what" and "about" and "you" in text:
    print("I am also having a good day")
    speak("I am also having a good day")
print("What can I do for you??")
speak("What can I do for you??")
with sr.Microphone() as source:
    r.energy_threshold=10000
    r.adjust_for_ambient_noise(source,1.2)
    print("listening..")
    audio=r.listen(source)
    text2=r.recognize_google(audio)
    print(text2)
if "information" in text2:
    print("You need information related to which topic?")
    speak("You need information related to which topic?")
    with sr.Microphone() as source:
        r.energy_threshold=10000
        r.adjust_for_ambient_noise(source,1.2)
        print("listening..")
        audio=r.listen(source)
        infor=r.recognize_google(audio)
        print(infor)
    print("searching {} in wikipedia".format(infor))
    speak("searching {} in wikipedia".format(infor))
    assist=Infow()
    assist.get_info(infor)
elif "play" and "video" in text2:
    speak("you want me to play which video?")
    with sr.Microphone() as source:
        r.energy_threshold=10000
        r.adjust_for_ambient_noise(source,1.2)
        print("listening..")
        audio=r.listen(source)
        video=r.recognize_google(audio)
        print(video)
    print("Playing {} on youtube".format(video))
    speak("Playing {} on youtube".format(video))
    assist=music()
    assist.play(video)
elif "news" in text2:
    print("Sure, Now I will read news for you")
    speak("Sure, Now I will read news for you")
    arr=news()
    for i in range(len(arr)):
        print(arr[i])
        speak(arr[i])
elif "fact" or "facts" in text2:
    print("Sure, ")
    speak("Sure, ")
    x=randfacts.getFact()
    print(x)
    speak("Did you know that, "+x)
elif "joke" or "jokes" in text2:
    print("Sure, get ready for some chuckles")
    speak("Sure, get ready for some chuckles")
    arr=joke()
    print(arr[0])
    speak(arr[0])
    print(arr[1])
    speak(arr[1])