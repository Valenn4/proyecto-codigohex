import pyttsx3

def sintetizar_voz(texto):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say(texto)
    engine.runAndWait()
    
