from nltk.chat.util import Chat, reflections

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
        ["Mi nombre es Chatbot ?",]
    ],
    [
        r"cómo estás",
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
        r"En qué día estamos hoy",
        ["Aún tengo que ajustar esta función",]
    ],
     [
        r"Cuándo es mi próximo médico",
        ["Aún tengo que ajustar esta función",]
    ],
     [
        r"¿Qué hora es ahora?",
        ["Aún tengo que ajustar esta función",]
    ],
     [
        r"Quiero jugar un juego",
        ["games.html"]
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
        r"finalizar",
        ["Chao","Fue bueno hablar contigo"]
],
]

chat = Chat(pares, mis_reflexions)

def chatear(mensaje):
    
    print("Hola soy un bot, escribe algo para comenzar") #mensaje por defecto
    chat = Chat(pares, mis_reflexions)
    x=chat.respond(mensaje)
    return x

