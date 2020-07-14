#Assistant
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("I am Your Assistant. How can I help you.")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please.........")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("Searching Wikipedia.....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("Youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'D:\\sital school\\mp3 songs\\other'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'music' in query:
            music_dir = 'D:\\sital school\\mp3 songs\\other'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'song' in query:
            music_dir = 'D:\\sital school\\mp3 songs\\other'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'play song' in query:
            music_dir = 'D:\\sital school\\mp3 songs\\other'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'open music' in query:
            music_dir = 'D:\\sital school\\mp3 songs\\other'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'open song' in query:
            music_dir = 'D:\\sital school\\mp3 songs\\other'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))


        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S:")
            print(strTime)
            speak(f"The time is {strTime}\n")

        elif 'open paint' in query:
            openPaint = 'C:\\Windows\\system32\\mspaint.exe'
            os.startfile(openPaint)

        elif 'paint' in query:
            openPaint = 'C:\\Windows\\system32\\mspaint.exe'
            os.startfile(openPaint)

        elif 'drawing' in query:
            openPaint = 'C:\\Windows\\system32\\mspaint.exe'
            os.startfile(openPaint)

        elif 'open darwing' in query:
            openPaint = 'C:\\Windows\\system32\\mspaint.exe'
            os.startfile(openPaint)

        elif 'icon converter' in query:
            webbrowser.open("icoconverter.com")

        elif 'ico converter' in query:
            webbrowser.open("icoconerter.com")

        elif 'picture' in query:
            opPic = 'C:\\Windows\\explorer.exe'
            os.startfile(opPic)

        elif 'photo' in query:
            opPic = 'C:\\Windows\\explorer.exe'
            os.startfile(opPic)


        elif 'open picture' in query:
            opPic = 'C:\\Windows\\explorer.exe'
            os.startfile(opPic)

        elif 'open photo' in query:
            opPic = 'C:\\Windows\\explorer.exe'
            os.startfile(opPic)

        elif 'what is your name' in query:
            speak("My name is Sheeetal assistant")

        elif 'who develop you' in query:
            speak("Sheeetal Chandra")
            print("Sital Chandra")

        elif 'who create you' in query:
            speak("Sheeetal Chandra")

        elif 'you are a girl or a boy' in query:
            speak("I am a Girl")

        elif 'what is your gender' in query:
            speak("I am a female")

        elif 'hi' in query:
            speak("Hi Sital")
            print("Hi Sital")

        elif 'open chrome' in query:
            chromePath = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
            os.startfile(chromePath)
