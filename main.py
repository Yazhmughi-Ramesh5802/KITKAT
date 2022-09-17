from distutils.util import strtobool
from email import message
from tkinter.messagebox import YES
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import pyaudio
import webbrowser as wb
import psutil
import pyjokes
import os
import pyautogui
import random
import json
import requests
from urllib.request import urlopen
import wolframalpha
import time
import pywhatkit
import eel
import js2py
import temp

def printData(x):
    print(x)
    eel.display(x)
# result, tempfile = js2py.run_file("static/script.js");
#
# result= tempfile.connect("Stack Vidhya Reader");
#
# printData(result);



eel.init("static")
engine = pyttsx3.init()
wolframalpha_app_id = r'your_api_key'

# printData('Calling Javascript...')
# eel.my_javascript_function(1, 2, 3, 4)


# def printData(x):
#     # eval_res,tempfile = js2py.run_file("/static/script.js")
#     # tempfile.display(x)
#     # printData(x)
#     printData(x)
# printData("")

def speak(audio):
    # engine.say("hello world")
    engine.say(audio)
    engine.runAndWait()

# speak("hello world")
def time_():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is ")
    speak(Time)

# time_()

def date_():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    date = datetime.datetime.now().day
    speak("The current date is ")
    speak(date)
    speak(month)
    speak(year)

# date_()


def joke():
    speak(pyjokes.get_joke())

    #greetings


# wishme()

def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        printData("Listening...")
        r.pause_threshold = 1
        audio = r.record(source,duration=3)
        #audio = r.listen(source)

    try:
        printData("Recognizing...")
        query = r.recognize_google(audio,language='en-us')
        printData(query)
    except Exception as e:
        printData(e)
        printData("Say that again please")
        return "None"
    return query

def cpu():
    # usage = str(psutil.cpu_percent())
    # speak("CPU is at"+usage)
    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)

def screenshot():
    img = pyautogui.screenshot()
    img.save(r'C:\Users\Yamini\Desktop\imgs\screenshot.jpg')

contacts = [['yalmugi','+91 xxxxxxxxxx'],['vishal', '+91 xxxxxxxxxx'], ['kumar', '+91 xxxxxxxxxx'], ['abinash', '+91 xxxxxxxxxx'], ['a','+91 xxxxxxxxxx']]

def watsapp_image():
    speak("Whom do u wanna send message");
    reciever = TakeCommand().lower();
    send = '+91 xxxxxxxxxx'

    flag = 0
    for i in range(len(contacts)):
        if reciever in contacts[i][0]:
            send = contacts[i][1];
            flag = 1;
            break;

    if (flag == 1):
        pywhatkit.sendwhats_image(send,r"C:\Users\Yamini\Desktop\yamini  clg\skcet logo.jpg","SKCET",15,True,5)
    else:
        speak("Sorry number not in contact list");

def watsapp():
    speak("Whom do u wanna send message");
    reciever = TakeCommand().lower();
    printData(reciever)
    speak("What message u wanna send")
    msg = TakeCommand().lower()
    printData(message)
    send = '+91 7358855843'
    flag = 0
    for i in range(len(contacts)):
        if reciever in contacts[i][0]:
            send = contacts[i][1];
            flag = 1;
            break;

    if (flag == 1):
        pywhatkit.sendwhatmsg_instantly(send, msg, 15, True, 3)

    else:
        speak("Sorry number not in contact list");

# TakeCommand()

#if __name__ == "__main__":
@eel.expose
def strat_fn():
    hour = datetime.datetime.now().hour
    if hour>=6 and hour<=12:
        speak("Good morning")
        if(hour<12):
            speak("Do you want to hear today's programming tip PLease say yes or no")
            ans=TakeCommand().lower()
            tips=["Make Your Fundamentals Clear","Learn By Doing, Practicing, and Not Just Reading","Code By Hand","Share, Teach, Discuss and Ask For Help","Use Online Resources","Take Breaks at regular intervals"," Learn to Use Debugger"]
            if(ans=='yes') :
                a=random.randint(0,6)
                tip="Today's programming tip is "+ tips[a]
                speak(tip)
            else:
                speak("sorry to disturb you")
    elif hour >=12 and hour<18:
        speak("Good Afternoon")
    elif hour >=18 and hour <24:
        speak("Good Evening")
    else:
        speak("Good Night")

    speak("may I know your name please")
    name = TakeCommand().lower()

    speak("pleased to meet you," + name)

    speak("Kitkat at your service. How can I help you?")
    

    while True:
        query = TakeCommand().lower()
        if 'time' in query:
            time_()
        elif 'date' in query:
            date_()
        elif 'wikipedia' in query:
            speak("searching..")
            query=query.replace('wikipedia','')
            result = wikipedia.summary(query,sentences=2)
            speak('According to wikipedia')
            printData(result)
            speak(result)
        
        elif 'search' in query:
            try:
                speak('Let me know the topic you want to surf')
                # chromepath = 'C:\Program Files\Google\Chrome\Application\chrome.exe %s'

                search_term = TakeCommand().lower()
                # wb.get(chromepath).open_new_tab(search+'.com')
                speak('here we go')
                wb.open('https://www.google.com/search?q='+search_term)
            except Exception as e:
                printData(e)

        elif 'youtube' in query or 'play' in query or 'videos' in query or 'video' in query:
            speak('It\'s youtube time,what\'s that you are curious about?')
            # chromepath = 'C:\Program Files\Google\Chrome\Application\chrome.exe %s'
            search_term = TakeCommand().lower()
            # wb.get(chromepath).open_new_tab(search+'.com')
            speak("playing now")
            pywhatkit.playonyt(search_term)
            # wb.open('https://www.youtube.com/results?search_query='+search_term)

        elif 'battery' in query or 'power' in query:
            cpu()
        
        elif 'joke' in query or 'laugh' in query:
            joke()
            speak("I can see you laughing...hahahahaha")
        
        elif 'go offline' in query or 'off' in query or 'stop' in query or'terminate' in query:
            speak('going offline.see you later,Dear'+name)
            quit()

        elif 'word' in query:
            speak('opening MS word...')
            # ms_word = r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs'
            ms_word = r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE"
            os.startfile(ms_word)
        elif 'write a note' in query or 'take notes' in query or 'notes' in query or 'note' in query:
            speak('I am ready to take notes.Let\'s start')
            notes = TakeCommand()
            file = open('notes.txt','w')
            file.write(notes)
            file.close()
            speak('And I\'m done taking notes')
        elif 'show notes' in query or 'show me the notes' in query or 'display' in query :
            speak('Here\'s what is noted')
            file = open('notes.txt','r')
            printData(file.read())
            speak(file.read())
        elif 'screenshot' in query or 'snap' in query:
            screenshot()
            speak('done with the screenshot')
        
        elif 'songs' in query or 'song' in query or 'play a song' in query or 'play songs' in query or 'play song' in query:
            video =r'C:\Users\Yamini\Desktop\videos'
            audio = r'C:\Users\Yamini\Desktop\memory card\entertinement\songs\telgu songs'
            speak("What do you prefer? Audio or Video")
            ans = (TakeCommand().lower())
            while(ans != 'audio' and ans != 'video'):
                speak("I could not understand you. Please Try again.")
                ans = (TakeCommand().lower())
        
            if 'audio' in ans:
                    songs_dir = audio
                    speak('Here you enjoy')
                    songs = os.listdir(songs_dir)
                    printData(songs)
            elif 'video' in ans:
                    songs_dir = video
                    printData('here you go')
                    songs = os.listdir(songs_dir)
                    printData(songs)
                
            speak("select a random number")
            rand = (TakeCommand().lower())
            while('number' not in rand and rand != 'random'):                       
                speak("I could not understand you. Please Try again.")          
                rand = (TakeCommand().lower())

            if 'number' in rand:
                    rand = int(rand.replace("number ",""))
                    os.startfile(os.path.join(songs_dir,songs[rand]))
                    continue                                                    
            elif 'random' in rand:
                    rand = random.randint(1,40)
                    os.startfile(os.path.join(songs_dir,songs[rand]))
                    continue

        elif 'remember' in query or 'remind' in query or 'keep in mind' in query:
            speak("what is it that you want me to remind?")
            memory = TakeCommand()
            speak("You asked me to remember that"+memory)
            remember = open('memory.txt','w')
            remember.write(memory)
            remember.close()

        elif 'do you remember anything' in query or 'reminder' in query:
            remember =open('memory.txt', 'r')
            speak("You asked me to remeber that"+remember.read())

        elif 'news' in query or 'happening' in query or 'happenings' in query:
            
            try:
                jsonObj = urlopen('https://newsapi.org/v2/everything?q=apple&from=2022-09-13&to=2022-09-13&sortBy=popularity&apiKey=89b29886052f4755a528fe7b14e1a88c')
                data = json.load(jsonObj)
                i = 1
                
                speak('here are some top news from the times of india')
                printData('''=================== TOP HEADLINES ================='''+ '\n')
                
                for item in data['articles']:
                    
                    printData(str(i) + '. ' + item['title'] + '\n')
                    printData(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
                    if i==6:
                         break
                    
            except Exception as e:
                printData(str(e)) 

        elif "where is" in query or 'locate' in query or 'location' in query or 'place' in query:
            query = query.replace("where is", "")
            location = query
            speak("here's the location you asked for")
            speak(location)
            wb.open("https://www.google.com/maps/place/" + location + "")

        elif "calculate" in query:
            
            app_id = "YTY9HW-97G2QJGVVP"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            printData("The answer is " + answer)
            speak("The answer is " + answer)

        elif "what is" in query or "who is" in query: 

            client = wolframalpha.Client("YTY9HW-97G2QJGVVP")
            res = client.query(query)
            
            try:
                printData (next(res.results).text)
                speak (next(res.results).text)
            except StopIteration:
                printData ("No results")

        elif 'log out' in query:
            os.system("shutdown -l")

        elif 'restart' in query:
            os.system("shutdown /r /t 1")

        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")

        elif 'what is love' and 'tell me about love' in query or 'love' in query:
            speak("It is 7th sense that destroy all other senses , "
            "And I think it is just a mere illusion , "
            "It is waste of time")

        elif 'SKCET' in query or 'sri krishna college' in query:
            speak('SRI KRISHNA COLLEGE OF ENGINEERING AND TECHNOLOGY, one of the top universities in south India, encourages innovation, Research and Development, and student empowerment through entrepreneurship to provide the best, most modern technical education possible.SRI KRISHNA COLLEGE OF ENGINEERING AND TECHNOLOGY is one of the premium institutions of south India, that imparts highest quality state-of-the-art technical education by providing impetus to innovation, Research and Development and empowering students with Entrepreneurship skills.')
        
        elif 'who is the HOD of information technology department' in query or 'head of department' in query:
            speak('It\'s our honourable mistress susila who is the pillar of the department.')

        elif 'principal' in query or 'Janet' in query:
            speak('Principal J. Janet.With 25 years of administrative and teaching expertise in engineering education leadership, Dr.J.Janet outlines an illustrious professional career. incredibly adaptable in the areas of academia, R&D, high-impact industry networking, and institutional visibility. Dr. J. Janet is exceptional in displaying her aura through articulate communication and versatile in cultivating and keeping high performance teams.')

        elif 'whatsapp web' in query:
            watsapp()

        def Introduction():
            speak("I am Kit-Kat 1.0 , Personal AI assistant , "
            "I am created by the team Techi Geeks , "
            "I can help you in various regards , "
            "I can search for you on the Internet , "
            "I can also grab definitions for you from wikipedia , "
            "In layman terms , I can try to make your life a bed of roses , "
            "Where you just have to command me , and I will do it for you , ")

        def Creator():
            speak("Techi Geek is an extra-ordinary team who has a passion for Robotics, Artificial Intelligence and Machine Learning ,"
            "they are very co-ordinated and supportive of each other ,"
            "If you are facing any problem regarding the 'kit-kat', they will be glad to help you ")
eel.start("index.html")