import pyttsx3

def sintetizar_voz(texto):
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()
    
