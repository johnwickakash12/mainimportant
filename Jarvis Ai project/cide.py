def takecommand():
    #It takes microphone input from the user and returns string  
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold=1
        audio = r.listen(source)
    try:
        print("Recognize...")
        query=r.recognize_google(audio,language='en-in')
        print(f"user said:{query}\n")
    except Exception as e:
        print(e)
        print("Say that again please")
        return "None"
    return query   