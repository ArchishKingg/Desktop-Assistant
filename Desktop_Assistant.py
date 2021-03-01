import pyttsx3 as p
import speech_recognition as sr
import datetime
from datetime import date
import webbrowser
import os
import requests
from pygame import mixer
from bs4 import BeautifulSoup
from win10toast import ToastNotifier
from pywikihow import search_wikihow
import smtplib
from idlist import my_gmail, password

toast = ToastNotifier()
toast.show_toast("Jarvis", "I am Online Sir !", duration=5)
engine = p.init('sapi5')
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
url = 'www.google.com'
weather_url = "https://www.google.com/search?q=temperature+in+islampur&rlz=1C1CHBD_enIN940IN940&oq=temperature+&aqs=chrome.1.69i57j35i39i285j0i433j0i433i457j0i402l2j0j69i61.8511j1j9&sourceid=chrome&ie=UTF-8"
wr = requests.get(weather_url) 
soup = BeautifulSoup(wr.text, "html.parser")
temp = soup.find("div", class_="BNeawe").text
temparature = f"Temperature outside is {temp}"
today = date.today()
date = f"Today's date is {today}"
bd = '2021-06-27'
mixer.init()
g = my_gmail
passw = password

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    strTime = datetime.datetime.now().strftime("%I:%M %p")
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak(f"Good Morning Sir! It is {strTime}")

    elif hour>=12 and hour<18:
        speak(f"Good Afternoon Sir! It is {strTime}")   

    elif date == bd:
        speak("Happy Birthday Sir!")
    
    else:
        speak(f"Good Evening Sir! It is {strTime}")

    speak("I am Jarvis")
    speak(temparature)
    speak(date)
    speak("How can I help you!")

def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(g, passw)
    server.sendmail(g, to, content)
    server.close()

def Command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing....")
        command = r.recognize_google(audio, language='en-in')

    except Exception as e:
        speak("")
        return "None"
    return command

if __name__ == "__main__":
    wish()
    while True:
        command = Command().lower()
        print(command)
        if 'open google' in command:
            speak("Sure Sir! Opening Google")
            os.startfile('C://Program Files (x86)//Google//Chrome//Application//chrome.exe')

        elif 'open youtube' in command:
            speak("Sure Sir! Opening Youtube")
            webbrowser.get(chrome_path).open(url='www.youtube.in')
        
        elif 'open amway' in command:
            speak("Sure Sir! Opening Amway")
            os.startfile('C://Program Files (x86)//Google//Chrome//Application//chrome.exe')
            webbrowser.get(chrome_path).open(url='www.amway.in')
        
        elif 'open vs code' in command:
            speak("Sure Sir! Opening VS Code")
            os.startfile('C://Users//User//AppData//Local//Programs//Microsoft VS Code//Code.exe')

        elif 'you can go to sleep' in  command:
            hour = int(datetime.datetime.now().hour)
            if hour>=0 and hour<12:
                speak("Bye Sir! Have a great day")
                break;

            elif hour>=12 and hour<18:
                speak("Bye Sir! Have a great day")   
                break;

            else:
                speak("Bye Sir. Good Night!")
                break;
        
        elif 'how are you' in  command:
            speak("I am completely fine Sir! How about you?")

        elif 'good morning' in  command:
            speak("Good Morning Sir! How are you!")
        
        elif 'good afternoon' in  command:
            speak("Good Afternoon Sir! How are you!")
        
        elif 'good evening' in  command:
            speak("Good Evening Sir! How are you!")
        
        elif 'i am fine' in  command:
            speak("Its good to hear sir! How can I help you!")
    
        elif 'open telegram' in  command:
            speak("Sure Sir! Opening telegram")
            os.startfile('C://Users//User//AppData//Roaming//Telegram Desktop//Telegram.exe')

        elif 'show my email' in  command:
            speak("Sure Sir! Opening Gmail")
            webbrowser.get(chrome_path).open(url='www.gmail.com')
        
        elif 'open whatsapp' in  command:
            speak("Sure Sir Sir! Opening Whatsapp")
            os.startfile('C://Users//User//AppData//Local//WhatsApp//WhatsApp.exe')

        elif 'i want to see my coding activity' in command:
            speak("Here you go Sir!")
            webbrowser.get(chrome_path).open(url='https://wakatime.com/dashboard')
        
        elif 'thank you' in command:
            speak("Its my pleasure Sir! Welcome")

        elif 'hello jarvis' in command:
            speak("Hi Sir! How are you?")

        elif 'open github' in command:
            speak("Sure Sir! Opening GitHub")
            webbrowser.get(chrome_path).open(url='https://github.com/')
        
        elif 'open amazon' in command:
            speak("Sure Sir! Opening Amazon")
            webbrowser.get(chrome_path).open(url='https://www.amazon.in')
        
        elif 'play some songs' in command:
            music_dir = 'D://@Archishman Sinha//@MUSIC@'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))
            speak("Enjoy the music Sir!")
        
        elif 'what is your name' in command:
            speak("I am Jarvis. Your Personal Assistant")

        elif 'what is the time' in command:
            strTime = datetime.datetime.now().strftime("%I:%M %p")    
            speak(f"Sir, the time is {strTime}")

        elif 'open ti launcher' in command:
            speak("Sure Sir! opening T Launcher")
            os.startfile('C://Users//User//AppData//Roaming//.minecraft//TLauncher.exe')

        elif 'open fl studio' in command:
            speak("Sure Sir! openinf fl studio")
            os.startfile('D://@Archishman Sinha//FL Studio 20//FL64.exe')

        elif 'are you online' in command:
            speak("I am online and perfect Sir!")

        elif 'greet everyone' in command:
            speak("Hello Everyone!")

        elif 'activate steps mode' in command:
            speak("Steps mode activated. Please tell me what you want to know!")
            how = Command().lower()
            max_res = 1
            res = search_wikihow(how, max_res)
            assert len(res) == 1
            res[0].print()
            speak(res[0].summary)

        elif 'activate cmd mode' in command:
            speak("Activating cmd mode! What command I shall give?")
            com = Command().lower()
            try:
                os.system(f'cmd /k "{com}"')
                continue
            except:
                speak("Sorry cannot execute that command")
                continue
                
        elif 'open instagram' in command:
            speak("Sure Sir! Opening Instagram")
            webbrowser.get(chrome_path).open(url='www.instagram.com')

        elif 'introduce yourself' in command:
            speak("Hello! My name is Jarvis! I am a Artificial Intelligence program made by Archishman Sinha. I can do a variety of tasks. Try me if you want to!!")

        elif 'shut down my pc' in command:
            speak("Sure Sir! Shutting down your PC")
            os.system("shutdown /s /t 1")

        elif 'what is the temperature today' in command:
            speak(temparature)

        elif 'kemon acho' in command:
            speak("Ami bhaalo aachi")

        elif 'create a python file in vs code' in command:
            speak("What should i name the file?")
            fn = Command()
            ffn = f"{fn}.py"
            f = open(ffn, "a")
            speak("File created sucessfully")

        elif 'play some music' in command:
            speak("Should I play Avichi music?")
            mi = Command()
            print(mi)
            if "yes" == mi:
                speak("OK Sir! Enjoy some Avichi vibes!!")
                mixer.music.load('D://Assistant//avicii//avicii_playlist.mp3')
                mixer.music.play()
            else:
                speak("Umm.. Then Martin Garrix music?")
                omi = Command()
                if omi == "yes":
                    speak("Ok Sir! Enjoy Martin vibes!")
                    mixer.music.load('D://Assistant//m_garrix//m_garrix.mp3')
                    mixer.music.play()
                else:
                    speak("Ok! playing some other EDMs")
                    mixer.music.load('D://Assistant//b_edm//b_edm.mp3')
                    mixer.music.play()
                
        elif 'stop the music' in command:
            try:
                mixer.music.set_volume = 0
                speak("Ok Sir! Stopping the music!")
                mixer.music.stop()
            except:
                speak("Sorry Sir! No music is playing")
        
        elif 'sorry' in command:
            speak("No problem sir! Its OK!")
        
        elif 'glad you are online' in command:
            speak("Thank you Sir! Always at your service!")
        
        elif 'activate drink water notifier' in command:
            speak("Activating water notifier")
            os.startfile('D://Assistant//notifiers//water_notifier.vbs')
        
        elif 'search something in google' in command:
            speak("What should I search?")
            gsearch = Command()
            g_search = gsearch.replace(" ", "+")
            g_url = f'http://www.google.com/search?q={g_search}'
            webbrowser.get(chrome_path).open(g_url)
        
        elif 'search something in youtube' in command:
            speak("What should I search?")
            ysearch = Command()
            y_search = ysearch.replace(" ", "+")
            y_url = f'https://www.youtube.com/results?search_query={y_search}'
            webbrowser.get(chrome_path).open(y_url)

        elif 'open w3 schools' in command:
            speak("Opening W3Schools I hope you learn something new. Good Luck Sir!")

        elif 'i want to code' in command:
            speak("Sure Sir! Opening VS Code")
            os.startfile('C://Users//User//AppData//Local//Programs//Microsoft VS Code//Code.exe')

        elif 'jarvis' in command:
            speak('Yes Sir!')
        
        elif 'can i know the temparature' in command:
            speak(temparature)

        elif 'open calculator' in command:
            speak("Ok Sir! opening calculator")
            os.startfile('calc.exe')

        elif 'send an email' in command:
            try:    
                speak("Whom should i send")
                to_a = Command().lower()
                a = to_a.replace(" ","")
                to = f"{a}@gmail.com"
                print(to)
                speak("What should I say!")
                content = Command()
                sendEmail(to, content)
                speak("Email has been sent successfully")
            except Exception as e:
                print(e)
                speak("Sorry Sir! I cannot send the email due to an error")
        
        elif 'open sublime text' in command:
            speak("Sure Sir! Opening Sublime Text")
            os.startfile('D://Sublime Text 3//sublime_text.exe')

        elif 'open odea' in command:
            speak("Sure SIr! opening IntelliJ Idea")
            os.startfile('C://Program Files//IntelliJ IDEA Community Edition 2020.2.3//bin//idea64.exe')
        
        elif 'open virtual box' in command:
            speak("Sure Sir! opening Virtual Box")
            os.startfile('C://ProgramData//Microsoft//\Windows//Start Menu//Programs//Oracle VM VirtualBox//Oracle VM VirtualBox.exe')

        # elif '' in command:
        #     pass
       
        # elif '' in command:
        #     pass
        
        # elif '' in command:
        #     pass
        
        elif '' in command:
            pass