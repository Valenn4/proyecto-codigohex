import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Di algo:")
    audio = recognizer.listen(source)

    try:
        texto = recognizer.recognize_google(audio, language="es-ES")
        print("Dijiste:", texto)
    except sr.UnknownValueError:
        print("Lo siento, no pude entender el audio.")
    except sr.RequestError as e:
        print(f"No se pudieron solicitar resultados al servicio de reconocimiento de voz de Google; {e}")
