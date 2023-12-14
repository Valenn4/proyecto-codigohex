import cv2
import numpy as np
import tensorflow as tf

# Cargar el modelo de detección de emociones
dict_emociones = {0: 'Ira', 1: 'Asco', 2: 'Tristeza', 3: 'Felicidad', 4: 'Miedo'}
loaded_model = tf.keras.models.load_model(r'C:\Users\grazi\proyecto-codigohex\alzheimer_project\authentication\opencv\Modelocompleto_deteccionEmociones01.h5')

# Cargar el clasificador de rostros
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
    # Aplicar la detección de rostros
    rostros = detectar_rostros(imagen)

    # Iterar sobre los rostros detectados y aplicar la detección de emociones
    for (x, y, w, h) in rostros:
        # Extraer la región de la cara de la imagen
        cara = imagen[y:y+h, x:x+w]

        # Aplicar la detección de emociones en la región de la cara
        emocion = detectar_emociones(cara)

        # Dibujar un rectángulo alrededor del rostro
        cv2.rectangle(imagen, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # Mostrar la emoción detectada sobre el rectángulo del rostro
        cv2.putText(imagen, f'Emoción: {emocion}', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    return imagen

# Iniciar la captura de video
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Aplicar la detección de emociones en rostros
    frame_con_emociones = detectar_emociones_en_rostro(frame)

    # Mostrar el resultado en tiempo real
    cv2.imshow('Detección de Emociones en Vivo', frame_con_emociones)

    # Salir si se presiona 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la captura y cerrar la ventana
cap.release()
cv2.destroyAllWindows()
