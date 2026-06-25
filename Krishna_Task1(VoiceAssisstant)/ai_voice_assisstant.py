import pyttsx3
import speech_recognition as sr
import pyautogui
import time
import datetime
import wikipedia
import webbrowser
import os
import random
import smtplib
import getpass
import platform

# Initialize pyttsx3
engine = pyttsx3.init('nsss')
voices = engine.getProperty('voices')

for voice in voices:
    print(voice.id)
    print(voice.name)
# Email dictionary - add your actual contacts
email_dict = {
    "friend": "friend@example.com",
    "family": "family@example.com"
}

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    assistant_name = "Hunterdii"
    speak(f"I am {assistant_name}. Please tell me how may I help you")

def takecommand():
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)
    except Exception as e:
        print(f"Microphone error: {e}")
        speak("I couldn't access your microphone. Please check it.")
        return "None"

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    # Get email credentials securely - DON'T hardcode passwords!
    # Option 1: Use environment variables (recommended)
    # email_user = os.environ.get('EMAIL_USER')
    # email_password = os.environ.get('EMAIL_PASSWORD')
    
    # Option 2: Input at runtime (for testing)
    email_user = 'krishna.arukala0099gmail.com'
    email_password = getpass.getpass("Enter your email password: ")  # More secure
    
    # Use Gmail with APP PASSWORD (not regular password) - enable in Gmail settings
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    try:
        server.login(email_user, email_password)
        # Use same email for sender as login
        server.sendmail(email_user, to, content)
        server.close()
        return True
    except Exception as e:
        print(f"Email error: {e}")
        server.close()
        return False

if __name__ == "__main__":
    wishMe()
    while True:
        query = takecommand().lower()
        
        # Skip if no valid command was received
        if query == "None":
            continue
        
        # Exit commands
        if query in ['exit', 'stop', 'quit', 'goodbye']:
            speak("Shutting down Hunterdii. Goodbye!")
            break

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "").strip()
            if not query:
                speak("Please tell me what to search on Wikipedia")
                continue
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except Exception as e:
                speak(f"Sorry, I couldn't find information about {query}")
                print(f"Wikipedia error: {e}")

        elif 'open youtube' in query:
            webbrowser.open("https://youtube.com")

        elif 'open google' in query:
            webbrowser.open("https://google.com")

        elif 'play music' in query:
            music_url = "https://music.youtube.com/playlist?list=PLIL965-SXjbVEiWwe1l6RApWYDnbhc_Oz&si=g69JUw7JlEO2s0k2"
            webbrowser.open(music_url)
            time.sleep(5)
            pyautogui.press('space')

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the current time is {strTime}")
        
        elif 'open code' in query:
            codepath = r"C:\Users\hetpa\OneDrive\Desktop\Python Programs\server.py"
            os.system(f'start "" "{codepath}"')

        elif 'search google for' in query:
            search_query = query.replace('search google for', '').strip()
            webbrowser.open(f"https://www.google.com/search?q={search_query}")

        elif 'search youtube for' in query:
            search_query = query.replace('search youtube for', '').strip()
            webbrowser.open(f"https://www.youtube.com/results?search_query={search_query}")

        elif 'search in hindi for' in query:
            search_query = query.replace('search in hindi for', '').strip()
            webbrowser.open(f"https://www.google.com/search?hl=hi&q={search_query}")

        elif 'search in gujarati for' in query:
            search_query = query.replace('search in gujarati for', '').strip()
            webbrowser.open(f"https://www.google.com/search?hl=gu&q={search_query}")

        elif 'send email to' in query:
            try:
                speak("What should I say?")
                content = takecommand()
                if content == "None":
                    speak("I didn't catch what you want to say")
                    continue
                    
                speak("Who should I send it to?")
                recipient = takecommand().lower()
                
                # FIXED: Check if recipient exists in dictionary
                if recipient not in email_dict:
                    speak(f"Sorry, I don't have an email for {recipient}. Available contacts: {', '.join(email_dict.keys())}")
                    continue
                    
                to = email_dict[recipient]
                if sendEmail(to, content):
                    speak("Email has been sent!")
                else:
                    speak("Sorry, I am not able to send this email.")
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to send this email.")

        elif 'open notepad' in query:
            os.system("notepad.exe")

        elif 'open calculator' in query:
            os.system("calc.exe")

        elif 'open command prompt' in query:
            os.system("cmd.exe")

        elif 'shutdown' in query:
            speak("Shutting down your computer in 1 second...")
            time.sleep(1)
            os.system("shutdown /s /t 0")

        elif 'restart' in query:
            speak("Restarting your computer in 1 second...")
            time.sleep(1)
            os.system("shutdown /r /t 0")
