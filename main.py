import speech_recognition as sp
import pyttsx3 as tx
import pywhatkit as kit
import datetime
import wikipedia as wiki

listener=sp.Recognizer()
engine=tx.init()

def talk(sentence):
    engine.say('Hi i am your tecmo ji, and now')
    engine.say(sentence)
    engine.runAndWait()
def take_command():
    try:
        with sp.Microphone() as source:
            print('hearing...')
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            command=command.lower()
            print(command)
            if('tecmo ji' in command):
                print(command)

    except:
        print('mm')

    return command


def run_techmoji():
    command=take_command()
    print(command)
    if('play' in command):
        song=command.replace('play','')
        talk('playing'+song)
        print('playing')
        kit.playonyt(song)

    elif('time' in command):
        time=datetime.datetime.now().strftime('%I:%M %p')
        talk('I know you lazy to see your watch. Anyways the time is'+time)

    elif(not ('time' and 'play') in command):
        info=wiki.summary(command,1)
        talk(info)




run_techmoji()
