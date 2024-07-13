# Image Classification Project 🚀

Este proyecto utiliza el modelo InceptionV3 para clasificar imágenes en tres categorías principales: personas, paisajes y carros.

![Image](image.png)

## Tabla de Contenidos 📑
- [Introducción](#introducción)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Requisitos](#requisitos)
- [Configuración](#configuración)
- [Ejecución](#ejecución)
- [Detalles del Script](#detalles-del-script)
- [Resultados](#resultados)
- [Contribuciones](#contribuciones)
- [Licencia](#licencia)

## Introducción 🌟
Este proyecto se basa en la arquitectura InceptionV3 para realizar la clasificación de imágenes. El objetivo es clasificar las imágenes en tres categorías: personas, paisajes y carros, utilizando un modelo preentrenado y técnicas de preprocesamiento de imágenes.

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
pip install -r requirements.txt


Contribuciones 🤝
¡Las contribuciones son bienvenidas! Siéntete libre de abrir un issue o un pull request. Aquí hay algunas maneras en las que puedes contribuir:

Reportar errores
Sugerir nuevas características
Mejorar la documentación
Enviar solicitudes de extracción para correcciones o nuevas características
Licencia 📜
Este proyecto está bajo la Licencia MIT. Mira el archivo LICENSE para más detalles.

--
## tal vez tambien el interese
“InceptionV3 classification improvement techniques”
bing.com

Papers with Code — Inception-v3 Explained | Papers With Code
paperswithcode.com

Hugging Face — Inception v3
huggingface.co

Google Research — Improving Inception and Image Classification in TensorFlow
research.google

Keras — InceptionV3
keras.io

ROCm Docs — Deep learning: Inception V3 with PyTorch — ROCm Documentation
rocmdocs.amd.com