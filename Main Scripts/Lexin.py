import pyttsx3
import subprocess
import webbrowser
import smtplib
import json
import random
import operator
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import os
import sys
import time
import requests
import shutil
import winshell #pip install winshell
from playsound import playsound #pip install playsound
import platform #an-inbuilt module
from urllib.request import urlopen
from clint.textui import progress  #pip install clint
from ecapture import ecapture as ec  #pip install ecapture
from bs4 import BeautifulSoup #pip install urllib











































def Command():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold =  1
        audio = r.listen(source)
    try:
        cmd = r.recognize_google(audio)
        print('User: ' + cmd + '\n')

    except sr.UnknownValueError:
        speak('Sorry  I did not get that , Do you mind typing your command')
        cmd = input(str('User:'))


    return cmd



name = 'Lexin'
engine = pyttsx3.init()


client = wolframalpha.Client('9L5757-TQKUTWJGA2')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    print(name +':' + audio)
    engine.say(audio)
    engine.runAndWait()


def Welcome():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')

    if currentH >= 12 and currentH < 4:
        speak('Good Afternoon!')

    if currentH >= 18 and currentH !=0:
        speak('Good Evening!')

Welcome()
spk = ['how can i help you sir','do you need any help sir','Hi sir Lexin here,Ready to help you']
speak(random.choice(spk))


if __name__ == '__main__':

    while True:

        cmd = Command();
        cmd = cmd.lower()

        if 'open youtube' in cmd or 'youtube' in cmd or 'lexin open youtube' in cmd:
            speak('okay,opening youtube')
            webbrowser.open('www.youtube.com')
        elif 'i am fine how are you' in cmd or 'i am fine' in cmd or 'i am good' in cmd:
            speak("good , im too fine")
        elif 'lexin laugh' in cmd or 'lexin laugh once more' in cmd or 'lexin lol' in cmd or 'lol' in cmd or 'giggle' in cmd or 'laugh' in cmd or 'lol' in cmd  or 'laugh again' in cmd or 'laugh once again' in cmd or 'can you laugh again' in cmd or 'laugh once more' in cmd or 'entertain me' in cmd :
            speak("hahahahahaha")
        elif 'search' in cmd or 'google' in cmd or 'browse' in cmd or 'lexin search' in cmd or 'What is' in cmd:
              speak("sorry  ,what should i search for")
              search= Command()
              speak("ok searching for "+search)
              webbrowser.open("https://www.google.com/search?client=firefox-b-d&q= "+search)
        elif 'open google'in cmd or 'google' in cmd or 'lexin open google' in cmd:
            speak('okay,opening google')
            webbrowser.open('www.google.co.in')

        elif 'open gmail' in cmd or 'gmail' in cmd or 'lexin open gmail' in cmd:
            speak('okay,opening gmail')
            webbrowser.open('www.gmail.com')

        elif "whats up" in cmd or 'how are you' in cmd or 'hi lexin , how are you' in cmd:
            stMsgs = ['i am good as always','i am fine , thanks for asking' ,'it depends on your internet connection' , 'i am good']
            speak(random.choice(stMsgs))

        elif 'email' in cmd or ' send email' in cmd :
            speak('Who is the recipient? ')
            recipient = Command()

            if 'me' in recipient:
                try:
                    speak('What should I say? ')
                    content = Command()

                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("Your_Username", 'Your_Password')
                    server.sendmail('Your_Username', "Recipient_Username", content)
                    server.close()
                    speak('Email sent!')

                except:
                    speak('Sorry ! I am unable to send your message at this moment!')


        elif 'nothing' in cmd or 'die' in cmd or 'abort' in cmd or 'stop' in cmd or 'lexin stop' in cmd or 'close' in cmd or 'lexin close' in cmd or 'quit' in cmd:
            speak('okay')
            speak('Bye, have a good day.')
            sys.exit()

        
        elif 'bye' in cmd or 'good bye' in cmd or 'tata' in cmd or 'buh bye' in cmd or 'bye lexin' in cmd:
            speak('Bye, have a good day.')
            sys.exit()

        elif 'hey lexin how are you' in cmd   or 'lexin how was your day' in cmd or 'how was your day' in cmd or 'how is your day going' in cmd or 'how are you' in cmd:
            opt=[' i\'m good ','fine','good','i had a fine day']
            speak(random.choice(opt))

        elif "who created you" in cmd or "who is your creator" in cmd or "who was your creator" in cmd or "who is the owner of lexin" in cmd or 'by whom were you created' in cmd or 'who owns you' in cmd :
            speak('I am created by Skyno ')
                
        elif "i want to buy something" in cmd  or "i want to buy things in online"  in cmd or "i want to buy things online" in cmd or "i want to buy a" in cmd or "order in online" in cmd:
            # can add somemore
            speak('Do you want me to open in amazon,flipkart or snapdeal')
            choice = Command()
            if choice.lower() == 'amazon':
                webbrowser.open_new_tab('http:\\www.amazon.com')
                speak('a new tab of amazon have been opened')
            elif choice.lower()=='flipkart':
                webbrowser.open_new_tab('http:\\www.flipkart.com')
                speak('a new tab of flipkart have been opened')
            elif choice.lower()=='snapdeal':
                webbrowser.open_new_tab('http:\\www.snapdeal.com')

            else:
                speak('sorry i am not familiar with it')

        elif "what is your name" in cmd or "can i know your name please " in cmd or "Hey lexin what is your name" in cmd or 'hi  what is your name' in cmd or ' can i know your name' in cmd or ' hey what is your name' in cmd:

               speak('MY name is lexin')
               
        elif"What is your age " in cmd or "can i know your age please " in cmd or "Hey lexin what is your age" in cmd or 'age' in cmd or 'can i know your age' in cmd or ' hi can i know your age' in cmd or ' hey what is your age' in cmd:
                speak(" i was just born")
                
        elif "where is your home" in cmd or "where were you born " in cmd or "where do you live " in cmd or 'where is your house' in cmd or  'in which place do you live' in cmd or 'where is your house located in ' in cmd or ' where is your home located in' in cmd or 'what is your address' in cmd or ' what is your house address' in cmd or 'what is your home addess' in cmd:
               speak("i Live in your internet connection")
               
        elif 'what is your job' in cmd or 'what is the job you are doing' in cmd or 'can i what work are you doing' in cmd or 'can you tell me what\'s your work' in cmd or 'are you carrying on any job' in cmd :
                sts=['i\'m working as a voice assistant to you ' , 'i\'m commited to job as a assistant to help you']#you can also change these statements if it's not good
                speak(random.choice(sts))
        elif 'who are you'in cmd or 'who the heck are you'in cmd:
            speak("I am Lexin , your voice assistant here to assist you")
            
        elif 'hey ,whats up' in cmd or 'how are you' in cmd:
            speak("i am good as always")
            
        elif 'turn on game mode'in cmd or 'play a game'in cmd or 'game'in cmd or 'i want to play a game' in cmd or 'game' in cmd:
            speak("ok turning on game mode")
            speak("what game do you want to play")
            speak("choose either flappy bird , Ping pong")
            game = Command()
            game = game.lower()
            if (game == 'flappy bird' or game == 'flappybird'):
                  speak("ok , opening flappy bird")
                  os.system('main.py')
                  
            elif(game == 'pingpong' or game == 'ping pong'):
                  speak("ok opening pingpong")
                  speak('do you want to play practice mode or do you want to play with the computer')
                  speak("enter either pvc or pm in the console panel , using keyboard")
                  pp = Command()
                  pp = pp.lower()
                  if (pp == 'pvc'):
                   speak("ok , opening play versus computer mode")
                   webbrowser.open("https://editor.p5js.org/jeevansuresh2508/full/XNNqjuh4U")
                   
                  elif(pp =='pm'):
                   speak("ok , opening practice mode")
                   webbrowser.open("https://editor.p5js.org/jeevansuresh2508/full/eqSkeFb71")
                   
                  else:
                   speak("oops ! , i am not sure about it")
                   speak("enter either pvc or pm")
            else :
                  speak("that's an invalid choice")
                  
        elif "how do i change your voice" in cmd or "change your voice" in cmd or "change voice" in cmd or "voice change in cmd" in cmd:
             speak(" i am sorry about it , but my voice is fine")
             
        elif 'are you married' in cmd or 'do you have a girlfriend' in cmd:
            speak(" i am married to my work")
            
        elif "can you get me to instagram" in cmd or "i want to make a post in my instagram account" in cmd or "lexin take me to instagram" in cmd or "can you please take me to instagram" in cmd:
            speak("OK, taking you to instagram.com")
            speak("Please wait for seconds")
            webbrowser.open_new_tab("https://www.instagram.com/")
            
        elif "can you take me to facebook" in cmd or "i want to make a status in facebook" in cmd or "lexin take me to facebook" in cmd :
            speak("opening facebook.com")
            speak("Please wait for seconds")
            
            webbrowser.open_new_tab("https://www.facebook.com/")
        elif "can you recommend the best programming language to be learnt" in cmd or "can you guide me which is the best programming language" in cmd or "which is the best programming language " in cmd or "Trending programming languages" in cmd:
            speak("i will recommend you to learn Python as it is the most user friendly and easiest programming language which gives more job oppurtunities")
            speak("or else you can learn java script, swift, java, c, c++ or php")

        elif"search youtube" in cmd or "play a  song on youtube"in cmd or "play a song in youtube" in cmd or"search youtube" in cmd or "search for a video in youtube" in cmd or "search a video"  in cmd or "play a video on youtube" in cmd:
            speak("alright what song do i need to search for")
            song = Command()
            webbrowser.open("https://www.youtube.com/results?search_query="+song)

        elif"play another music" in cmd or "another music" in cmd:
            playsound("music.mp3")
            
        elif"play music" in cmd or "i want to hear some music" in cmd or "play some songs" in cmd or "play a song" in cmd or "sing a song" in cmd:
            webbrowser.open("https://www.youtube.com/watch?v=1M8ZfDOURw0")
            
        elif "open whatsapp" in cmd or  "whatsapp" in cmd:
            speak("alright opening whatsapp")
            webbrowser.open("https://web.whatsapp.com")
            
        elif "open notepad" in cmd or "notepad" in cmd or "please open notepad" in cmd :
            subprocess.Popen("c:\\Windows\\System32\\notepad.exe")
            
        elif "open python" in cmd or  "python" in cmd or  "please open python" in cmd : 
            subprocess.Popen("c:\\Windows\\System32\\python.exe")

        elif "open wordpad" in cmd or"wordpad"  in cmd or "please open wordpad" in cmd:
            subprocess.Popen("c:\\Windows\\System32\\wordpad.exe")
            
        elif "tell me a joke" in cmd or  "please tell me a joke" in cmd or  "crack a joke" in cmd:
            joke = ["Hey Rachyl, do you remember me? Person 2: Wrong number. Person 1: What’s your number then?","Mom: How make chicken Daughter: What? Mom: Where buy chicken Daughter: Mom, this isn’t Google. Mom: Avocado"]
            speak(random.choice(joke))
        elif 'wikipedia' in cmd:
            try:
                speak('Searching Wikipedia...')
                query = cmd.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences = 3)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except:
                if "what is wikipedia" in cmd or "wikipedia" in cmd:
                    results = wikipedia.summary(cmd,sentences=3)
                    print(results)
                    speak(results)
                else:
                    speak("Sorry there is no page in Wikipedia named " + cmd.replace("wikipedia",""))
                    speak("Do you want me to show results in google for your query")
                    resp=Command()
                    if resp=="yes":
                        webbrowser.open_new_tab("www.google.com//" + cmd)
                    elif resp=="no":
                        speak("Thank you")
                    else:
                        speak("Please try within yes or no")
                        speak("To try again try saying open" + cmd)
                '''No idea if this is correct I adde this because If there is no page for the command given it is resulting as an error'''


        elif 'open stackoverflow' in cmd:
            speak("Here you go to Stack Over flow.Happy coding")
            webbrowser.open("stackoverflow.com")

        elif "what's your name" in cmd or "What is your name" in cmd:
            speak("My friends call me")
            speak("Lexin")
            print("My friends call me Lexin")
            
        elif "calculate" in cmd:

            app_id = "Wolframalpha api id"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer)
            
        elif "who i am" in cmd or "who am i" in cmd:
            speak("Since you talk In English, you must be an human ig ?")
            
        elif "why you came to world" in cmd:
            speak("Thanks to those who invented me , further it is a secret")
            
        elif 'news' in cmd or "what is the news" in cmd or "tell me the news today" in cmd or "can you tell me the news today" in cmd :

            try:
                jsonObj = urlopen('''https://newsapi.org / v1 / articles?source = the-times-of-india&sortBy = top&apiKey =\\times of India Api key\\''')
                data = json.load(jsonObj)
                i = 1


                speak('here are some top news from the times of india')
                print('''=============== TIMES OF INDIA ============'''+ '\n')

                for item in data['articles']:

                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
            except Exception as e:

                print(str(e))

        elif 'shutdown system' in cmd or "shut down my laptop" in cmd :
                speak("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call("shutdown /s /t 1")

        elif 'empty recycle bin' in cmd or "clear my bin" in cmd or "clear my recycle bin" in cmd:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin Recycled")

        elif "don't listen" in cmd or "stop listening" in cmd or "pause" in cmd :
            speak("for how much time you want to stop Lexinfrom listening commands")
            a = int(Command())
            time.sleep(a)
            print(a)

        elif "where is" in cmd:
            query = cmd
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl/maps/place/" + location + "")
            
        elif "open  " in cmd or "take a photo" in cmd or "take photo" in cmd or " take a pic" in cmd:
            ec.capture(0, "Jarvis_Camera ", "img.jpg")

        elif "restart" in cmd or "restart my laptop" in cmd:
            subprocess.call(["shutdown", "/r"])

        elif "hibernate" in cmd or "sleep" in cmd:
            speak("Hibernating")
            subprocess.call("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        elif "log off" in cmd or "sign out" in cmd:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])

        elif "write a note" in cmd:
            speak("What should i write, sir")
            note = Command()
            file = open('jarvis.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = Command()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
                ##Error
            else:
                file.write(note)

        elif "show note" in cmd:
            speak("Showing Notes")
            file = open("jarvis.txt", "r")
            print(file.read())
            speak(file.read(6))
            
        elif "take me to twitter" in cmd or "can you take me to twitter" in cmd or "please get me to twitter" in cmd :
           speak("Ok taking you to twitter.com")
           webbrowser.open_new_tab("https://twitter.com/login?lang=en")
           
        elif "please take me to google" in cmd or "can you take me to google" in cmd or "i want to browse in google" in cmd:
            speak("Taking you to google.com")
            webbrowser.open_new_tab("https://www.google.com/")
            
        elif "move forward" in cmd or "go forward" in cmd:
            speak("Command Recognized , Moving forward")
            webbrowser.open("192.168.0.109/forward")
            
        elif "move backward" in cmd or "go backward" in cmd:
            speak("Command Recognized , Moving Backward")
            webbrowser.open("192.168.0.109/backward")
            
        elif "turn towards left" in cmd or "turn left" in cmd or "move left" in cmd:
            speak("command recognized,moving towards left")
            webbrowser.open("192.168.0.109/left")
            
        elif "turn towards right" in cmd or "turn right" in cmd or "move right" in cmd:
            speak("command recognized, moving towards right")
            webbrowser.open("192.168.0.109/right")
            
        elif "rotate rightside" in cmd or "rotate towards right" in cmd or "rotate right" in cmd:
            speak("command recognized , rotating towards right")
            webbrowser.open("192.168.0.109/turnright")
            
        elif "rotate leftside" in cmd or "rotate towards left" in cmd or "rotate left" in cmd:
            speak("command recognized, rotating towards left")
            webbrowser.open("192.168.0.109/turnleft")

        elif "rotate" in cmd:
            speak("command recognized , rotating")
            webbrowser.open("192.168.0.109/rotate")
            
        elif "stop" in cmd:
            speak("command recognized , stopping")
            webbrowser.open("192.168.0.109/stp")


        elif "turn on light" in cmd:
            speak("command recognized, turning on LED")
            webbrowser.open("http://192.168.0.104/gpio/1")   
        elif "turn off light" in cmd:
            speak("command recognized,turning off LED")
            webbrowser.open("http://192.168.0.104/gpio/0") 
            

        elif "open command prompt" in cmd or "open commandprompt" in cmd or "open cmd" in cmd or "cmd" in cmd or "command prompt" in cmd:
            subprocess.call('cmd.exe')
            
            


        elif "why am i single" in cmd: 
            speak("Probably because you are too nice") 
        elif "are you single" in cmd: 
            speak("unfortunately im a single Motherfucker too, yep I know you are single")
        elif "no" in cmd or "nope" in cmd:
            speak("alright cool, Bye for Now then")
    
                                               
        
        else:
            cmd = cmd
            speak('Searching...')
            try:
                try:
                 res = client.query(cmd)
                 results = next(res.results).text
                 speak(results)
                    
                except:
                 results = wikipedia.summary(cmd, sentences=2)
                 speak('According to Wikipedia')
                 speak(results)
        
            except:
                speak("whoops, that wasnt supposed to happen")
                speak("I am not quite sure about that, anything else I can help you with ?")
        
        speak('anything ?')
