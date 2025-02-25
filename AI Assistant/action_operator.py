import speech_to_text
import text_to_speech
import datetime
import webbrowser
import weather




def action_fun(data):
    user_data = data.lower()
    
    if "what is your name" in user_data:
        text_to_speech.text_to_speech_fun("My name is Virtual Assistant")
        return "My name is Virtual Assistant"
    
    elif "Hello" in user_data or "hey" in user_data:
        text_to_speech.text_to_speech_fun("Hi Sir, How can I help you")
        return "Hi Sir, How can I help you"
    
    elif "time now" in user_data:
        current_time = datetime.datetime.now()
        Time = str(current_time) + "Hour" + str(current_time.minute) + "minute"
        text_to_speech.text_to_speech_fun(Time)
        return Time
    
    elif "shut down" in user_data:
        text_to_speech.text_to_speech_fun("Ok Sir")
        return "Ok Sir"
    
    elif "play youtube" in user_data:
        webbrowser.open('https://youtube.com/')
        text_to_speech.text_to_speech_fun("Youtube is open for you, enjoy")
        return "Youtube is open for you, enjoy"
    
    elif "open google" in user_data:
        webbrowser.open('https://google.com/')
        text_to_speech.text_to_speech_fun("Google is open for you, enjoy")
        return "Google is open for you, enjoy"
    
    elif "weather" in user_data:
        result = weather.weather_fun()
        text_to_speech.text_to_speech_fun(result)
        return result
    
    else:
        text_to_speech.text_to_speech_fun("I am unable to understand")
        return "I am unable to understand"