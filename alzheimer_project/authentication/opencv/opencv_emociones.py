import cv2
import numpy as np
import tensorflow as tf

dict_emociones = {0: 'Ira', 1: 'Asco', 2: 'Tristeza', 3: 'Felicidad', 4: 'Sorpresa'}

# Cargar el clasificador de rostros
loaded_model = tf.keras.models.load_model(r'C:\Users\valen\OneDrive\Desktop\proyecto-codigohex\alzheimer_project\authentication\opencv\Modelocompleto_deteccionEmociones01.h5')
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
    net = cv2.dnn.readNetFromCaffe("C:/Users/mati/Desktop/proyecto-codigohex/alzheimer_project/authentication/opencv/opencv_face_detector.prototxt", 'C:/Users/mati/Desktop/proyecto-codigohex/alzheimer_project/authentication/opencv/res10_300x300_ssd_iter_140000.caffemodel')

    # Parametros del modelo
    # Tamaño
    anchonet = 300
    altonet = 300
    # Valores medios de los canales de color
    media = [104, 117, 123]
    umbral = 0.7

    frame = cv2.flip(imagen, 1)

       # Extraemos info de los frames
    altoframe = frame.shape[0]
    anchoframe = frame.shape[1]

    # Preprocesamos la imagen
    # Images - Factor de escala - tamaño - media de color - Formato de color(BGR-RGB) - Recorte
    blob = cv2.dnn.blobFromImage(frame, 1.0, (anchonet, altonet), media, swapRB = False, crop = False)

    # Corremos el modelo
    net.setInput(blob)
    detecciones = net.forward()

    # Iteramos
    for i in range(detecciones.shape[2]):
        # Extraemos la confianza de esa deteccion
        conf_detect = detecciones[0,0,i,2]
        # Si superamos el umbral (70% de probabilidad de que sea un rostro)
        if conf_detect > umbral:

            # Extraemos las coordenadas
            xmin = int(detecciones[0, 0, i, 3] * anchoframe)
            ymin = int(detecciones[0, 0, i, 4] * altoframe)
            xmax = int(detecciones[0, 0, i, 5] * anchoframe)
            ymax = int(detecciones[0, 0, i, 6] * altoframe)

            # Dibujamos el rectangulo
            cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), (0,0,255), 2)
            # Texto que vamos a mostrar
            label = "Confianza de deteccion: %.4f" % conf_detect
            # Tamaño del fondo del label
            label_size, base_line = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)
            # Colocamos fondo al texto
            cv2.rectangle(frame, (xmin, ymin - label_size[1]), (xmin + label_size[0], ymin + base_line),
                          (0,0,0), cv2.FILLED)
            # Colocamps el texto
            cv2.putText(frame, label, (xmin, ymin), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 1)

            rostros = detectar_rostros(imagen)
            emociones = []

            for (x, y, w, h) in rostros:
                cara_color = imagen[y:y + h, x:x + w]
                cara_gris = cv2.cvtColor(cara_color, cv2.COLOR_BGR2GRAY)
                cara_redimensionada = cv2.resize(cara_gris, (96, 96))
                emocion = detectar_emociones(cara_redimensionada)
                emociones.append(emocion)


            return emociones
        return 'No hay rostro'
