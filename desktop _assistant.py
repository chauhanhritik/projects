from datetime import datetime
import playsound  #for music
import os
import pyaudio
import speech_recognition as sr   #sr works as your access later in the code for speech recognition
import wikipedia
import pyttsx3                    #text to speech
import webbrowser
import smtplib                    #send mail
# you will have to pip install speechrecognition, pyaudio, wikipedia,pyttsx3
engine = pyttsx3.init('sapi5')      #set ting engine as obj
voices = engine.getProperty('voices')    #properties of voices
engine.setProperty('voices',voices[0].id)
# engine.runAndwait()

def speakup(text):
    engine.say(text)
    engine.runAndWait()

def greet_me():      #TO GREET  THE USER BASED ON THE TIME
    # now = datetime.now()
    morning_time = "00:00:00"
    afternoon_time = "12:00:01"
    evening_time = "16:00:01"
    night_time = "20:00:01"
    current_time = datetime.strftime(datetime.now(), "%H:%M:%S")
    print(f"Time : {current_time}") 
    if (current_time < morning_time) and (current_time > night_time):
        print("Good Night Sir  ")
        a = 'good night sir'
    elif (current_time < night_time) and (current_time > evening_time):
        print("Good Evening Sir  ")
        a = 'good evening sir'
    elif (current_time < evening_time) and (current_time >afternoon_time):
        print("Good Afternoon Sir  ")
        a = 'good afternoon sir'
    else:
        a = 'good morning sir'
        print("Good Morning Sir  ")
    return a

def task_():         #take input from user audio
    print("please speak")
    t = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....:")
        audio = t.listen(source)
    try :
        print("Processing command....")
        tk = t.recognize_google(audio,language = 'en-in')
        print("task =  ", str(tk))

    except Exception as e:
        print("Couldn't get that. Please speak again.")
        tk = None
    return tk

def search(result):
    speakup('searching the database.....')
    result = wikipedia.summary(result, sentences = 2)   #we shall take only two first lines
    print(result)
    speakup(result)
    
#main section of the program
print("Initialising your assistant....")
speakup("Initialising your assistant")

greeting = greet_me()           #GREET THE USER
speakup(greeting)               #greet with audio
print("How may I help you today Sir ?  \n")
speakup(" I am you virtual assistant.")
speakup("How may i help you ? Would  you like to view the menu? or you may just give me a command as per your convenience.")
while True:
    
    task = task_()  # to input task by voice
    if 'who is' in task.lower() or 'wikipedia' in task.lower() or 'info' in task.lower() or 'data' in task.lower():   #search about someone on wikipedia
        if 'who is' in task.lower():
            task = task.replace('who is '," ")    #removing the word from task so that we can search it easily
        elif 'wikipedia' in task.lower():
             task = task.replace('wikipedia'," ")
        elif  'info' in task.lower():
            task = task.replace('info'," ")
        else:
            task = task.replace('data'," ")
        search(task)
    elif 'menu' in task.lower():
        print("1. To find iformation about someone or something speak- -(who is// wikipedia// info // data)  NAME -")
        print("2. To open google  speak - google -")
        print("3. To open youtube  speak - youtube -")
        print("4. To open youtube  speak - youtube -")
        print("5. To open something educational  speak - education -")
        print("6. To play songs  speak - music -")    
        print("7. To watch movies  speak - movies -")

    elif 'google' in task.lower():  #open google 
        url = 'google.com'
        path_chrome = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe %s" #--profile-directory="Default"
        webbrowser.get(path_chrome).open(url)

    elif "youtube" in task.lower():  #open youtube
        url = 'youtube.com'
        path_chrome = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe %s" #--profile-directory="Default"
        webbrowser.get(path_chrome).open(url)

    elif 'education' in task.lower():  #open udemy 
        url = 'udemy.com'
        path_chrome = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe %s" #--profile-directory="Default"
        webbrowser.get(path_chrome).open(url)

    elif 'mail' in task.lower():  #send mail 
        to = '******.pottekat@gmail.com'
        to1 = 'naturalgamer2904@gmail.com'
        content = task_()
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.login('naturalgamer2904@gmail.com','********')
        # for i in range(0,1):
        server.sendmail('naturalgamer2904@gmail.com',to1,content)
        server.close()

    elif 'song' in task.lower() or 'music' in task.lower():  #play song 
        path = 'D:\\phn\\music (1)'
        songs = os.listdir(path)
        print(songs)
        a = input('enter the name : ')
        # os.startfile(os.path.join(path, songs[a]))
        playsound.playsound(f'D:\\phn\\music (1)\\{a}.mp3')

    elif 'movie' in task.lower() or 'movies' in task.lower():  #open movies in the directory 
        path = 'D:\\series\\Dragonball Z Remastered Seasons 1-9 + Movies Pack\\Dragon Ball Z Movies Pack [Triple-Audio]'
        movies = os.listdir(path)
        print(movies)
        a = int(input('enter the index : '))
        os.startfile(os.path.join(path, movies[a]))
    elif 'exit' in task.lower():
        break
    else:
        print("Invalid command. Please try again")
        speakup("Invalid command. Please try again")
    print("to exit speak - exit -")
    print("to continue - just give the next command -")
    task = task_()    
    
c = input()