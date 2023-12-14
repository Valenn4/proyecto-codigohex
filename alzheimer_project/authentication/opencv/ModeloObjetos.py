import tensorflow as tf
import numpy as np
import cv2
from sklearn.preprocessing import LabelEncoder

loaded_model = tf.keras.models.load_model(r'C:\Users\grazi\proyecto-codigohex\alzheimer_project\authentication\opencv\Cargas_modelo_Objetos.h5')

# Cargar la imagen
ruta_imagen = "alzheimer_project/authentication/opencv/mazana.jpg"

imagen_color = cv2.imread(ruta_imagen)

if imagen_color is not None:
    imagen_color = cv2.cvtColor(imagen_color, cv2.COLOR_BGR2RGB)

    imagen_gris = cv2.cvtColor(imagen_color, cv2.COLOR_RGB2GRAY)
    imagen_redimensionada = cv2.resize(imagen_gris, (150, 150))
    imagen_redimensionada = np.expand_dims(imagen_redimensionada, axis=-1)

    imagen_redimensionada = imagen_redimensionada / 255.0

    prediccion = loaded_model.predict(np.expand_dims(imagen_redimensionada, axis=0))

    # Obtener el valor numérico predicho
    predicted_label_numeric = np.argmax(prediccion, axis=1)[0]

    # Definir el diccionario de categorías
    dict_categorias = {
        7: 'Mochila',
        3: 'Enchufes',
        11: 'Zapatos',
        5: 'Laptop',
        6: 'Manzana',
        8: 'Paraguas',
        4: 'Fresa',
        10: 'Sofa',
        9: 'Silla',
        12: 'Mesa',
        1: 'Cargadores de móvil',
        0: 'Banana',
        2: 'Celular'
    }

    # Obtener el nombre de la categoría predicha
    predicted_label_original = dict_categorias[predicted_label_numeric]

    print("Predicción:", predicted_label_original)
else:
    print("Error al leer la imagen. Asegúrate de que la ruta de la imagen sea correcta.")