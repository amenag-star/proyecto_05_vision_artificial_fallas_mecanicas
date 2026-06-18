from pathlib import Path
import numpy as np
import pandas as pd
from PIL import Image

import streamlit as st
import tensorflow as tf


# =========================
# Configuración general
# =========================

st.set_page_config(
    page_title="Detección de fallas mecánicas",
    page_icon="🔧",
    layout="centered"
)

PROJECT_ROOT = Path(__file__).resolve().parents[1]
MODEL_PATH = PROJECT_ROOT / "outputs" / "modelos" / "modelo_cnn_fallas_mecanicas.keras"

IMG_SIZE = (96, 96)
CLASS_NAMES = ["Defected1", "Defected2", "Normal"]


# =========================
# Funciones principales
# =========================

@st.cache_resource
def cargar_modelo():
    """Carga el modelo CNN entrenado."""
    model = tf.keras.models.load_model(MODEL_PATH)
    return model


def preprocesar_imagen(uploaded_file):
    """Prepara la imagen para que tenga el mismo formato usado en el entrenamiento."""
    image = Image.open(uploaded_file).convert("RGB")
    image_resized = image.resize(IMG_SIZE)

    image_array = np.array(image_resized).astype("float32") / 255.0
    image_array = np.expand_dims(image_array, axis=0)

    return image, image_array


def predecir_imagen(model, image_array):
    """Genera la predicción del modelo."""
    predictions = model.predict(image_array)
    probabilities = predictions[0]

    predicted_index = int(np.argmax(probabilities))
    predicted_class = CLASS_NAMES[predicted_index]
    confidence = float(probabilities[predicted_index])

    return predicted_class, confidence, probabilities


# =========================
# Interfaz
# =========================

st.title("🔧 Visión Artificial para Detección de Fallas Mecánicas")

st.write(
    """
    Esta aplicación utiliza un modelo CNN entrenado con TensorFlow/Keras para clasificar
    imágenes de componentes mecánicos en tres categorías:
    
    - **Defected1**
    - **Defected2**
    - **Normal**
    """
)

st.warning(
    """
    Este modelo fue entrenado con un dataset reducido. Sus resultados deben considerarse
    como apoyo experimental y no como diagnóstico industrial definitivo.
    """
)

st.divider()

uploaded_file = st.file_uploader(
    "Sube una imagen de una pieza mecánica",
    type=["jpg", "jpeg", "png", "bmp", "webp"]
)

if uploaded_file is not None:
    try:
        model = cargar_modelo()
        original_image, image_array = preprocesar_imagen(uploaded_file)

        st.subheader("Imagen cargada")
        st.image(original_image, use_container_width=True)

        predicted_class, confidence, probabilities = predecir_imagen(model, image_array)

        st.subheader("Resultado de la predicción")

        st.metric(
            label="Clase predicha",
            value=predicted_class,
            delta=f"Confianza: {confidence * 100:.2f}%"
        )

        probabilities_df = pd.DataFrame({
            "Clase": CLASS_NAMES,
            "Probabilidad": probabilities
        })

        probabilities_df["Probabilidad (%)"] = probabilities_df["Probabilidad"] * 100

        st.subheader("Probabilidad por clase")
        st.dataframe(
            probabilities_df[["Clase", "Probabilidad (%)"]],
            use_container_width=True
        )

        st.bar_chart(
            probabilities_df.set_index("Clase")["Probabilidad (%)"]
        )

        st.info(
            """
            Interpretación: la clase con mayor probabilidad es la seleccionada por el modelo.
            Para uso industrial real, se recomienda validar con más imágenes y condiciones
            variadas de iluminación, ángulo, desgaste y fondo.
            """
        )

    except Exception as e:
        st.error("Ocurrió un error al procesar la imagen.")
        st.exception(e)

else:
    st.info("Sube una imagen para ejecutar la predicción.")