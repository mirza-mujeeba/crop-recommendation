import streamlit as st
import numpy as np
import pickle

# Load model and label encoder
model = pickle.load(open("boosting.pkl", "rb"))
label_encoder = pickle.load(open("label_encoder.pkl", "rb"))

st.set_page_config(page_title="Crop Recommendation", page_icon="🌾")
st.title("🌾 Crop Recommendation System")

N = st.number_input("Nitrogen (N)")
P = st.number_input("Phosphorus (P)")
K = st.number_input("Potassium (K)")
temperature = st.number_input("Temperature (°C)")
humidity = st.number_input("Humidity (%)")
ph = st.number_input("pH level")
rainfall = st.number_input("Rainfall (mm)")

if st.button("Recommend Crop"):
    input_data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    prediction = model.predict(input_data)
    crop = label_encoder.inverse_transform(prediction)
    st.success(f"🌱 Recommended Crop: **{crop[0]}**")