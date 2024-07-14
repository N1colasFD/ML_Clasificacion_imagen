
# Image Classification Project 🚀

Este proyecto utiliza el modelo InceptionV3 🧠 para clasificar imágenes en tres categorías principales: personas, paisajes y carros en su segunda version **Clasificador_ImagenesV2.py**, la version normal generaliza.

<a href="https://postimg.cc/YjdB0pVW">
    <img src="https://i.postimg.cc/L6p9y53N/00e6f8a9fcbf996b20290bcf30c862c2.gif" alt="Classification GIF" width="100"/>
</a>

## Tabla de Contenidos 📑
- [Introducción](#introducción)
- [Algoritmo InceptionV3](#algoritmo-inceptionv3)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Requisitos](#requisitos)
- [Configuración](#configuración)
- [Ejecución](#ejecución)
- [Detalles del Script](#detalles-del-script)
- [Resultados](#resultados)
- [Contribuciones](#contribuciones)
- [Licencia](#licencia)

## Introducción 🌟
Este proyecto se basa en la arquitectura InceptionV3 para realizar la clasificación de imágenes. El objetivo es lograr clasificar las imágenes en tres categorías: personas, paisajes y carros, utilizando un modelo preentrenado y técnicas de preprocesamiento de imágenes.

![InceptionV3 Architecture](https://paperswithcode.com/media/methods/Inceptionv3.png)

### Ventajas de InceptionV3
- **Eficiencia Computacional**: Optimiza el uso de recursos computacionales mediante el uso de convoluciones de diferentes tamaños.
- **Reducción de Parámetros**: Utiliza convoluciones 1x1 para reducir la dimensionalidad y mejorar la eficiencia.
- **Alta Precisión**: Ha demostrado ser muy precisa en tareas de clasificación de imágenes en comparación con otras arquitecturas.

## Aplicaciones del Modelo InceptionV3 📊

InceptionV3 es un modelo versátil que se ha utilizado en una variedad de tareas de aprendizaje profundo. La siguiente gráfica muestra las diferentes tareas en las que se ha empleado InceptionV3, junto con el número de artículos publicados y su porcentaje de participación en cada tarea.

[![Captura-de-pantalla-2024-07-13-193221.png](https://i.postimg.cc/gkTMzXtK/Captura-de-pantalla-2024-07-13-193221.png)](https://postimg.cc/Xp9KxJbZ)

### Distribución de Tareas
- **Image Classification**: 16 papers (11.94%)
- **General Classification**: 15 papers (11.19%)
- **Classification**: 13 papers (9.70%)
- **Adversarial Attack**: 5 papers (3.73%)
- **Quantization**: 4 papers (2.99%)
- **Object Detection**: 3 papers (2.24%)
- **Image Captioning**: 3 papers (2.24%)
- **Diversity**: 3 papers (2.24%)
- **Semantic Segmentation**: 3 papers (2.24%)
- **Other**: Resto de las tareas no especificadas en detalle.

Esta distribución evidencia la popularidad de InceptionV3 en tareas de clasificación de imágenes, así como su aplicabilidad en otros dominios del aprendizaje profundo.

----
## Uso de Modelos a lo Largo del Tiempo 📈

La gráfica diferentes modelos de redes neuronales, incluida Inception-v3, a lo largo del tiempo. Esto nos permite observar las tendencias y la popularidad relativa, asi como la superidad en ciertas tareas de ResNet sobre InceptionV3

[![Captura-de-pantalla-2024-07-13-193607.png](https://i.postimg.cc/KYyDjnPt/Captura-de-pantalla-2024-07-13-193607.png)](https://postimg.cc/fVB9gSgb)

### Modelos Comparados
- **Inception-v3**: Representado en azul.
- **ResNet**: Representado en rojo.
- **VGG**: Representado en verde.
- **MobileNetV2**: Representado en amarillo.
- **DenseNet**: Representado en naranja.
- **AlexNet**: Representado en cian.

Esta comparación temporal destaca cómo ResNet ha mantenido una popularidad constante y elevada en comparación con otros modelos, mientras que Inception-v3 y otros han tenido fluctuaciones menores en su uso.



### Enlaces Útiles
- [Papers with Code — Inception-v3 Explained](https://paperswithcode.com/method/inception-v3)
- [Google Research — Improving Inception and Image Classification in TensorFlow](https://arxiv.org/abs/1512.00567)
- [Keras — InceptionV3](https://keras.io/api/applications/inceptionv3/)
- [ROCm Docs — Deep learning: Inception V3 with PyTorch](https://rocmdocs.amd.com/en/latest/Deep_learning/Deep_learning_Inceptionv3.html)

## Estructura del Proyecto 📂

- **landing/**: Carpeta de entrada con las imágenes a clasificar.
- **out_classi/**: Carpeta de salida con las imágenes clasificadas.
  - **car/**: Imágenes clasificadas como carros.
  - **landscape/**: Imágenes clasificadas como paisajes.
  - **people/**: Imágenes clasificadas como personas.
  - **unclassified/**: Imágenes no clasificadas.
- **unclassified/**: Carpeta para imágenes no clasificadas.
- **config.ini**: Archivo de configuración con las rutas de las carpetas.
- **classification_log.txt**: Registro de las clasificaciones realizadas.
- **requirements.txt**: Dependencias necesarias para ejecutar el proyecto.
- **Clasificador_Imagenes.py**: Script principal de clasificación.
- **Clasificador_ImagenesV2.py**: Versión mejorada del script de clasificación.

## Requisitos 📦

Para instalar las dependencias, ejecuta:
```bash
pip install -r requirements.txt```
