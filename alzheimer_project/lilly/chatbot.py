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
        r"(.*) Spotify ?",
        ["Quieres escuchar un artista, canción o Playlist?",]
    ],
    [
        r"(.*) canción ",
        ["De que artista?",]
    ],
    [
        r"(.*) álbum ",
        ["De que artista?",]
    ],
    [
        r"(.*) playlist ",
        ["De que artista?",]
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

