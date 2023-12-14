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
        r"Dónde guardo mis llaves generalmente",
        ["Aún tengo que ajustar esta función",]
    ],
    
    [
        r"(.*) Spotify ?|(.*) Quiero escuchar música|Quiero escuchar musica",
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
        r"(.*) Quiero ver el calendario|Quiero ver el calendario",
        ["../calendario"]
    ],
     [
        r"(.*) Quiero jugar un juego",
        ["../juegos"]
    ],
    [
        r"(.*) Quiero mi perfil|(.*) Quiero ver mi perfil",
        ["../perfil"]
    ],
    [
        r"(.*) Quién es mi contacto de emergencia|Quien es mi contacto de emergencia|quién es mi contacto de emergencia",
        ["contacto de emergencia"]
    ],
    [
        r"(.*) Tengo una emergencia|ayuda|auxilio",
        ["Los numeros de emergencia son. El numero de la Policía Nacional es 091. El numero de la Guardia Civil es 062. El numero de los bombero es 080. Si sufre de violencia de genero marque 016. ¿A qué numero quieres llamar?"]
    ],
    [
        r"(.*) qué día es hoy",
        [f'Hoy es día {datetime.now().day} del {datetime.now().month} del {datetime.now().year}']
    ],
    [
        r"(.*) qué hora es",
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

