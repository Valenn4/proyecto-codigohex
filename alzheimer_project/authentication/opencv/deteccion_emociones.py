import tensorflow as tf
import numpy as np
import cv2

dict_emociones = {0:'Ira', 1:'Asco', 2:'Tristeza', 3:'Felicidad', 4: 'Miedo'}

loaded_model = tf.keras.models.load_model('Modelocompleto_deteccionEmociones01.h5')


# Cargar la imagen
ruta_imagen = 'foto_sorprendida.jpg'

imagen_color = cv2.imread(ruta_imagen)
imagen_color = cv2.cvtColor(imagen_color, cv2.COLOR_BGR2RGB)

imagen_gris = cv2.cvtColor(imagen_color, cv2.COLOR_RGB2GRAY)
imagen_redimensionada = cv2.resize(imagen_gris, (96, 96))
imagen_redimensionada = np.expand_dims(imagen_redimensionada, axis=-1)

imagen_redimensionada = imagen_redimensionada / 255.0

prediccion = loaded_model.predict(np.expand_dims(imagen_redimensionada, axis=0))
print("Predicción:", prediccion)

# Obtener las predicciones de emociones
prediccion_emociones = prediccion[0, -5:]

# Aplicar la función softmax a las predicciones de emociones
probabilidades_emociones = tf.nn.softmax(prediccion_emociones)
# Obtener la clase con la probabilidad más alta para las emociones
clase_predicha_emociones = np.argmax(probabilidades_emociones)

# Obtener el nombre de la emoción predicha
emocion_predicha = dict_emociones[clase_predicha_emociones]

print("Probabilidades de emociones:", probabilidades_emociones.numpy())
print("Emoción predicha:", emocion_predicha)
