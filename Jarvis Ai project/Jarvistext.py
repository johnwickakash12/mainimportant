import os
import wikipedia
import datetime
import smtplib
import webbrowser
import pyttsx3
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    timee=int(datetime.datetime.now().hour)
    if timee<12:
        speak("  Good,  morning sir ")
    elif timee>=12 and timee<18:
        speak(" Good,   Afternoon sir")
    else:
        speak("  Good,   Evening sir")
    speak("I am jarvis ,an ai made from Akash koirala how can i help you")
if __name__=="__main__":
    wishme()
    while True:
        command=input("Waiting for your command\n")
        command=command.lower()
        if 'wikipedia'in command:
            command=command.replace("wikipedia","")
            result=wikipedia.summary(command,sentences=2)
            speak("According to Wikipedia")
            print(f"{result}\n")
            speak(result)
        elif 'open youtube' in command:
            webbrowser.open("youtube.com")
        elif 'open my website' in command:
            webbrowser.open("35.153.98.190")
        elif 'open bluej' in command:
            path1="C:\\Program Files\\BlueJ\\BlueJ"
            os.startfile(path1)
            
        elif'open music' in command:
            codePath = "C:\\Users\\Akash koirala\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'quit' in command:
            break
            