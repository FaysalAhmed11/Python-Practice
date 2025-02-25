import pyttsx3

def text_to_speech_fun(text):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 'rate = 70')
    engine.say(text)
    engine.runAndWait()
    
    
#text_to_speech_fun("Hello World")