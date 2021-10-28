import os
import sys
import pyttsx3
import datetime
import pyaudio
import wikipedia
import webbrowser
import pyjokes
from datetime import date
import speech_recognition as sr
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>5 and hour<12:
        speak("Good mmorning sir , how may i help you")
    elif hour>=12 and hour<16:
        speak("Good afternoon sir, how may i help you")
    elif hour>=16 and hour<20:
        speak("Good evening sir, how may i help you")
    else:
        speak("hello sir, how may i help you")
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone()as source:
        print("Listening...")
        r.pause_threshold = 1
        audio =r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        #print(e)
        print("Please say it again")
        return "None"
    return query
if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower() #Converting user query into lower case

        # Logic for executing tasks based on query
        if 'who' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            print('searching...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

            speak("Do you think detail is wrong")
            print("Do you think detail is wrong")
            takeCommand()
            if 'yes' in query:
                speak("Sorry for inconvenience, please search on wikipedia yourself, here you go")
                print("Sorry for inconvenience, please search on wikipedia yourself, here you go")
                webbrowser.open("https://www.wikipedia.org/")
            else:
                speak("thank you for your feedback")
                print("thank you for your feedback")


        elif 'your name' in query:
            speak("My name is Daisy and i am laptop assistant of my creater Vishwas")

        elif 'open youtube' in query:
            speak('opening...')
            print('opening...')
            webbrowser.open("youtube.com")

        elif 'music' in query:
            speak('opening...')
            print('opening')
            webbrowser.open("https://music.youtube.com/")

        elif 'google' in query:
            speak('opening')
            print('opening')
            webbrowser.open("www.google.com")

        elif 'kota factory season 2' in query:
            speak('opening')
            print('opening')
            webbrowser.open("https://fulltube.cc/kota-factory-2021-hindi-season-2/")

        elif 'Discord' in query:
            webbrowser.open("https://discord.com/channels/@me")
            speak("Opening discord")
            print("opening discord")

        elif 'Gmail' in query:
            webbrowser.open("https://mail.google.com/mail/u/1/#inbox")
            speak("opening gmail")
            print("opening gmail")

        elif 'joke' in query:
            joke=pyjokes.get_joke()
            speak(joke)
            print(joke)

        elif 'LMS' in query:
            webbrowser.open("https://lms.bennett.edu.in/login/index.php")
            speak("Opening LMS")
            print("Opening LMS")


        elif 'whatsapp' in query:
            speak('opening')
            print('opening')
            webbrowser.open("https://web.whatsapp.com/")

        elif 'wikipedia' in query:
            speak("opening...")
            print("opening...")
            webbrowser.open('https://www.wikipedia.org/')

        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir, time is {strTime}")

        elif 'pycharm' in query:
            codepath="D:\\PyCharm Community Edition 2021.2.2\\bin\\pycharm64.exe"
            os.startfile(codepath)
            speak("opening...")
            print("opening...")

        elif 'brave' in query:
            codepath="C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
            os.startfile(codepath)
            speak("opening..")
            print("opening...")

        elif 'android studio' in query:
            codepath="D:\\android studio\\bin\\studio64.exe"
            os.startfile(codepath)
            speak("opening android studio")
            print("opening android studio")

        elif 'outlook' in query:
            codepath="C:\\Program Files\\Microsoft Office\\root\\Office16\\OUTLOOK.EXE"
            os.startfile(codepath)
            speak("opening outlook")
            print("opening outlook")

        elif "command" in query:
            os.system("start cmd")
            speak("opening command prompt")
            print("opening command prompt")

        elif "shut down" in query:
            os.system("shutdown /s /t5")

        elif "close" in query:
            speak("Thanks for working with me. Bye  Bye sir")
            sys.exit()

        else:

            print("I am still learning")


