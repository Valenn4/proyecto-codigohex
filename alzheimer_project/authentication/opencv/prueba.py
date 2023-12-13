import tensorflow as tf
import numpy as np
import cv2
from sklearn.preprocessing import LabelEncoder

loaded_model = tf.keras.models.load_model('best_model21.h5')

# Cargar la imagen
ruta_imagen = r'C:\Users\grazi\OneDrive\Documentos\proyectofinalfundasplay\datasetobjetos\DatasetObjets\DatasetObjetos\Laptop\57c64423-1f3e-40ce-8c17-abac17e885e3.__CR0,0,1200,900_PT0_SX600_V1___.jpg'

imagen_color = cv2.imread(ruta_imagen)
imagen_color = cv2.cvtColor(imagen_color, cv2.COLOR_BGR2RGB)

imagen_gris = cv2.cvtColor(imagen_color, cv2.COLOR_RGB2GRAY)
imagen_redimensionada = cv2.resize(imagen_gris, (150, 150))
imagen_redimensionada = np.expand_dims(imagen_redimensionada, axis=-1)

imagen_redimensionada = imagen_redimensionada / 255.0

prediccion = loaded_model.predict(np.expand_dims(imagen_redimensionada, axis=0))
print("Predicción:", prediccion)

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
