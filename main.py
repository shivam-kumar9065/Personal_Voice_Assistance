import requests
from online_ops import find_my_ip, get_latest_news, get_random_advice, get_random_joke, get_trending_movies, \
    get_weather_report, play_on_youtube, search_on_google, search_on_wikipedia, send_email, send_whatsapp_message, search, search_on_googlemaps
import pyttsx3
import speech_recognition as sr
from decouple import config
from datetime import datetime
from os_ops import open_calculator, open_camera, open_cmd, open_notepad, open_discord, shut_down, re_start, sys_info, get_cpu_temp, get_ram_usage, install, stop_music, pause_music, open_microsoftEdge, telegram,  excel, power_point, word, power_BI
from random import choice
from utils import opening_text
from pprint import pprint
from arthmetic import add, sub
import os
import pywhatkit

USERNAME = config('USER')
BOTNAME = config('BOTNAME')

engine = pyttsx3.init('sapi5')

# Set Rate
engine.setProperty('rate', 180)

# Set Volume
engine.setProperty('volume', 1.0)

# Set Voice (Female)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


# Text to Speech Conversion
def speak(text):
    """Used to speak whatever text is passed to it"""

    engine.say(text)
    engine.runAndWait()


# Greet the user
def greet_user():
    """Greets the user according to the time"""

    hour = datetime.now().hour
    if (hour >= 6) and (hour < 12):
        speak(f"Good Morning {USERNAME}")
    elif (hour >= 12) and (hour < 16):
        speak(f"Good afternoon {USERNAME}")
    else:
        speak(f"Good Evening {USERNAME}")
    speak(f"I am {BOTNAME}. How may I assist you?")


# Takes Input from User
def take_user_input():
    """Takes user input, recognizes it using Speech Recognition module and converts it into text"""

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        if not 'exit' in query or 'stop' in query:
            speak(choice(opening_text))
        else:
            hour = datetime.now().hour
            if hour >= 21 and hour < 6:
                speak("Good night sir, take care!")
            else:
                speak('Have a good day sir!')
            exit()
    except Exception:
        speak('Sorry, I could not understand. Could you please say that again?')
        query = 'None'
    return query


if __name__ == '__main__':
    greet_user()
    while True:
        query = take_user_input().lower()

        if 'open notepad' in query:
            open_notepad()

        elif 'open discord' in query:
            open_discord()

        elif 'open microsoft edge' in query or 'open edge' in query:
            open_microsoftEdge()

        elif 'open command prompt' in query or 'open cmd' in query:
            open_cmd()

        elif 'shut down' in query:
            shut_down()

        elif 'restart' in query:
            re_start()

        elif "TELEGRAM" in query:
            speak("Opening TELEGRAM")
            os.system("telegram")

        elif "EXCEL" in query:
            speak("Opening MICROSOFT EXCEL")
            os.system("excel")

        elif "Power Point" in query:
            speak("Opening MICROSOFT POWERPOINT")
            os.system("powerpnt")

        elif "WORD" in query:
            speak("Opening MICROSOFT WORD")
            os.system("winword")


        elif 'the time' in query:
            strtime = datetime.now().strftime('%H:%M:%S')
            speak(f'Sir the time is {strtime}')

        
        elif 'open camera' in query:
            open_camera()

        elif 'exit' in query or 'stop' in query or 'chup' in query:
            speak('ok sir,  please call me when you need me')
            quit()

        elif 'get ram uses' in query or 'current ram uses' in query:
            get_ram_usage()
            print('RAM usage is {} MB'.format(int(get_ram_usage() / 1024 / 1024)))
            speak(print)
        elif 'system information' in query:
            sys_info('my_system')

        elif 'addition' in query:
            add()
            speak("The addition operation is success")

        elif 'open calculator' in query:
            open_calculator()

        elif 'subtraction' in query:
            sub()
            speak("The subtraction of two numbers is completed")

        elif 'cpu temperature' in query or 'computer temperature' in query:
            get_cpu_temp()
            print('Computer temperature is {} degC'.format(get_cpu_temp()))

        elif 'my brother' in query:
            speak("your brother name are Abhishek kumar, Aditay kumar")
            speak("your brother are younger form you")


        elif 'ip address' in query:
            ip_address = find_my_ip()
            speak(f'Your IP Address is {ip_address}.\n For your convenience, I am printing it on the screen sir.')
            print(f'Your IP Address is {ip_address}')

        elif 'wikipedia' in query:
            speak('What do you want to search on Wikipedia, sir?')
            search_query = take_user_input().lower()
            results = search_on_wikipedia(search_query)
            speak(f"According to Wikipedia, {results}")
            speak("For your convenience, I am printing it on the screen sir.")
            print(results)

        elif 'youtube' in query:
            speak('What do you want to play on Youtube, sir?')
            video = take_user_input().lower()
            play_on_youtube(video)
            speak("playing")

        elif 'search on google' in query:
            speak('What do you want to search on Google, sir?')
            query = take_user_input().lower()
            search_on_google(query)

        elif "send whatsapp message" in query:
            speak(
                'On what number should I send the message sir? Please enter in the console: ')
            number = input("Enter the number: ")
            speak("What is the message sir?")
            message = take_user_input().lower()
            send_whatsapp_message(number, message)
            speak("I've sent the message sir.")

        elif "send an email" in query:
            speak("On what email address do I send sir? Please enter in the console: ")
            receiver_address = input("Enter email address: ")
            speak("What should be the subject sir?")
            subject = take_user_input().capitalize()
            speak("What is the message sir?")
            message = take_user_input().capitalize()
            if send_email(receiver_address, subject, message):
                speak("I've sent the email sir.")
            else:
                speak("Something went wrong while I was sending the mail. Please check the error logs sir.")

        elif 'joke' in query:
            speak(f"Hope you like this one sir")
            joke = get_random_joke()
            speak(joke)
            speak("For your convenience, I am printing it on the screen sir.")
            pprint(joke)

        elif "advice" in query:
            speak(f"Here's an advice for you, sir")
            advice = get_random_advice()
            speak(advice)
            speak("For your convenience, I am printing it on the screen sir.")
            pprint(advice)

        elif "trending movies" in query:
            speak(f"Some of the trending movies are: {get_trending_movies()}")
            speak("For your convenience, I am printing it on the screen sir.")
            print(*get_trending_movies(), sep='\n')

        elif 'news' in query:
            speak(f"I'm reading out the latest news headlines, sir")
            speak(get_latest_news())
            speak("For your convenience, I am printing it on the screen sir.")
            print(*get_latest_news(), sep='\n')

        elif 'weather' in query:
            ip_address = find_my_ip()
            city = requests.get(f"https://ipapi.co/{ip_address}/city/").text
            speak(f"Getting weather report for your city {city}")
            weather, temperature, feels_like = get_weather_report(city)
            speak(f"The current temperature is {temperature}, but it feels like {feels_like}")
            speak(f"Also, the weather report talks about {weather}")
            speak("For your convenience, I am printing it on the screen sir.")
            print(f"Description: {weather}\nTemperature: {temperature}\nFeels like: {feels_like}")

        elif 'goodbye' in query:
            speak("goodbye sir,have a nice day")

        elif 'hello' in query or 'hi' in query:
            speak('Hello,Wellcome to Advance A.I. virtual intelligence project. At your service sir.')

        elif 'thanks' in query or 'tanks' in query or 'thank you' in query:
            speak('You are wellcome,no problem')


        elif 'how are you' in query or 'and you' in query or 'are you okay' in query:
            speak("Fine sir,Thanks")

        elif '*' in query:
            speak('Be polite please')

        elif 'your name' in query:
            speak("my name is voice assistance")

        elif 'I love you' in query:
            speak("I love you too")

        elif 'God' in query:
            speak("yes")

        elif 'your God name' in query or 'your owner name' in query:
            speak("My owner or god mane is Shivam kumar")

        elif 'who made you' in query:
            speak("I have been made by my god")

        elif 'your gender' in query:
            speak("I am a girl")

        elif 'good night' in query:
            speak("Good night dad, take care!")

        elif 'you need a break' in query:
            speak("ok sir, call me when you have some task")
            break

        elif 'sleep mode' in query or 'sleep' in query:
            speak('good night')
            os.system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')

        elif 'map' in query:
            speak('What do you want to search on Google map, sir?')
            query = take_user_input().lower()
            search_on_googlemaps(query)

        elif 'shivam' in query or 'shivam beta' in query:
            speak("Be in your limit")

        elif '.com' in query:
            speak("opening" + query)
            search(query)

        elif 'install' in query:
            speak("installing" + query)
            install(query)


        elif 'beta' in query or 'son' in query:
            speak('Yes Dad?, What can I doo for you dad?')



        elif 'play music' in query:
            music_dir = 'D:/New folder (2)'
            songs = os.listdir(music_dir)
            speak("playing music")
            print(songs)
            os.startfile(os.path.join(music_dir, songs[1]))

        elif 'stop music' in query:
            stop_music()
            speak("music stopped")

        elif 'pause music' in query:
            pause_music()
            speak("music paused")



        elif 'are you single' in query:
            speak("I am in a relationship with wifi")

        elif 'follow my command' in query:
            speak("tell me sir i am waiting for your order")

        elif 'close' in query:
            speak("closing sir")

        elif 'play' in query:
            soung = query.replace('play', ' ')
            speak("playing" + soung)
            pywhatkit.playonyt(soung)





