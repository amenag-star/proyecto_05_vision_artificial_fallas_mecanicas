# Proyecto 05: Visión Artificial para Detección de Fallas Mecánicas

## Descripción del proyecto

Este proyecto aplica técnicas de visión artificial y redes neuronales convolucionales para clasificar imágenes de componentes mecánicos utilizados en mantenimiento industrial.

El objetivo principal es desarrollar un modelo de Machine Learning capaz de identificar visualmente piezas en buen estado y piezas con posibles fallas, utilizando imágenes clasificadas en tres categorías:

* Defected1
* Defected2
* Normal

El proyecto se enmarca en una aplicación industrial orientada al apoyo de procesos de diagnóstico, mantenimiento preventivo, control de calidad y reducción de tiempos de inspección en componentes mecánicos.

---

## Contexto industrial

En entornos industriales, la inspección visual de componentes mecánicos suele depender de la experiencia del personal técnico. Este proceso puede verse afectado por variabilidad humana, tiempos de revisión, condiciones de iluminación, nivel de desgaste de las piezas y disponibilidad de especialistas.

La visión artificial permite apoyar este proceso mediante modelos capaces de reconocer patrones visuales en imágenes, clasificando piezas según su estado o tipo de defecto.

Este tipo de solución puede aplicarse en áreas como:

* Mantenimiento industrial.
* Diagnóstico de fallas.
* Control de calidad.
* Gestión de repuestos.
* Inspección visual asistida.
* Automatización de procesos técnicos.

---

## Objetivo general

Desarrollar un modelo de clasificación de imágenes mediante una red neuronal convolucional CNN, utilizando TensorFlow y Keras, para identificar fallas visuales en componentes mecánicos.

---

## Objetivos específicos

* Cargar y organizar un dataset de imágenes clasificado por tipo de componente.
* Preparar las imágenes para entrenamiento mediante redimensionamiento y normalización.
* Dividir los datos en conjuntos de entrenamiento, validación y prueba.
* Construir y entrenar un modelo CNN con TensorFlow/Keras.
* Evaluar el desempeño del modelo mediante métricas de clasificación.
* Exportar gráficos, métricas y resultados del modelo.
* Documentar el proyecto como parte de un portafolio profesional de Data Science aplicado a industria.

---

## Dataset utilizado

El proyecto utiliza el dataset:

**Mechanic Component Images (Normal / Defected)**

El dataset contiene imágenes de pistones mecánicos clasificadas en tres carpetas:

* Defected1
* Defected2
* Normal

En este proyecto se trabajó con un total de 285 imágenes.

Por tamaño y condiciones de descarga, el dataset original no se incluye directamente en el repositorio. La carpeta `data/raw/` contiene una nota explicativa.

---

## Estructura del proyecto

```text
proyecto_05_vision_artificial_fallas_mecanicas/
│
├── data/
│   ├── raw/
│   │   └── README.md
│   └── processed/
│
├── docs/
│
├── notebooks/
│   └── 01_clasificacion_fallas_mecanicas_cnn.ipynb
│
├── outputs/
│   ├── graficos/
│   ├── metricas/
│   └── modelos/
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

## Herramientas utilizadas

* Python
* TensorFlow
* Keras
* NumPy
* Pandas
* Matplotlib
* Scikit-learn
* Pillow
* Jupyter Notebook

---

## Metodología

El desarrollo del proyecto siguió las siguientes etapas:

1. Definición del problema industrial.
2. Organización del dataset por carpetas de clase.
3. Creación de una tabla con rutas de imágenes y etiquetas.
4. Codificación numérica de clases.
5. Visualización de distribución de imágenes.
6. División estratificada en entrenamiento, validación y prueba.
7. Preprocesamiento de imágenes.
8. Construcción de modelo CNN.
9. Entrenamiento con aumento de datos y EarlyStopping.
10. Evaluación del modelo sobre conjunto de prueba.
11. Generación de matriz de confusión.
12. Exportación de métricas y gráficos.
13. Conclusión técnica e industrial.

---

## Modelo desarrollado

Se construyó una red neuronal convolucional con capas de convolución, pooling, regularización mediante dropout y una capa final softmax para clasificación multiclase.

Debido al tamaño reducido del dataset, se incorporó aumento de datos mediante:

* Rotación leve.
* Zoom.
* Contraste.
* Volteo horizontal.

Esto permite mejorar la capacidad de generalización del modelo frente a variaciones visuales.

---

## Resultados principales

El modelo entrenado alcanzó un desempeño alto sobre el conjunto de prueba utilizado:

* Test loss: 0.0956
* Test accuracy: 1.0
* Imágenes analizadas: 285
* Clases: Defected1, Defected2, Normal

Este resultado indica que el modelo logró clasificar correctamente las imágenes del conjunto de prueba utilizado.

Sin embargo, debido al tamaño reducido del dataset, este resultado debe interpretarse con cautela. Para una implementación industrial real, sería necesario validar el modelo con una mayor cantidad de imágenes y con condiciones reales de operación.

---

## Archivos generados

El proyecto exporta resultados en las siguientes carpetas:

### Gráficos

```text
outputs/graficos/
```

Incluye gráficos como:

* Distribución de imágenes por clase.
* Ejemplos de imágenes por clase.
* Accuracy de entrenamiento y validación.
* Loss de entrenamiento y validación.
* Matriz de confusión.
* Ejemplos de predicción del modelo.

### Métricas

```text
outputs/metricas/
```

Incluye archivos CSV con:

* Historial de entrenamiento.
* Reporte de clasificación.
* Métricas resumen del modelo.
* Predicciones sobre el conjunto de prueba.

### Modelos

```text
outputs/modelos/
```

El modelo entrenado se guarda localmente en formato `.keras`, pero no se incluye en GitHub por tamaño y buenas prácticas de repositorio.

---

## Interpretación industrial

Desde una perspectiva industrial, este proyecto demuestra cómo la visión artificial puede apoyar procesos técnicos de inspección visual.

Una solución de este tipo puede ayudar a:

* Reducir tiempos de diagnóstico.
* Apoyar decisiones de mantenimiento.
* Estandarizar criterios de inspección.
* Detectar posibles defectos visuales.
* Complementar la experiencia del personal técnico.
* Mejorar procesos de control de calidad.

---

## Limitaciones

El proyecto presenta algunas limitaciones importantes:

* El dataset utilizado es pequeño.
* Las imágenes pertenecen a un contexto controlado.
* No se validó con imágenes reales capturadas en terreno.
* No se evaluaron condiciones variables de iluminación, suciedad, ángulo o desgaste.
* El modelo requiere mayor validación antes de una implementación productiva.

---

## Próximos pasos

Como continuación del proyecto, se propone:

* Ampliar el dataset con imágenes reales de componentes industriales.
* Incorporar nuevas clases de fallas mecánicas.
* Comparar la CNN simple con modelos de Transfer Learning.
* Evaluar arquitecturas como MobileNetV2, ResNet o EfficientNet.
* Crear una aplicación simple para cargar imágenes y obtener predicciones.
* Integrar el modelo con un sistema de inspección o mantenimiento.
* Generar un dashboard de seguimiento de fallas detectadas.

---

## Conclusión

Este proyecto demuestra la aplicación de redes neuronales convolucionales en un problema industrial de clasificación visual de componentes mecánicos.

Más allá del resultado técnico, el valor del proyecto está en conectar experiencia industrial, mantenimiento, control de calidad e inteligencia artificial aplicada.

El caso permite mostrar cómo herramientas de Data Science y Machine Learning pueden transformar procesos técnicos tradicionales en soluciones más automatizadas, medibles y escalables.
