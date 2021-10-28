import speech_recognition as sr
import pyaudio
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold=1
        audio=r.listen(source)
        try:
            print("Recoganizing...")
            quary=r.recognize_google(audio, language='en-in')
            print(quary)

        except Exception as e:
            a="Sorry sir, Please speak again"
            print(a)
takeCommand()

