import os
import sys
import pyttsx3
#text to speech
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
        question=r.recognize_google(audio,language='en-in')
        print(f"User said: {question}\n")
    except Exception as e:
        #print(e)
        print("Please say it again")
        return "None"
    return question
if __name__ == "__main__":
    wishMe()
    while True:
        question = takeCommand().lower()
        if 'who' in question:
            speak('Searching Wikipedia...')
            print('searching...')
            question = question.replace("wikipedia", "")
            results = wikipedia.summary(question, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

            speak("Do you think detail is wrong")
            print("Do you think detail is wrong")
            takeCommand()
            if 'yes' in question:
                speak("Sorry for inconvenience, please search on wikipedia yourself, here you go")
                print("Sorry for inconvenience, please search on wikipedia yourself, here you go")
                webbrowser.open("https://www.wikipedia.org/")
            else:
                speak("thank you for your feedback")
                print("thank you for your feedback")

        elif 'your name' in question:
            speak("My name is Spec   and i am your voice assistant.")

        elif 'how are you' in question:
            speak("I am fine, how are you sir")

        elif 'open youtube' in question:
            speak('opening...')
            print('opening...')
            webbrowser.open("youtube.com")

        elif 'music' in question:
            speak('opening...')
            print('opening')
            webbrowser.open("https://music.youtube.com/")

        elif 'google' in question:
            speak('opening')
            print('opening')
            webbrowser.open("www.google.com")

        elif 'discord' in question:
            webbrowser.open("https://discord.com/channels/@me")
            speak("Opening discord")
            print("opening discord")

        elif 'Gmail' in question:
            webbrowser.open("https://mail.google.com/mail/u/1/#inbox")
            speak("opening gmail")
            print("opening gmail")

        elif "i don't care" in question:
            webbrowser.open("https://music.youtube.com/watch?v=7hDam9i-Aps&list=RDAMVM7hDam9i-Aps")
            speak("playing")

        elif "excuses" in question:
            webbrowser.open("https://music.youtube.com/watch?v=x18b0D8sTwo&list=RDAMVMx18b0D8sTwo")
            speak("playing")

        elif 'joke' in question:
            joke=pyjokes.get_joke()
            speak(joke)
            print(joke)

        elif 'LMS' in question:
            webbrowser.open("https://lms.bennett.edu.in/login/index.php")
            speak("Opening LMS")
            print("Opening LMS")


        elif 'whatsapp' in question:
            speak('opening')
            print('opening')
            webbrowser.open("https://web.whatsapp.com/")

        elif 'wikipedia' in question:
            speak("opening...")
            print("opening...")
            webbrowser.open('https://www.wikipedia.org/')

        elif 'the time' in question:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir, time is {strTime}")

        elif 'pycharm' in question:
            codepath="D:\\PyCharm Community Edition 2021.2.2\\bin\\pycharm64.exe"
            os.startfile(codepath)
            speak("opening...")
            print("opening...")

        elif 'brave' in question:
            codepath="C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
            os.startfile(codepath)
            speak("opening..")
            print("opening...")

        elif 'android studio' in question:
            codepath="D:\\android studio\\bin\\studio64.exe"
            os.startfile(codepath)
            speak("opening android studio")
            print("opening android studio")

        elif 'outlook' in question:
            codepath="C:\\Program Files\\Microsoft Office\\root\\Office16\\OUTLOOK.EXE"
            os.startfile(codepath)
            speak("opening outlook")
            print("opening outlook")

        elif "command" in question:
            os.system("start cmd")
            speak("opening command prompt")
            print("opening command prompt")

        elif "shut down" in question:
            os.system("shutdown /s /t5")

        elif "sing" in question:
            speak("Sorry sir, I can't sing but i am sure i few weeks i will learn to sing")


        elif "sleep" in question:
            speak("Thanks for working with me. Bye  Bye sir ,Have a nice day ")
            sys.exit()
        else:
            print("I am still learning")


