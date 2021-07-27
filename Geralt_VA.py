import pyttsx3 #pip install pyttsx3
import pyaudio #pip install pipwin #pipwin install pyaudio
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=5 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<16:
        speak("Good Afternoon!") 

    elif hour>=16 and hour<20:
        speak("Good Evening!")   
  
    else:
        speak("Hello!")  

    speak("I am Geralt Mam. Please tell me how may I help you")       

def takeCommand():
    #takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1 #manages speed during speech recognition
        r.energy_threshold = 500 #manages background noise
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('abc@gmail.com', 'password')
    server.sendmail('xyz@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()


        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open code' in query:
            #opens online compiler for coding
            webbrowser.open("onlinegdb.com")   

        elif 'play video' in query:
            # opens selected series or movie file present in the D drive
            video_dir = 'D:\\'
            files = os.listdir(video_dir)
            print(files)    
            os.startfile(os.path.join(video_dir, files[4]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Mam, the time is {strTime}")

        elif 'open media player' in query:
            # opens VLC media player
            codePath = "C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe"
            os.startfile(codePath)

        elif 'email to me' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "xyz@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Shreyanta sama. I am not able to send this email")   
                # enable the less secure apps feature in your Gmail account to prevent Google security from blocking the function call

        elif 'quit' in query or 'bye' in query:
            speak("Thank you for your time mam. Hope to see you soon.")
            exit()
