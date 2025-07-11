import streamlit as st
import pickle
import os

# Load model and encoder
model = pickle.load(open("boosting.pkl", "rb"))
label_encoder = pickle.load(open("label_encoder.pkl", "rb"))

st.set_page_config(page_title="Crop Recommendation", page_icon="🌾")
st.title("Crop Recommendation System")

N = st.number_input("Nitrogen (N)")
P = st.number_input("Phosphorus (P)")
K = st.number_input("Potassium (K)")
temperature = st.number_input("Temperature (°C)")
humidity = st.number_input("Humidity (%)")
ph = st.number_input("pH level")
rainfall = st.number_input("Rainfall (mm)")

if st.button("Recommend"):
    # Make prediction
    input_data = [[N, P, K, temperature, humidity, ph, rainfall]]
    prediction = model.predict(input_data)
    predicted_crop = label_encoder.inverse_transform(prediction)[0]

    # Display the result
    st.success(f"Recommended Crop: {predicted_crop}")

    # Show image (must be inside this same block)
    import os
    image_path = f"images/{predicted_crop.lower()}.png"
    if os.path.exists(image_path):
        st.image(image_path, caption=predicted_crop, use_column_width=True)
    else:
        st.info("No image available for this crop.")
