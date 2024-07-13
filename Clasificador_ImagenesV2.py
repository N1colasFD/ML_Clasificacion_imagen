import configparser
import tensorflow as tf
from tensorflow.keras.applications import InceptionV3
from tensorflow.keras.applications.inception_v3 import preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import numpy as np
import os
import shutil
import pillow_heif
from PIL import Image
import time
import psutil

# Leer configuración de 'config.ini'
config = configparser.ConfigParser()
config.read('config.ini')
environment = "Config"

try:
    INPUT_DIR = config[environment]['directorio_carpeta_landing']
    OUTPUT_DIR = config[environment]['directorio_carpeta_output']
    UNCLASSIFIED_DIR = config[environment]['directorio_carpeta_unclassified']
except KeyError as e:
    raise

SUPPORTED_FORMATS = ('.heic', '.png', '.jpg', '.jpeg')

# Cargar el modelo preentrenado InceptionV3
model = InceptionV3(weights='imagenet')

def setup_output_directory(output_dir):
    """Crea el directorio de salida si no existe."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Directorio de salida creado: {output_dir}")
    else:
        print(f"Directorio de salida ya existe: {output_dir}")

def load_heic_image(heic_path):
    """Carga una imagen HEIC y la convierte a un formato compatible con Pillow."""
    heif_file = pillow_heif.read_heif(heic_path)
    img = Image.frombytes(
        heif_file.mode, 
        heif_file.size, 
        heif_file.data,
        "raw",
        heif_file.mode,
        heif_file.stride,
    )
    return img

def print_system_info():
    """Imprime información sobre el uso de CPU y GPU."""
    cpu_usage = psutil.cpu_percent()
    print(f"Uso de CPU: {cpu_usage}%")
    if tf.config.list_physical_devices('GPU'):
        for gpu in tf.config.experimental.list_physical_devices('GPU'):
            gpu_details = tf.config.experimental.get_device_details(gpu)
            print(f"GPU: {gpu_details}")

def map_to_custom_categories(label):
    """Mapea las etiquetas del modelo a las tres categorías personalizadas."""
    people_keywords = ['person', 'man', 'woman', 'boy', 'girl', 'face', 'human']
    car_keywords = ['car', 'vehicle', 'automobile', 'truck', 'bus']
    landscape_keywords = ['mountain', 'river', 'forest', 'landscape', 'tree', 'sky', 'beach', 'sea']

    if any(keyword in label for keyword in people_keywords):
        return 'people'
    elif any(keyword in label for keyword in car_keywords):
        return 'car'
    elif any(keyword in label for keyword in landscape_keywords):
        return 'landscape'
    else:
        return 'unclassified'


def classify_and_copy_image(img_path):
    """Clasifica una imagen y la copia al directorio correspondiente."""
    try:
        # Cargar y preprocesar la imagen
        if img_path.lower().endswith('.heic'):
            img = load_heic_image(img_path)
        else:
            img = Image.open(img_path)
        
        img = img.resize((299, 299))  # InceptionV3 requiere tamaño 299x299 
        
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = preprocess_input(img_array)

        # Clasificar la imagen
        predictions = model.predict(img_array)
        decoded_predictions = decode_predictions(predictions, top=1)
        label = decoded_predictions[0][0][1]

        # Determinar la categoría
        category = map_to_custom_categories(label)
        category_dir = os.path.join(OUTPUT_DIR, category)
        if not os.path.exists(category_dir):
            os.makedirs(category_dir)
            print(f"Directorio de categoría creado: {category_dir}")
        shutil.copy(img_path, os.path.join(category_dir, os.path.basename(img_path)))
        print(f'Copiado: {img_path} -> {category_dir}')
        return (img_path, label, category_dir)
    except Exception as e:
        print(f"Error al procesar la imagen {img_path}: {e}")
        return None

def process_images(input_dir):
    """Procesa todas las imágenes en el directorio especificado."""
    if not os.path.exists(input_dir):
        print(f"No se encontró el directorio de entrada: {input_dir}")
        return

    images_to_process = [f for f in os.listdir(input_dir) if f.lower().endswith(SUPPORTED_FORMATS)]
    num_images = len(images_to_process)

    if (num_images == 0):
        print(f"No se encontraron imágenes en {input_dir} para procesar.")
        return

    print(f"Se encontraron {num_images} imágenes para procesar en {input_dir}.")

    log_entries = []
    for filename in images_to_process:
        img_path = os.path.join(input_dir, filename)
        if os.path.isfile(img_path):
            result = classify_and_copy_image(img_path)
            if result:
                img_path, label, category_dir = result
                log_entries.append({
                    "imagen": img_path,
                    "extension": os.path.splitext(img_path)[1],
                    "clasificacion": label,
                    "directorio": category_dir,
                    "peso_archivo": os.path.getsize(img_path)
                })
            time.sleep(3)  # Añadir un retardo para no estresar el CPU o GPU

    with open('classification_log.txt', 'w') as log_file:
        for entry in log_entries:
            log_file.write(f"{entry['imagen']}||{entry['extension']}||{entry['clasificacion']}||{entry['directorio']}||{entry['peso_archivo']}\n")

    print("Informe de clasificación generado en 'classification_log.txt'.")

    # Estadística
    total_size = sum(entry["peso_archivo"] for entry in log_entries)
    print(f"Total de imágenes clasificadas: {len(log_entries)}")
    print(f"Tamaño total de las imágenes clasificadas: {total_size:.2f} Mbytes ")

if __name__ == "__main__":
    setup_output_directory(OUTPUT_DIR)
    process_images(INPUT_DIR)
