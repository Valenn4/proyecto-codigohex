import cv2
import numpy as np
import tensorflow as tf

dict_emociones = {0: 'Ira', 1: 'Asco', 2: 'Tristeza', 3: 'Felicidad', 4: 'Miedo'}

# Carga del modelo de detección de emociones
loaded_model = tf.keras.models.load_model(r'C:\Users\grazi\proyecto-codigohex\alzheimer_project\authentication\opencv\Modelocompleto_deteccionEmociones01.h5')

# Carga del clasificador de rostros
cascada_rostro = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def detectar_emociones(imagen):
    imagen_color = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)

    imagen_gris = cv2.cvtColor(imagen_color, cv2.COLOR_RGB2GRAY)
    imagen_redimensionada = cv2.resize(imagen_gris, (96, 96))
    imagen_redimensionada = np.expand_dims(imagen_redimensionada, axis=-1)

    imagen_redimensionada = imagen_redimensionada / 255.0

    prediccion = loaded_model.predict(np.expand_dims(imagen_redimensionada, axis=0))

    prediccion_emociones = prediccion[0, -5:]
    probabilidades_emociones = tf.nn.softmax(prediccion_emociones)
    clase_predicha_emociones = np.argmax(probabilidades_emociones)

    emocion_predicha = dict_emociones[clase_predicha_emociones]

    return emocion_predicha

def detectar_rostros(imagen):
    # Convertir la imagen a escala de grises para la detección de rostros
    imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

    # Detectar rostros en la imagen
    rostros = cascada_rostro.detectMultiScale(imagen_gris, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Devolver las coordenadas de los rostros detectados
    return rostros

def detectar_emociones_en_rostro(imagen):
    rostros = detectar_rostros(imagen)
    emociones = []

    for (x, y, w, h) in rostros:
        cara_color = imagen[y:y + h, x:x + w]
        cara_gris = cv2.cvtColor(cara_color, cv2.COLOR_BGR2GRAY)
        cara_redimensionada = cv2.resize(cara_gris, (96, 96))
        emocion = detectar_emociones(cara_redimensionada)
        emociones.append(emocion)


    return emociones
