import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import noisereduce as nr

listener = sr.Recognizer()
engine = pyttsx3.init()
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source, duration=1)
            print('listening...!!!')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        print('error in take command fn')
        pass
    return command

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        print(song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M:%p')
        print('Current time is '+time)
        talk('current time is ' + time)

    elif 'search' in command:
        person = command.replace('search', '')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)
    elif 'how are you' in command:
        talk('I am fine, thanks. How about you')
    elif 'fine' in command:
        talk('How can i help you')
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'single' in command:
        talk('I am in a relationship with siri')
    elif 'joke' in command:
        jokes = pyjokes.get_joke()
        print(jokes)
        talk(jokes)
    elif 'bye' in command:
        talk('no problem bye')
        pass
    else:
        talk('Pardon, Please say it again')


while True:
    run_alexa()