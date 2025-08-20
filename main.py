import speech_recognition as sr
import os
import webbrowser
import datetime

chatStr = ""


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold =  1
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from Jarvis"

if __name__ == '__main__':
    print('Welcome to Tusk A.I')

    while True:
        print("Listening...")
        query = takeCommand()
        #sites
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"], ["google", "https://www.google.com"],["Instagram", "https://www.instagram.com"],["X", "https://www.x.com"],["Spotify", "https://www.spotify.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                print(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])

        if "open music" in query:
            musicPath = "C:/Users/DELL/Downloads/Flute Song.mp3"
            os.system(f"open {musicPath}")

        elif "the time" in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Sir time is {time} ")


        elif "Quit".lower() in query.lower():
            exit()

        elif "reset chat".lower() in query.lower():
            chatStr = ""

        else:
            print("Chatting...")

