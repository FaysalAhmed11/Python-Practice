import speech_recognition as sr

recogniger = sr.Recognizer()

def speech_to_text_fun():
    with sr.Microphone() as source:
        audio = recogniger.listen(source)
        try:
            voice_data = ""
            voice_data = recogniger.recognize_google(audio)
           
            return voice_data
            
        except sr.UnknownValueError:
            print("error")
            
        except sr.RequestError:
            print("Request Error")
            
            
speech_to_text_fun()