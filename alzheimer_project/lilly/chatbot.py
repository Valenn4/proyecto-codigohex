from nltk.chat.util import Chat, reflections
from datetime import datetime
mis_reflexions = {
"ir": "fui",
"hola": "hey"
}


pares = [
    [
        r"mi nombre es (.*)",
        ["Hola %1, como estas ?",]
    ],
     [
        r"cuál es tu nombre",
        ["Mi nombre es Lilly",]
    ],
    [
        r"cómo estás|como estas?|como estás?|como estas",
        ["Bien, y tu?",]
    ],
    [
        r"disculpa (.*)",
        ["No pasa nada",]
    ],
    [
        r"hola|hey|buenas",
        ["Hola", "Que tal",]
    ],
    [
        r"que (.*) quieres ?",
        ["Nada gracias",]
        
    ],
    [
        r"(.*) creado ?",
        ["Fui creado hoy",]
    ],
     [
        r"Cuándo es mi próximo médico",
        ["Aún tengo que ajustar esta función",]
    ],
     [
        r"Quiero jugar un juego",
        ["../juegos"]
    ],
     [
        r"Dónde guardo mis llaves generalmente",
        ["Aún tengo que ajustar esta función",]
    ],
    
    [
        r"(.*) Spotify ?|Quiero escuchar música|Quiero escuchar musica",
        ["Quieres escuchar un artista, canción, playlist o album?",]
    ],
    [
        r"Quiero escuchar una cancion|Quiero escuchar una canción",
        ["Cuál es el nombre de la canción?",]
    ],
    [
        r"Quiero escuchar una playlist",
        ["Cuál es el nombre de la playlist?",]
    ],
    [
        r"Quiero escuchar un album",
        ["Cuál es el nombre del album?",]
    ],
    [
        r"Quiero escuchar un artista",
        ["Cuál es el nombre del artista?",]
    ],
    [
        r"La cancion se llama (.*)|La canción se llama (.*)",
        ["track:http://127.0.0.1:8000/api/spotify/%1",]
    ],
    [
        r"El album se llama (.*)",
        ["album:http://127.0.0.1:8000/api/spotify/%1",]
    ],
    [
        r"La playlist se llama (.*)",
        ["playlist:http://127.0.0.1:8000/api/spotify/%1",]
    ],
    [
        r"El artista se llama (.*)",
        ["artist:http://127.0.0.1:8000/api/spotify/%1",]
    ],
    [
        r"quién es Olga",
        ["La mejor orientadora del mundo",]
    ],
    [
        r"Quiero ver el calendario",
        ["../calendario"]
    ],
    [
        r"Quién es mi contacto de emergencia|Quien es mi contacto de emergencia",
        ["contacto de emergencia"]
    ],
    [
        r"qué día es hoy",
        [f'Hoy es día {datetime.now().day} de {datetime.now().month} del {datetime.now().year}']
    ],
    [
        r"qué hora es",
        [f'Son las {datetime.now().hour}:{datetime.now().minute}']
    ],
    [
        r"finalizar",
        ["Chao","Fue bueno hablar contigo"]
],
]

chat = Chat(pares, mis_reflexions)

def chatear(mensaje):
    chat = Chat(pares, mis_reflexions)
    x=chat.respond(mensaje)
    return x

