from distutils.util import strtobool
from email import message
from tkinter.messagebox import YES
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
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



engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
wolframalpha_app_id = r'YTY9HW-97G2QJGVVP'
api_key = r'067c76dbe8caac93fa25cdf648abf7a5'
base_url = "http://api.openweathermap.org/data/2.5/weather?"


# def sendEmail(to,content):
#     server = smtplib.SMTP('smtp.gmail.com',587)
#     server.ehlo()
#     server.starttls()
#     #my acc
#     server.login('yamujawa3@gmail.com','yamini@1406')
#     server.sendmail('yamujawa3@gmail.com',to,content)
#     server.close()

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
        # r.adjust_for_ambient_noise(source)
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-us')
        print(query)
    except Exception as e:
        print(e)
        print("Say that again please")
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

contacts = [['yalmugi','+91 7358855843'],['vishal', '+91 8667748941'], ['kumar', '+91 9087395904'], ['abinash', '+91 8220928970'], ['aishu','+91 73057 05570']]

def watsapp_image():
    speak("Whom do u wanna send message");
    reciever = TakeCommand().lower();
    send = '+91 7358855843'

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
    #pywhatkit.sendwhatmsg_instantly('+91 9843491240', 'hello daddy', 15, True, 3)

    speak("Whom do u wanna send message");
    reciever = TakeCommand().lower();
    print(reciever)
    speak("What message u wanna send")
    msg = TakeCommand().lower()
    print(message)
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

def Introduction():
            print("I am Kit-Kat 1.0 , Personal AI assistant , "
            "I am created by the team Techi Geeks , "
            "I can help you in various regards , "
            "I can search for you on the Internet , "
            "I can also grab definitions for you from wikipedia , "
            "In layman terms , I can try to make your life a bed of roses , "
            "Where you just have to command me , and I will do it for you  ")
            speak("I am Kit-Kat 1.0 , Personal AI assistant , "
            "I am created by the team Techi Geeks , "
            "I can help you in various regards , "
            "I can search for you on the Internet , "
            "I can also grab definitions for you from wikipedia , "
            "In layman terms , I can try to make your life a bed of roses , "
            "Where you just have to command me , and I will do it for you ")

def Creator():
        print("Techi Geek is an extra-ordinary team who has a passion for Robotics, Artificial Intelligence and Machine Learning ,"
        "they are very co-ordinated and supportive of each other ,"
        "If you are facing any problem regarding the 'kit-kat', they will be glad to help you ")
        speak("Techi Geek is an extra-ordinary team who has a passion for Robotics, Artificial Intelligence and Machine Learning ,"
        "they are very co-ordinated and supportive of each other ,"
        "If you are facing any problem regarding the 'kit-kat', they will be glad to help you ")
# TakeCommand()

if __name__ == "__main__":
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
    print("pleased to meet you," + name)
    speak("pleased to meet you," + name)

    print("KITKAT at your service. How can I help you?")
    speak("KITKAT at your service. How can I help you?")
    

    while True:
        query = TakeCommand().lower()
        if 'time' in query:
            time_()
            
        elif 'date' in query:
            date_()
        # elif 'wikipedia' in query:
        #     speak("searching..")
        #     query=query.replace('wikipedia','')
        #     result = wikipedia.summary(query,sentences=2)
        #     speak('According to wikipedia')
        #     print(result)
        #     speak(result)
        
        elif 'search' in query:
            try:
                speak('Let me know the topic you want to surf')
                # chromepath = 'C:\Program Files\Google\Chrome\Application\chrome.exe %s'

                search_term = TakeCommand().lower()
                # wb.get(chromepath).open_new_tab(search+'.com')
                speak('here we go')
                wb.open('https://www.google.com/search?q='+search_term)
            except Exception as e:
                print(e)

        elif 'youtube' in query or 'play' in query or 'videos' in query or 'video' in query:
            speak('It\'s youtube time,what\'s that you are curious about?')
            # chromepath = 'C:\Program Files\Google\Chrome\Application\chrome.exe %s'
            search_term = TakeCommand().lower()
            # wb.get(chromepath).open_new_tab(search+'.com')
            speak("playing now")
            wb.open('https://www.youtube.com/results?search_query='+search_term)

        elif 'battery' in query or 'power' in query:
            cpu()
        elif 'i love you' in query or 'love' in query :
            lst=['Yeah, thanks. I love myself too.','takes out pepper spray','I love you too, but as a friend.','Forget it, you know nothing about me!','I am shutting my eyes tight so everything goes black.','And I’m calling the police.','I mean...who doesn’t love me?']
            a=random.randint(0,len(lst)-2)
            speak(lst[a])
            print(lst[a])

        
        elif 'joke' in query or 'laugh' in query:
            joke()
            print("I can see you laughing...hahahahaha")
            speak("I can see you laughing...hahahahaha")
        
        elif 'go offline' in query or 'off' in query or 'stop' in query or'terminate' in query:
            print('going offline.see you later,Dear'+name)
            #print('KITKAT is Sorry for causing the inconvienience. Kitkat will be back with a bang . kitkat 2 point o will see u soon')
            
            speak('going offline.see you later,Dear'+name)
            #speak('KITKAT is Sorry for causing the inconvienience. Kitkat will be back with a bang . kitkat 2 point o will see u soon')
            quit()

        elif 'word' in query:
            speak('opening MS word...')
            # ms_word = r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs'
            ms_word = r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE"
            os.startfile(ms_word)
        elif 'write a note' in query or 'take notes' in query:
            speak('I am ready to take notes.Let\'s start')
            notes = TakeCommand()
            file = open('notes.txt','w')
            file.write(notes)
            file.close()
            speak('And I\'m done taking notes')
        elif 'show notes' in query or 'show me the notes' in query or 'display' in query :
            speak('Here\'s what is noted')
            file = open('notes.txt','r')
            print(file.read())
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
                    print(songs)
            elif 'video' in ans:
                    songs_dir = video
                    print('here you go')
                    songs = os.listdir(songs_dir)
                    print(songs)
                
            speak("select a random number")
            rand = (TakeCommand().lower())
            while('number' not in rand and rand != 'random'):                       #used while loop to keep the jarvis on the speak command untill req. command is given.
                speak("I could not understand you. Please Try again.")          #first used 'rand' before while then again after, so that rand is already defind, and Input is taken and then checked if it is according to reuirement or not. And if it is not which means while loop is true, then commands under 'while loop' will execute untill desired approach.As it will again ask the user for input in the same block. 
                rand = (TakeCommand().lower())

            if 'number' in rand:
                    rand = int(rand.replace("number ",""))
                    os.startfile(os.path.join(songs_dir,songs[rand]))
                    continue                                                    #'continue' is used, so that after executing the commands in 'if' or 'elif' block, it will move to the next part of execution (or code). but in this case as this is the last execution of related function then it will move to the next function (i.e. in this code, it will be TakeCommand() )
            elif 'random' in rand:
                    rand = random.randint(1,40)
                    os.startfile(os.path.join(songs_dir,songs[rand]))
                    continue
        
        elif 'do you remember anything' in query or 'reminder' in query:
            remember =open('memory.txt', 'r')
            speak("You asked me to remeber that"+remember.read())

        elif 'remember' in query or 'remind' in query or 'keep in mind' in query:
            speak("what is it that you want me to remind?")
            memory = TakeCommand()
            speak("You asked me to remember that"+memory)
            remember = open('memory.txt','w')
            remember.write(memory)
            remember.close()
        
        elif 'introduce' in query or 'who is kitkat' in query:
            Introduction()
        
        elif 'creator' in query or 'founder' in query or 'owner' in query:
            Creator()

        elif 'news' in query or 'happening' in query or 'happenings' in query:
            
            try:
                jsonObj = urlopen('https://newsapi.org/v2/everything?q=apple&from=2022-09-13&to=2022-09-13&sortBy=popularity&apiKey=89b29886052f4755a528fe7b14e1a88c')
                data = json.load(jsonObj)
                i = 1
                
                speak('here are some top news from the times of india')
                print('''=================== TOP HEADLINES ================='''+ '\n')
                
                for item in data['articles']:
                    
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
                    if i==6:
                         break
                    
            except Exception as e:
                print(str(e)) 

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
            print("The answer is " + answer)
            speak("The answer is " + answer)

        elif "what is" in query or "who is" in query: 

            client = wolframalpha.Client("YTY9HW-97G2QJGVVP")
            res = client.query(query)
            
            try:
                print (next(res.results).text)
                speak (next(res.results).text)
            except StopIteration:
                print ("No results")

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

        elif 'principal' in query or 'Janet' in query:
            speak('Principal J. Janet.With 25 years of administrative and teaching expertise in engineering education leadership, Dr.J.Janet outlines an illustrious professional career. incredibly adaptable in the areas of academia, R&D, high-impact industry networking, and institutional visibility. Dr. J. Janet is exceptional in displaying her aura through articulate communication and versatile in cultivating and keeping high performance teams.')
            print('Principal J. Janet.With 25 years of administrative and teaching expertise in engineering education leadership, Dr.J.Janet outlines an illustrious professional career. incredibly adaptable in the areas of academia, R&D, high-impact industry networking, and institutional visibility. Dr. J. Janet is exceptional in displaying her aura through articulate communication and versatile in cultivating and keeping high performance teams.')

        elif 'college' in query or 'sri krishna college' in query:
            speak('SRI KRISHNA COLLEGE OF ENGINEERING AND TECHNOLOGY, one of the top universities in south India, encourages innovation, Research and Development, and student empowerment through entrepreneurship to provide the best, most modern technical education possible.SRI KRISHNA COLLEGE OF ENGINEERING AND TECHNOLOGY is one of the premium institutions of south India, that imparts highest quality state-of-the-art technical education by providing impetus to innovation, Research and Development and empowering students with Entrepreneurship skills.')
            print('SRI KRISHNA COLLEGE OF ENGINEERING AND TECHNOLOGY, one of the top universities in south India, encourages innovation, Research and Development, and student empowerment through entrepreneurship to provide the best, most modern technical education possible.SRI KRISHNA COLLEGE OF ENGINEERING AND TECHNOLOGY is one of the premium institutions of south India, that imparts highest quality state-of-the-art technical education by providing impetus to innovation, Research and Development and empowering students with Entrepreneurship skills.')


        elif 'who is the HOD of information technology department' in query or 'head of the department' in query:
            speak('It\'s our honourable mistress susila who is the pillar of the department.')
            print('It\'s our honourable mistress susila who is the pillar of the department.')

        

        elif 'whatsapp web' in query or 'whatsapp' in query:
            watsapp()
        
        elif 'image' in query or 'whatsapp image' in query:
            watsapp_image()


        
                
        # elif "weather" in query: 
			
		# 	# Google Open weather website 
		# 	# to get API of Open weather
        #     api_key = "067c76dbe8caac93fa25cdf648abf7a5"
        #     base_url = "http://api.openweathermap.org/data /2.5/weather?q="
        #     speak(" City name ")
        #     print("City name : ")
        #     city_name = TakeCommand()
        #     complete_url = base_url + "appid =" + api_key + "&q =" + city_name
        #     response = requests.get(complete_url)
        #     x = response.json()
            
        #     if x["cod"] != "404":
        #         y = x["main"]
        #         current_temperature = y["temp"]
        #         current_pressure = y["pressure"]
        #         current_humidiy = y["humidity"]
        #         z = x["weather"]
        #         weather_description = z[0]["description"]
        #         print(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description))
                
        #     else:
        #         speak(" City Not Found ") 

