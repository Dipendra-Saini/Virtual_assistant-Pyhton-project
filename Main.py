import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pyjokes
import randfacts
import pyautogui as pg
import time
from playsound import playsound
from win32com.client import Dispatch
import requests
from ss import *
import json

li = []
class virtual_assistant:
    def __init__(self):
        self.Assistant = pyttsx3.init('sapi5')
        self.voice = self.Assistant.getProperty('voices')
        self.Assistant.setProperty('voices',self.voice[1].id)
        self.Assistant.setProperty('rate', 180)

    def speak(self,audio):
        self.Assistant.say(audio)
        self.Assistant.runAndWait()

    def wishme(self):
        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour <12:
            self.speak("Good Morning Sir")
        elif hour>=12 and hour<18:
            self.speak("Good Afternoon Sir")
        else:
            self.speak("Good Evening Sir")
        self.speak("I am your Personal Assistant. How may i help you Sir.")

    def take_command(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening.......")
            playsound('C:\\Users\\DELL\\Pictures\\sound\\ring.mp3')
            # r.energy_threshold = 8000
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            self.speak("Recognizing.............. ")
            query = r.recognize_google(audio,language = 'en-in')
            print(f"You said : {query}\n")
        except Exception as e:
            self.speak("Sorry Sir!!")
            return "None"
        return query
    
    def news(self,data):
        for i in range(5):
            li.append("Number "+str(i+1) +" "+ data["articles"][i]["title"]+".")
        return li

    def follow_command(self,command):
        if "hello" in command:
            self.speak("Hello Sir How are you Sir ?")

        elif 'i am good' in command:
            self.speak("My pleasure to hear this Sir. How may i help you Sir.")

        elif "what about you" in command:
            self.speak("I am also having a good day Sir.")

        elif "tell me your name" in command:
            self.speak("I am Your Personal Assistant Sir")

        elif "who are you" in command:
            self.speak("I am Your Personal Assistant Sir")

        elif "time" in command:
            time_is = datetime.datetime.now().strftime("%H:%M:%S")
            self.speak(f"Sir the time is : {time_is}")
        
        elif 'date' in command:
            date_is = datetime.date.today().strftime("%B %d, %Y")
            self.speak(f"Sir Today Date  is : {date_is}")

        elif 'day' in command:
            d1 = datetime.date.today().strftime("%d %m %Y")
            day_name= ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']
            day = datetime.datetime.strptime(d1, '%d %m %Y').weekday()
            self.speak(f"Sir Today  is : {day_name[day]}")  

        elif "information" in command:
            self.speak("You need information related to which topic : ")
            next_command = self.take_command().lower()
            self.speak("Searching..........")
            result = wikipedia.summary(next_command,sentences = 2)
            print(result)
            self.speak(result)

        elif "open youtube" in command:
            self.speak("Opening Youtube Sir..........")
            webbrowser.open("https://www.youtube.com/")

        elif "open google" in command:
            self.speak("Opening Google Sir..........")
            webbrowser.open("https://www.google.com/")

        elif "open stack overflow" in command:
            self.speak("Opening Stack overflow Sir..........")
            webbrowser.open("https://www.stackoverflow.com/")

        elif "open vs code" in command:
            self.speak("Opening vs code Sir..........")
            path_file = "D:\\files\\Microsoft VS Code\\Code.exe"
            os.startfile(path_file)

        elif "play music" in command:
            self.speak("Playing music Sir..........")
            music_path = 'C:\\Users\\DELL\\Music'
            songs = os.listdir(music_path)
            os.startfile(os.path.join(music_path,songs[1])) 

        elif "play video" in command:
            self.speak("Playing video Sir..........")
            video_path = 'C:\\Users\\DELL\\Videos\\YT shorts'
            videos = os.listdir(video_path)
            os.startfile(os.path.join(video_path,videos[0]))

        elif 'fact' in command:
            fact_gen = randfacts.getFact()
            print(fact_gen)
            self.speak("Did you  know that ,")
            self.speak(fact_gen)

        elif 'joke' in command:
            self.speak("Sure Sir, Get ready for some chukles")
            joke_gen = pyjokes.get_joke(language="en", category="neutral")
            print(joke_gen)
            self.speak(joke_gen)

        elif 'news' in command:
            url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=54b0b263d9cd48a2a6c732a299f28df5"
            data = requests.get(url).json()
            try:
                obj = self.news(data)
                self.speak("The request was accepted ")
                self.speak("Top news of the day")
                for i in range(len(obj)):
                    print(obj[i])
                    self.speak(obj[i])
                
            except Exception as e:
                self.speak("Sorry! the request was not accepted")

        elif 'weather' in command:
            self.speak("Weather in phagwara is :")
            complete_url = "http://api.openweathermap.org/data/2.5/weather?appid=d9f7204fa8b25b7849b0a5b7ede29404&q=Phagwara"
            response = requests.get(complete_url)
            x = response.json()
            y = x["main"]
            z = x["weather"]
            self.speak("Temperature (in celcius) : ")
            self.speak(int(y["temp"])-273)
            self.speak("Atmospheric pressure (in hPa unit) : ")
            self.speak(y["pressure"])
            self.speak("Humidity (in percentage) : ")
            self.speak(y["humidity"])
            self.speak("Description : ")
            self.speak(z[0]["description"])

        elif 'send message' in command:
            self.speak("Sending What's app message.........")
            webbrowser.open("https://web.whatsapp.com/")
            time.sleep(8)
            pg.click(300,183)
            pg.typewrite('DIP')
            time.sleep(2)
            pg.click(320,325)
            time.sleep(2)
            pg.typewrite("Hello ! What's up")
            time.sleep(2)
            pg.click(1684,977)

        elif 'send mail' in command:
            self.speak("Sending Mail .........")
            webbrowser.open("https://mail.google.com/")
            time.sleep(10)
            pg.click(35,175)
            time.sleep(2)
            pg.typewrite("dipudipendrasingh23@gmail.com")
            time.sleep(5)
            pg.click(1700,520)
            time.sleep(1)
            pg.typewrite("Nope")
            time.sleep(3)
            pg.click(1300,600)
            time.sleep(1)
            pg.typewrite("Hello How are you")
            time.sleep(2)
            pg.click(1300,1000)

        elif 'shut down' in command:
            os.system('shutdown -s')

        elif 'exit' in command:
            return False
        elif 'quit' in command:
            return False
        elif 'bye' in command:
            return False
        elif 'stop' in command:
            return False
        else:
            self.speak("Say it again Sir")

def main():
    va = virtual_assistant()
    va.wishme()
    while True:

        command = va.take_command().lower()
        feed=va.follow_command(command)
        if feed is False:
            break
    va.speak("Thank you Sir, It was nice interaction with you !!")

if __name__ == "__main__":
    main()
