import numpy as np
import streamlit as st
import tensorflow as tf
from PIL import Image

st.title("Boozeifier - Alcohol detection ")
st.write("Import image, then Boozeifier will judge if it's alcohol or not!")

@st.cache_resource
def load_boozeifier_model():
    model = tf.keras.models.load_model("boozeifier_model.keras")
    return model

try:
    boozeifier_model = load_boozeifier_model()
except FileNotFoundError:
    st.error("Model not found!")
    st.stop()

CLASS_NAMES = ["Alcohol", "Not an alcohol"]

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

st.divider()

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Imported image", width=200)

    st.subheader("Prediction")
    prepared_image = image.resize((200, 200))
    image_array = tf.keras.utils.img_to_array(prepared_image)
    image_array = tf.expand_dims(image_array, axis=0)

    predictions = boozeifier_model.predict(image_array)
    score = tf.nn.softmax(predictions[0])

    predicted_class = CLASS_NAMES[np.argmax(score)]
    confidence = 100 * score[np.argmax(score)].numpy()

    st.write(f"{predicted_class} ({confidence:.2f}% confidence)")
